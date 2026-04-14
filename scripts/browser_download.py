#!/usr/bin/env python3
"""
AI Security Guide – Headless Browser Paper Downloader

Uses Playwright / Chromium to download PDFs that fail with direct HTTP
requests.  arXiv blocks Python's urllib3 TLS fingerprint but serves PDFs
normally to real browsers.

Usage:
    python3 scripts/browser_download.py              # retry all failed
    python3 scripts/browser_download.py --all        # re-download everything
    python3 scripts/browser_download.py --url URL    # download a single URL

After a successful run, raw/manifest.json is updated in place.
"""

import argparse
import asyncio
import hashlib
import json
import re
import sys
from pathlib import Path

from playwright.async_api import async_playwright, TimeoutError as PwTimeout

# ── Paths ─────────────────────────────────────────────────────────────────────
REPO_ROOT = Path(__file__).parent.parent
MANIFEST   = REPO_ROOT / "raw" / "manifest.json"
OUTPUT_DIR = REPO_ROOT / "raw" / "papers"

# ── Helpers (duplicated from download_papers.py for standalone use) ────────────

def make_filename(url: str) -> str:
    m = re.search(r"arxiv\.org/pdf/([\d.v]+)", url)
    if m:
        return f"arxiv_{m.group(1)}.pdf"
    if "usenix.org" in url:
        base = url.rstrip("/").split("/")[-1]
        if base.endswith(".pdf"):
            return base[:120]
    if "dl.acm.org" in url:
        m2 = re.search(r"10\.\d+/(.+)", url)
        if m2:
            return "acm_" + re.sub(r"[^\w.-]", "_", m2.group(1))[:80] + ".pdf"
    if "neurips.cc" in url or "proceedings.neurips" in url:
        base = url.rstrip("/").split("/")[-1]
        if base.endswith(".pdf"):
            return base[:120]
    base = url.split("?")[0].rstrip("/").split("/")[-1]
    if base.endswith(".pdf") and len(base) > 6:
        return re.sub(r"[^\w.-]", "_", base)[:120]
    return f"paper_{hashlib.md5(url.encode()).hexdigest()[:12]}.pdf"


def dest_for(meta: dict) -> Path:
    """Reconstruct output path from manifest metadata."""
    if "file" in meta:
        return REPO_ROOT / meta["file"]
    src = meta.get("source_file", "")
    parts = Path(src).parts
    if len(parts) >= 2:
        d = OUTPUT_DIR / parts[0] / parts[1]
    else:
        d = OUTPUT_DIR / "misc"
    d.mkdir(parents=True, exist_ok=True)
    return d / make_filename(meta["url"])


# ── Core download ──────────────────────────────────────────────────────────────

ARXIV_RE = re.compile(r"arxiv\.org")

async def fetch_pdf(page, url: str) -> tuple[bool, str, bytes]:
    """
    Navigate to `url` with Playwright and return (success, message, bytes).

    Strategy:
      1. Go to the URL; capture the navigation response body.
      2. If it's a PDF (%PDF magic), return it.
      3. If the server forces a download (Content-Disposition: attachment),
         page.goto() raises "Download is starting" — catch it and wait for
         the download event to deliver the file bytes.
      4. If it's an HTML page (e.g. arXiv abs), look for the PDF link and recurse.
    """
    download_result: list[bytes] = []
    download_ready = asyncio.Event()

    async def on_download(dl):
        try:
            path = await dl.path()
            if path:
                download_result.append(Path(path).read_bytes())
        except Exception:
            pass
        finally:
            download_ready.set()

    page.on("download", on_download)
    response = None

    try:
        try:
            response = await page.goto(url, wait_until="domcontentloaded",
                                        timeout=40_000)
        except PwTimeout:
            return False, "Navigation timeout", b""
        except Exception as nav_exc:
            if "Download is starting" not in str(nav_exc):
                return False, str(nav_exc)[:100], b""
            # Server sent Content-Disposition: attachment — wait for download
            try:
                await asyncio.wait_for(download_ready.wait(), timeout=20)
            except asyncio.TimeoutError:
                return False, "Download timeout", b""
            data = download_result[0] if download_result else b""
            if data.startswith(b"%PDF"):
                return True, "forced-download", data
            return False, "download-not-pdf", b""

        if not response:
            return False, "No response", b""

        status = response.status
        if status not in (200, 206):
            return False, f"HTTP {status}", b""

        # Some navigations trigger a download alongside the response
        if download_ready.is_set() and download_result:
            data = download_result[0]
            if data.startswith(b"%PDF"):
                return True, "inline-download", data

        # Read the response body
        try:
            body = await response.body()
        except Exception:
            body = b""

        if body.startswith(b"%PDF"):
            return True, "inline-pdf", body

        # HTML page — look for a PDF link (arXiv abs page, etc.)
        ct = (response.headers.get("content-type") or "").lower()
        if "html" in ct and ARXIV_RE.search(url):
            # Try the canonical PDF link from the abs page
            href = await page.evaluate("""
                () => {
                    const a = document.querySelector(
                        'a[href*="/pdf/"], a.abs-button[href*="pdf"]'
                    );
                    return a ? a.href : null;
                }
            """)
            if href and href != url:
                page.remove_listener("download", on_download)
                return await fetch_pdf(page, href)

        return False, f"Not a PDF (ct={ct[:30]}, {len(body)}B)", b""

    except PwTimeout:
        return False, "Timeout", b""
    except Exception as exc:
        return False, str(exc)[:100], b""
    finally:
        try:
            page.remove_listener("download", on_download)
        except Exception:
            pass


async def download_one(page, meta: dict) -> tuple[bool, str, int]:
    url  = meta["url"]
    dest = dest_for(meta)

    if dest.exists() and dest.stat().st_size > 512:
        return True, "cached", dest.stat().st_size

    dest.parent.mkdir(parents=True, exist_ok=True)

    ok, msg, data = await fetch_pdf(page, url)
    if ok and data:
        dest.write_bytes(data)
        return True, msg, len(data)
    return False, msg, 0


# ── Parallel download ──────────────────────────────────────────────────────────

# Per-domain delay AFTER each request (seconds)
DELAY_ARXIV = 1.0
DELAY_OTHER = 0.8


async def worker(ctx, meta: dict, total: int,
                 downloaded: list, failed: list,
                 sem_arxiv: asyncio.Semaphore,
                 sem_other: asyncio.Semaphore,
                 lock: asyncio.Lock,
                 counter: list) -> None:
    """One async worker: acquire semaphore → create page → download → release."""
    url = meta["url"]
    is_arxiv = "arxiv.org" in url
    sem   = sem_arxiv if is_arxiv else sem_other
    delay = DELAY_ARXIV if is_arxiv else DELAY_OTHER

    async with sem:
        page = await ctx.new_page()
        try:
            ok, msg, size = await download_one(page, meta)
        finally:
            await page.close()

        async with lock:
            counter[0] += 1
            idx = counter[0]
            label = (url[:65] + "…") if len(url) > 68 else url
            if ok:
                dest = dest_for(meta)
                entry = {**meta, "file": str(dest.relative_to(REPO_ROOT)),
                         "size": size}
                tag = "SKIP" if msg == "cached" else "OK  "
                print(f"[{idx:3d}/{total}] {tag}  {size // 1024:5d} KB  {label}")
                downloaded.append(entry)
            else:
                print(f"[{idx:3d}/{total}] FAIL  {msg[:30]:30s}  {label}")
                failed.append({**meta, "error": msg})

        await asyncio.sleep(delay)


# ── Main ──────────────────────────────────────────────────────────────────────

async def run(targets: list[dict]) -> dict:
    """Download `targets` concurrently and return {downloaded, failed} dicts."""
    downloaded: list = []
    failed:     list = []
    total = len(targets)

    # Semaphores must be created inside the running event loop
    sem_arxiv = asyncio.Semaphore(6)   # arXiv: 6 concurrent
    sem_other = asyncio.Semaphore(4)   # everything else: 4 concurrent
    lock      = asyncio.Lock()
    counter   = [0]                    # mutable counter shared across workers

    async with async_playwright() as pw:
        browser = await pw.chromium.launch(
            headless=True,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--disable-dev-shm-usage",
                "--no-sandbox",
            ],
        )
        ctx = await browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            ),
            accept_downloads=True,
            viewport={"width": 1280, "height": 800},
        )

        tasks = [
            worker(ctx, meta, total, downloaded, failed,
                   sem_arxiv, sem_other, lock, counter)
            for meta in targets
        ]
        await asyncio.gather(*tasks)
        await browser.close()

    return {"downloaded": downloaded, "failed": failed}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--all", action="store_true",
                        help="Re-attempt every URL in the manifest (not just failures)")
    parser.add_argument("--url", metavar="URL",
                        help="Download a single URL (adds to manifest)")
    args = parser.parse_args()

    # ── Load manifest ────────────────────────────────────────────────────────
    if not MANIFEST.exists():
        print(f"[error] manifest not found: {MANIFEST}")
        sys.exit(1)

    manifest = json.loads(MANIFEST.read_text())

    # ── Build target list ────────────────────────────────────────────────────
    if args.url:
        targets = [{"url": args.url, "text": "manual", "source_file": "misc/misc.md",
                    "sources": ["manual"]}]
    elif args.all:
        targets = manifest.get("failed", []) + manifest.get("downloaded", []) + \
                  manifest.get("skipped", [])
    else:
        targets = manifest.get("failed", [])

    if not targets:
        print("Nothing to download.")
        return

    print(f"{'='*60}")
    print(f"AI Security Guide – Headless Browser Downloader")
    print(f"Targets : {len(targets)}")
    print(f"Browser : Chromium (Playwright)")
    print(f"{'='*60}\n")

    result = asyncio.run(run(targets))

    # ── Update manifest ──────────────────────────────────────────────────────
    if not args.url:
        # Merge: keep existing successes, replace failures
        existing_ok = {e["url"] for e in manifest.get("downloaded", [])
                       if e["url"] not in {f["url"] for f in result["failed"]}}
        prev_ok = [e for e in manifest.get("downloaded", [])
                   if e["url"] in existing_ok]
        manifest["downloaded"] = prev_ok + [
            e for e in result["downloaded"] if e.get("size", 0) > 512
        ]
        manifest["failed"] = result["failed"]
        MANIFEST.write_text(json.dumps(manifest, indent=2))

    print(f"\n{'='*60}")
    print(f"Downloaded : {len(result['downloaded'])} papers")
    print(f"Failed     : {len(result['failed'])} papers")

    if result["failed"]:
        print("\nStill failing (may need institutional access):")
        for f in result["failed"][:15]:
            print(f"  [{f['error'][:25]:25s}] {f['url'][:60]}")


if __name__ == "__main__":
    main()

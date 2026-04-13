#!/usr/bin/env python3
"""
AI Security Guide – Paper Downloader
Scans all markdown files in the repo, extracts paper URLs,
and downloads PDFs into raw/papers/ organized by section.

Rate-limits arXiv requests (3s) and other hosts (1s) to be
respectful. Writes a manifest to raw/manifest.json.
"""

import re
import os
import time
import json
import hashlib
import requests
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
OUTPUT_DIR = REPO_ROOT / "raw" / "papers"
MANIFEST_FILE = REPO_ROOT / "raw" / "manifest.json"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (compatible; AI-Security-Guide-Archive/1.0; "
        "Academic Research; https://github.com/nabeelxy/ai-security-guide)"
    )
}

# Domains/text patterns that indicate non-paper links to skip
SKIP_URL_FRAGMENTS = [
    "github.com", "notebooklm", "huggingface.co", "linkedin.com",
    "agentwild-workshop", "rdi.berkeley", "llm-vulnerability.github",
    "hiddenlayer.com/innovation", "unit42.palo", "blogs.cisco",
    "anthropic.com/research", "anthropic.com/news", "meta.com",
]
SKIP_TEXT_FRAGMENTS = [
    "github", "notebooklm", "podcast", "demo", "site", "blog",
    "talk", "tutorial", "slides", "report on", "article",
]

# Domains that indicate actual paper / PDF links
PAPER_URL_FRAGMENTS = [
    "arxiv.org", "usenix.org", "dl.acm.org/doi/pdf",
    "ieeecomputer.org", "proceedings.neurips.cc",
    "openreview.net", "aclanthology.org",
]
# Direct PDF hosts that are legitimate paper sources
DIRECT_PDF_HOSTS = [
    "cdn.anthropic.com", "www-cdn.anthropic.com",
    "fbcdn.net", "storage.googleapis.com",
    "github.io",  # many author-hosted PDFs
    "jaehanwork.github.io",
    "scontent-lax3",
    "assets.anthropic.com",
    "media.licdn.com",
]


def normalize_url(url: str) -> str:
    """Normalize arxiv abs → pdf; strip expiring IEEE signed params."""
    # arxiv abs → pdf
    if "arxiv.org/abs/" in url:
        m = re.search(r"arxiv\.org/abs/([\d.]+)", url)
        if m:
            return f"https://arxiv.org/pdf/{m.group(1)}"
    # Strip expiring signed query params (IEEE, etc.)
    if "ieeecomputer.org" in url and "?" in url:
        return url.split("?")[0]
    # Strip version suffix on arxiv PDF if present (keep it for accuracy)
    return url


def is_paper_url(url: str, text: str) -> bool:
    url_l = url.lower()
    text_l = text.lower()

    # Explicit skips
    if any(f in url_l for f in SKIP_URL_FRAGMENTS):
        return False
    if any(f in text_l for f in SKIP_TEXT_FRAGMENTS):
        # Allow direct PDFs even if text says "report"
        if url_l.endswith(".pdf") and any(d in url_l for d in DIRECT_PDF_HOSTS):
            return True
        return False

    # Must match a known paper source
    if any(f in url_l for f in PAPER_URL_FRAGMENTS):
        return True
    if url_l.endswith(".pdf") and any(d in url_l for d in DIRECT_PDF_HOSTS):
        return True

    return False


def extract_paper_urls(md_file: Path) -> list[dict]:
    """Return list of {url, text, source_file} for paper links in a markdown file."""
    try:
        content = md_file.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return []

    links = re.findall(r"\[([^\]]*)\]\((https?://[^\)\s]+)\)", content)
    results = []
    seen_urls = set()

    for text, url in links:
        url = normalize_url(url.strip())
        if url in seen_urls:
            continue
        if is_paper_url(url, text):
            seen_urls.add(url)
            results.append({
                "url": url,
                "text": text.strip(),
                "source_file": str(md_file.relative_to(REPO_ROOT)),
            })
    return results


def make_filename(url: str) -> str:
    """Generate a filesystem-safe filename for the paper."""
    # arXiv
    m = re.search(r"arxiv\.org/pdf/([\d.v]+)", url)
    if m:
        return f"arxiv_{m.group(1)}.pdf"

    # USENIX
    if "usenix.org" in url:
        base = url.rstrip("/").split("/")[-1]
        if base.endswith(".pdf"):
            return base[:120]

    # ACM
    if "dl.acm.org" in url:
        m = re.search(r"10\.\d+/(.+)", url)
        if m:
            return "acm_" + re.sub(r"[^\w.-]", "_", m.group(1))[:80] + ".pdf"

    # NeurIPS
    if "neurips.cc" in url or "proceedings.neurips" in url:
        base = url.rstrip("/").split("/")[-1]
        if base.endswith(".pdf"):
            return base[:120]

    # Generic PDF
    base = url.split("?")[0].rstrip("/").split("/")[-1]
    if base.endswith(".pdf") and len(base) > 6:
        return re.sub(r"[^\w.-]", "_", base)[:120]

    # Fallback: hash
    h = hashlib.md5(url.encode()).hexdigest()[:12]
    return f"paper_{h}.pdf"


def section_dir(source_file: str) -> Path:
    """Map source file path to output subdirectory."""
    parts = Path(source_file).parts
    if len(parts) >= 2:
        top = parts[0]          # e.g. security_for_ai
        sub = parts[1]          # e.g. llm_security
        return OUTPUT_DIR / top / sub
    return OUTPUT_DIR / "misc"


def download_pdf(url: str, dest: Path) -> tuple[bool, str, int]:
    """Download url to dest. Returns (success, status_msg, bytes)."""
    try:
        resp = requests.get(url, headers=HEADERS, timeout=40,
                            stream=True, allow_redirects=True)
        if resp.status_code != 200:
            return False, f"HTTP {resp.status_code}", 0

        content = b"".join(resp.iter_content(chunk_size=16384))

        # Validate PDF magic bytes
        if not content.startswith(b"%PDF"):
            ct = resp.headers.get("content-type", "")
            return False, f"Not a PDF (ct={ct[:40]})", 0

        dest.write_bytes(content)
        return True, "OK", len(content)

    except requests.exceptions.Timeout:
        return False, "Timeout", 0
    except Exception as exc:
        return False, str(exc)[:80], 0


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("=" * 60)
    print("AI Security Guide – Paper Downloader")
    print("=" * 60)
    print(f"\nScanning markdown files in: {REPO_ROOT}\n")

    # Collect all unique paper URLs across all .md files
    all_papers: dict[str, dict] = {}
    for md_file in sorted(REPO_ROOT.rglob("*.md")):
        if ".git" in md_file.parts or "raw" in md_file.parts:
            continue
        for p in extract_paper_urls(md_file):
            url = p["url"]
            if url not in all_papers:
                all_papers[url] = {**p, "sources": [p["source_file"]]}
            else:
                if p["source_file"] not in all_papers[url]["sources"]:
                    all_papers[url]["sources"].append(p["source_file"])

    print(f"Found {len(all_papers)} unique paper URLs\n")

    manifest: dict[str, list] = {"downloaded": [], "failed": [], "skipped": []}
    total = len(all_papers)

    for i, (url, meta) in enumerate(all_papers.items(), 1):
        dest_dir = section_dir(meta["source_file"])
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest = dest_dir / make_filename(url)

        short_url = (url[:72] + "...") if len(url) > 75 else url
        print(f"[{i:3d}/{total}] {short_url}")

        if dest.exists() and dest.stat().st_size > 1024:
            sz = dest.stat().st_size
            print(f"         SKIP  (cached {sz // 1024} KB)")
            manifest["skipped"].append(
                {**meta, "file": str(dest.relative_to(REPO_ROOT)), "size": sz}
            )
            continue

        ok, msg, size = download_pdf(url, dest)

        if ok:
            print(f"         OK    {size // 1024} KB → {dest.relative_to(REPO_ROOT)}")
            manifest["downloaded"].append(
                {**meta, "file": str(dest.relative_to(REPO_ROOT)), "size": size}
            )
        else:
            print(f"         FAIL  {msg}")
            if dest.exists():
                dest.unlink(missing_ok=True)
            manifest["failed"].append({**meta, "error": msg})

        # Respectful rate limiting
        delay = 3.5 if "arxiv.org" in url else 1.0
        time.sleep(delay)

    # Write manifest
    MANIFEST_FILE.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST_FILE.write_text(json.dumps(manifest, indent=2))

    print("\n" + "=" * 60)
    print(f"Downloaded : {len(manifest['downloaded'])} papers")
    print(f"Cached     : {len(manifest['skipped'])} (already present)")
    print(f"Failed     : {len(manifest['failed'])} (paywalled / unavailable)")
    print(f"Manifest   : raw/manifest.json")

    if manifest["failed"]:
        print("\nFailed URLs:")
        for f in manifest["failed"]:
            print(f"  [{f['error'][:20]:20s}] {f['url'][:70]}")


if __name__ == "__main__":
    main()

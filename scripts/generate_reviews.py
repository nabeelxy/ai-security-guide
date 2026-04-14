#!/usr/bin/env python3
"""
AI Security Guide – Automated Review Generator

Reads downloaded PDFs from raw/papers/, extracts text with PyMuPDF,
sends each paper to Claude (claude-sonnet-4-6) and generates a structured
8-section review matching the existing reviews/ format.

Requirements:
    ANTHROPIC_API_KEY environment variable must be set.
    pip install anthropic pymupdf

Usage:
    # Generate reviews for all papers that don't have one yet
    python3 scripts/generate_reviews.py

    # Limit to N papers (useful for a first test run)
    python3 scripts/generate_reviews.py --limit 5

    # Force-regenerate reviews even if they already exist
    python3 scripts/generate_reviews.py --force

    # Only process papers in a specific section
    python3 scripts/generate_reviews.py --section security_for_ai/llm_security
"""

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

import fitz  # PyMuPDF
import anthropic

# ── Config ────────────────────────────────────────────────────────────────────
REPO_ROOT   = Path(__file__).parent.parent
MANIFEST    = REPO_ROOT / "raw" / "manifest.json"
MAX_CHARS   = 60_000   # ~15k tokens — enough for a thorough review
MODEL       = "claude-sonnet-4-6"

REVIEW_PROMPT = """\
You are an expert AI security researcher writing a structured review of an \
academic paper for a curated knowledge base.

Read the paper text below and write a review following EXACTLY this format \
(8 sections, markdown, no extra sections):

# {title}

#### **What is this paper about?**
2-3 paragraphs. Plain-language explanation accessible to a senior engineer \
who isn't a specialist. Include one concrete analogy.

---

#### **Key Contributions**
Bulleted list (3-5 items). Each bullet is a crisp, specific contribution.

---

#### **Key Findings**
Bulleted list (3-5 items). Concrete results, numbers, success rates where \
available.

---

#### **Main Limitations or Drawbacks**
Bulleted list (2-4 items). Honest assessment of what the paper doesn't cover \
or where results may not generalise.

---

#### **Previous Works Evaluated and Compared**
How does this paper position itself against prior work? What baselines does \
it beat and by how much?

---

#### **How to Productionize this Research Result**
Bulleted list (3-4 items). Concrete, actionable steps for a security or ML \
engineer deploying this in a real system.

---

#### **Research Gaps Still Existing**
Bulleted list (3-4 items). Open questions this paper leaves unanswered, or \
new questions it raises.

---

Write only the review. Do not add preamble, disclaimers, or any text outside \
the eight sections above.

PAPER TEXT:
{text}
"""

# ── PDF helpers ───────────────────────────────────────────────────────────────

def extract_text(pdf_path: Path, max_chars: int = MAX_CHARS) -> str:
    """Extract plain text from a PDF, truncating to max_chars."""
    try:
        doc = fitz.open(str(pdf_path))
        parts = []
        for page in doc:
            parts.append(page.get_text("text"))
        doc.close()
        text = "\n".join(parts)
        # Remove null bytes and excessive whitespace
        text = re.sub(r"\x00", "", text)
        text = re.sub(r"\n{4,}", "\n\n\n", text)
        return text[:max_chars]
    except Exception as exc:
        return f"[PDF extraction failed: {exc}]"


def guess_title(pdf_path: Path, meta: dict) -> str:
    """Best-effort title extraction: manifest text → PDF first line → filename."""
    # Use the link text from the manifest as a title hint
    txt = meta.get("text", "").strip()
    if txt and txt.lower() not in {"paper", "pdf", "arxiv", "link"}:
        return txt

    # Try first non-empty line of the PDF
    try:
        doc = fitz.open(str(pdf_path))
        for page in doc:
            for line in page.get_text("text").splitlines():
                line = line.strip()
                if len(line) > 10:
                    doc.close()
                    return line[:200]
        doc.close()
    except Exception:
        pass

    return pdf_path.stem.replace("_", " ").replace("-", " ").title()


# ── Review path helpers ───────────────────────────────────────────────────────

def arxiv_id_from_url(url: str) -> str | None:
    m = re.search(r"arxiv\.org/(?:pdf|abs)/([\d.v]+)", url)
    return m.group(1) if m else None


def reviews_dir_for(source_file: str) -> Path | None:
    """
    Map a source markdown file path to the section's reviews/ directory.
    E.g. 'security_for_ai/llm_security/README.md'
      →  REPO_ROOT / 'security_for_ai/llm_security/reviews'
    """
    parts = Path(source_file).parts
    if len(parts) < 2:
        return None
    # Use up to depth 2 (top-level + subsection)
    section = REPO_ROOT / parts[0] / parts[1]
    reviews = section / "reviews"
    reviews.mkdir(parents=True, exist_ok=True)
    return reviews


def review_filename(meta: dict) -> str:
    arxiv = arxiv_id_from_url(meta["url"])
    if arxiv:
        return f"review-{arxiv}.md"
    h = meta["url"].split("/")[-1].split("?")[0]
    h = re.sub(r"[^\w.-]", "_", h)[:60]
    return f"review-{h}.md"


# ── Claude call ───────────────────────────────────────────────────────────────

def generate_review(client: anthropic.Anthropic, title: str, text: str) -> str:
    prompt = REVIEW_PROMPT.format(title=title, text=text)
    msg = client.messages.create(
        model=MODEL,
        max_tokens=2048,
        messages=[{"role": "user", "content": prompt}],
    )
    return msg.content[0].text.strip()


# ── README table updater ──────────────────────────────────────────────────────

def update_readme_table(source_file: str, url: str, review_path: Path) -> bool:
    """
    Update the Summary column of the publication table in the section README.
    Finds the row whose Material cell contains the URL and adds a Review link.
    Returns True if the README was modified.
    """
    readme = REPO_ROOT / Path(source_file).parts[0] / Path(source_file).parts[1] / "README.md"
    if not readme.exists():
        return False

    content = readme.read_text(encoding="utf-8")

    # Find the table row containing this URL
    # Pattern: any line with the URL and an empty last column (| |)
    arxiv_id = arxiv_id_from_url(url)
    search = arxiv_id or url.split("/")[-1][:30]

    # Build relative review link from the README's directory
    rel = review_path.relative_to(readme.parent)
    link = f"[Review]({rel})"

    lines = content.splitlines()
    changed = False
    for i, line in enumerate(lines):
        if search in line and line.strip().startswith("|"):
            cells = line.split("|")
            # Summary is typically the last non-empty cell
            # Only update if the summary cell is empty
            if len(cells) >= 2:
                last_content = cells[-2].strip()  # second-to-last (last is trailing |)
                if last_content == "":
                    cells[-2] = f" {link} "
                    lines[i] = "|".join(cells)
                    changed = True
                    break

    if changed:
        readme.write_text("\n".join(lines), encoding="utf-8")
    return changed


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--limit", type=int, default=0,
                        help="Max number of reviews to generate (0 = unlimited)")
    parser.add_argument("--force", action="store_true",
                        help="Regenerate reviews that already exist")
    parser.add_argument("--section", metavar="PATH",
                        help="Only process papers whose source_file starts with PATH")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be done without calling the API")
    args = parser.parse_args()

    # ── API key ──────────────────────────────────────────────────────────────
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key and not args.dry_run:
        print("[error] ANTHROPIC_API_KEY is not set.")
        print("  export ANTHROPIC_API_KEY=sk-ant-...")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key) if api_key else None

    # ── Load manifest ────────────────────────────────────────────────────────
    if not MANIFEST.exists():
        print(f"[error] Manifest not found: {MANIFEST}")
        sys.exit(1)

    manifest = json.loads(MANIFEST.read_text())
    papers = [p for p in manifest.get("downloaded", []) if p.get("size", 0) > 512]

    print(f"{'='*60}")
    print(f"AI Security Guide – Review Generator")
    print(f"Model       : {MODEL}")
    print(f"Papers      : {len(papers)} downloaded")
    print(f"Dry run     : {args.dry_run}")
    print(f"{'='*60}\n")

    generated = 0
    skipped   = 0
    errors    = 0

    for meta in papers:
        # ── Section filter ───────────────────────────────────────────────────
        src = meta.get("source_file", "")
        if args.section and not src.startswith(args.section):
            continue

        # ── Locate PDF ───────────────────────────────────────────────────────
        file_rel = meta.get("file", "")
        pdf_path = REPO_ROOT / file_rel if file_rel else None
        if not pdf_path or not pdf_path.exists():
            continue

        # ── Determine review output path ─────────────────────────────────────
        rev_dir = reviews_dir_for(src)
        if rev_dir is None:
            continue
        rev_file = rev_dir / review_filename(meta)

        if rev_file.exists() and not args.force:
            skipped += 1
            continue

        # ── Check limit ──────────────────────────────────────────────────────
        if args.limit and generated >= args.limit:
            break

        # ── Extract PDF text ─────────────────────────────────────────────────
        title = guess_title(pdf_path, meta)
        url   = meta["url"]

        print(f"[{generated+1}] {title[:70]}")
        print(f"     src : {pdf_path.name}")
        print(f"     dest: {rev_file.relative_to(REPO_ROOT)}")

        if args.dry_run:
            print(f"     [dry-run — skipping API call]\n")
            generated += 1
            continue

        text = extract_text(pdf_path)
        if not text or text.startswith("[PDF extraction failed"):
            print(f"     SKIP — could not extract text\n")
            errors += 1
            continue

        # ── Call Claude ──────────────────────────────────────────────────────
        try:
            review = generate_review(client, title, text)
        except anthropic.RateLimitError:
            print("     Rate-limited — waiting 60s …")
            time.sleep(60)
            try:
                review = generate_review(client, title, text)
            except Exception as exc:
                print(f"     FAIL after retry: {exc}\n")
                errors += 1
                continue
        except Exception as exc:
            print(f"     FAIL: {exc}\n")
            errors += 1
            continue

        # ── Save review ──────────────────────────────────────────────────────
        rev_file.write_text(review, encoding="utf-8")
        print(f"     OK  → {len(review)} chars\n")

        # ── Update README table ──────────────────────────────────────────────
        updated = update_readme_table(src, url, rev_file)
        if updated:
            print(f"     README table updated")

        generated += 1
        # Small delay to avoid hammering the API
        time.sleep(1)

    print(f"\n{'='*60}")
    print(f"Reviews generated : {generated}")
    print(f"Skipped (exist)   : {skipped}")
    print(f"Errors            : {errors}")
    if generated > 0:
        est = generated * 0.01
        print(f"Estimated API cost: ~${est:.2f}")


if __name__ == "__main__":
    main()

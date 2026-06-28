#!/usr/bin/env python3
"""One-time migration: Tinkerer RST -> Hugo Markdown.

Walks the legacy YYYY/MM/DD/slug.rst posts and pages/*.rst, converts the body
with pandoc (rst -> gfm), lifts the Tinkerer footer metadata
(.. author/categories/tags/comments) into Hugo YAML front matter, and writes
Hugo leaf bundles under content/, copying each post's co-located images.

Run once from the repo root:  python3 migrate.py
The 4 posts using Runestone interactive directives still need a manual pass.
"""
from __future__ import annotations

import re
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
YEAR_DIRS = ["2019", "2020", "2021", "2022", "2023", "2024", "2025", "2026"]

# Pages that redirect externally (mirrors the old conf.py sphinx-reredirects).
PAGE_REDIRECTS = {
    "about": "https://landing.runestone.academy",
    "library": "https://runestone.academy/ns/books/index",
}

FOOTER_RE = re.compile(r"^\.\.\s+(author|categories|tags|comments)::(.*)$")


def yaml_escape(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def split_footer(text: str):
    """Return (body_without_footer, meta dict)."""
    meta = {"author": "", "categories": "", "tags": ""}
    kept = []
    for line in text.splitlines():
        m = FOOTER_RE.match(line.strip())
        if m:
            key, val = m.group(1), m.group(2).strip()
            if key in meta:
                meta[key] = val
            continue
        kept.append(line)
    return "\n".join(kept), meta


def strip_sphinx_only(body: str) -> str:
    """Drop directives that have no Hugo equivalent: toctree, contents."""
    out, lines, i = [], body.splitlines(), 0
    while i < len(lines):
        stripped = lines[i].lstrip()
        if stripped.startswith((".. toctree::", ".. contents::")):
            # skip the directive line plus its indented option/content block
            i += 1
            while i < len(lines) and (lines[i].strip() == "" or lines[i][:1] in (" ", "\t")):
                i += 1
            continue
        out.append(lines[i])
        i += 1
    return "\n".join(out)


def extract_title(body: str):
    """Pull the first RST section title; return (title, remaining_body)."""
    lines = body.splitlines()
    # skip leading blanks / role definitions
    n = 0
    while n < len(lines) and lines[n].strip() == "":
        n += 1
    if n + 1 < len(lines) and re.fullmatch(r"[=\-~^\"#*]+", lines[n + 1].strip() or "x"):
        title = lines[n].strip()
        rest = lines[n + 2:]
        return title, "\n".join(rest)
    return "", body


def parse_list(val: str):
    items = [p.strip() for p in val.split(",") if p.strip()]
    return [i for i in items if i.lower() != "none"]


def pandoc(rst: str) -> str:
    res = subprocess.run(
        # shift headings down one: the post title is the page H1 (from front
        # matter), so in-body sections become H2 and below.
        ["pandoc", "-f", "rst", "-t", "gfm", "--wrap=none",
         "--shift-heading-level-by=1"],
        input=rst, text=True, capture_output=True,
    )
    if res.returncode != 0:
        raise RuntimeError(res.stderr)
    return res.stdout


def build_front_matter(fields: dict) -> str:
    out = ["---"]
    for k, v in fields.items():
        if v in (None, "", []):
            continue
        if isinstance(v, list):
            out.append(f"{k}:")
            out.extend(f"  - {yaml_escape(x)}" for x in v)
        elif isinstance(v, bool):
            out.append(f"{k}: {str(v).lower()}")
        else:
            out.append(f"{k}: {yaml_escape(str(v))}")
    out.append("---")
    return "\n".join(out) + "\n\n"


def copy_assets(src_dir: Path, dest_dir: Path):
    for f in src_dir.iterdir():
        if f.is_file() and f.suffix.lower() != ".rst":
            shutil.copy2(f, dest_dir / f.name)


def convert_post(rst_path: Path):
    parts = rst_path.relative_to(ROOT).parts  # year, mm, dd, slug.rst
    year, mm, dd = parts[0], parts[1], parts[2]
    slug = rst_path.stem
    raw = rst_path.read_text(encoding="utf-8")
    body, meta = split_footer(raw)
    title, body = extract_title(body)
    body = strip_sphinx_only(body)
    md = pandoc(body)

    authors = [a for a in parse_list(meta["author"]) if a.lower() != "default"]
    fm = build_front_matter({
        "title": title,
        "date": f"{year}-{mm}-{dd}",
        "slug": slug,
        "categories": parse_list(meta["categories"]),
        "tags": parse_list(meta["tags"]),
        "author": authors,
    })

    dest = ROOT / "content" / "posts" / year / f"{mm}-{dd}-{slug}"
    dest.mkdir(parents=True, exist_ok=True)
    (dest / "index.md").write_text(fm + md, encoding="utf-8")
    copy_assets(rst_path.parent, dest)
    return dest


def convert_page(rst_path: Path):
    slug = rst_path.stem
    raw = rst_path.read_text(encoding="utf-8")
    body, meta = split_footer(raw)
    title, body = extract_title(body)
    body = strip_sphinx_only(body)
    md = pandoc(body)

    fields = {"title": title, "slug": slug, "type": "pages"}
    if slug in PAGE_REDIRECTS:
        fields["redirect"] = PAGE_REDIRECTS[slug]
    fm = build_front_matter(fields)

    dest = ROOT / "content" / "pages" / slug
    dest.mkdir(parents=True, exist_ok=True)
    (dest / "index.md").write_text(fm + md, encoding="utf-8")
    copy_assets(rst_path.parent, dest)
    return dest


def main():
    posts = []
    for y in YEAR_DIRS:
        posts += sorted((ROOT / y).rglob("*.rst"))
    print(f"Converting {len(posts)} posts...")
    for p in posts:
        try:
            convert_post(p)
        except Exception as e:
            print(f"  !! {p}: {e}")

    pages = sorted((ROOT / "pages").glob("*.rst"))
    print(f"Converting {len(pages)} pages...")
    for p in pages:
        try:
            convert_page(p)
        except Exception as e:
            print(f"  !! {p}: {e}")
    print("Done.")


if __name__ == "__main__":
    main()

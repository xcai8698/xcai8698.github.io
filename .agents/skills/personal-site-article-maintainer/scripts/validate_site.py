#!/usr/bin/env python3
"""Lightweight structural and local-link checks for the personal HTML site."""
from __future__ import annotations

import argparse
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: set[str] = set()
        self.links: list[tuple[str, str]] = []
        self.styles: list[str] = []
        self.scripts: list[str] = []
        self.h1_count = 0
        self.title_seen = False
        self.description_seen = False
        self.time_values: list[str] = []
        self.inline_styles = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        a = dict(attrs)
        if tag == "h1":
            self.h1_count += 1
        if tag == "meta" and a.get("name", "").lower() == "description" and a.get("content", "").strip():
            self.description_seen = True
        if tag == "time" and a.get("datetime"):
            self.time_values.append(a["datetime"] or "")
        if tag == "link" and a.get("href") and "stylesheet" in (a.get("rel") or "").lower():
            self.styles.append(a["href"] or "")
        if tag == "script" and a.get("src"):
            self.scripts.append(a["src"] or "")
        if tag in {"a", "link", "img", "script"}:
            attr = "src" if tag in {"img", "script"} else "href"
            if a.get(attr):
                self.links.append((tag, a[attr] or ""))
        if a.get("id"):
            self.ids.add(a["id"] or "")
        if "style" in a:
            self.inline_styles += 1

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self.title_seen = True


def parse(path: Path) -> PageParser:
    parser = PageParser()
    parser.feed(path.read_text(encoding="utf-8"))
    parser.close()
    return parser


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("site_root", nargs="?", default=".", help="Root directory containing index.html")
    root = Path(ap.parse_args().site_root).resolve()
    homepage = root / "index.html"
    if not homepage.is_file():
        print(f"ERROR: missing {homepage}")
        return 2

    errors: list[str] = []
    warnings: list[str] = []
    pages = [homepage, *sorted((root / "notes").glob("*.html"))]
    parsers: dict[Path, PageParser] = {}
    for page in pages:
        p = parse(page)
        parsers[page] = p
        rel = page.relative_to(root).as_posix()
        if not p.title_seen:
            errors.append(f"{rel}: missing <title>")
        if not p.description_seen:
            errors.append(f"{rel}: missing non-empty meta description")
        if p.h1_count != 1:
            errors.append(f"{rel}: expected exactly one h1, found {p.h1_count}")
        if p.inline_styles:
            errors.append(f"{rel}: {p.inline_styles} inline style attribute(s); use shared CSS")
        if p.scripts:
            warnings.append(f"{rel}: script source(s) found: {', '.join(p.scripts)}")
        if page != homepage:
            if "../assets/site.css" not in p.styles:
                errors.append(f"{rel}: missing ../assets/site.css stylesheet")
            if not p.time_values:
                errors.append(f"{rel}: missing <time datetime=...>")
            for value in p.time_values:
                if len(value) != 10 or value[4] != "-" or value[7] != "-":
                    errors.append(f"{rel}: date is not YYYY-MM-DD: {value}")
            if 'class="article-lead"' not in page.read_text(encoding="utf-8"):
                errors.append(f"{rel}: missing .article-lead")

    for page, parser in parsers.items():
        for _tag, raw in parser.links:
            parsed = urlparse(raw)
            if parsed.scheme or parsed.netloc or raw.startswith("//"):
                continue
            path_part = unquote(parsed.path)
            target = (page.parent / path_part).resolve() if path_part else page
            try:
                target.relative_to(root)
            except ValueError:
                errors.append(f"{page.relative_to(root)}: local link escapes site root: {raw}")
                continue
            if path_part and not target.is_file() and not target.is_dir():
                errors.append(f"{page.relative_to(root)}: broken local link: {raw}")
            if parsed.fragment and target.is_file() and target.suffix.lower() == ".html":
                target_parser = parsers.get(target)
                if target_parser is None:
                    try:
                        target_parser = parse(target)
                    except (OSError, UnicodeError):
                        target_parser = None
                if target_parser and unquote(parsed.fragment) not in target_parser.ids:
                    errors.append(f"{page.relative_to(root)}: missing fragment #{parsed.fragment} in {target.relative_to(root)}")

    home_links = [raw for tag, raw in parsers[homepage].links if tag == "a" and raw.startswith("notes/")]
    for dup in sorted({u for u in home_links if home_links.count(u) > 1}):
        errors.append(f"index.html: duplicate article entry: {dup}")

    print(f"Checked {len(pages)} HTML page(s) under {root}")
    for warning in warnings:
        print(f"WARN: {warning}")
    for error in errors:
        print(f"ERROR: {error}")
    if errors:
        print(f"FAILED: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1
    print(f"PASSED: no structural or local-link errors ({len(warnings)} warning(s))")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

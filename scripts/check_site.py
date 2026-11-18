#!/usr/bin/env python3
"""Check local internal links and essential structure of the static GitHub Pages site."""
from __future__ import annotations

import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

DOCS = Path(__file__).resolve().parents[1] / "docs"


class PageLinks(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.refs: list[str] = []
        self.h1_count = 0
        self.has_main = False
        self.has_viewport = False
        self.has_description = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "h1":
            self.h1_count += 1
        if tag == "main" and values.get("id") == "main":
            self.has_main = True
        if tag == "meta" and values.get("name") == "viewport":
            self.has_viewport = True
        if tag == "meta" and values.get("name") == "description":
            self.has_description = True
        if tag in ("a", "link", "img", "script"):
            value = values.get("href") or values.get("src")
            if value:
                self.refs.append(value)


def check() -> int:
    errors: list[str] = []
    pages = sorted(DOCS.rglob("*.html"))
    if not pages:
        print("No HTML pages found in docs/", file=sys.stderr)
        return 1

    root = DOCS.resolve()
    for page in pages:
        parser = PageLinks()
        parser.feed(page.read_text(encoding="utf-8"))
        label = str(page.relative_to(DOCS))
        if parser.h1_count != 1:
            errors.append(f"{label}: expected exactly one h1, got {parser.h1_count}")
        if not (parser.has_main and parser.has_viewport and parser.has_description):
            errors.append(f"{label}: missing main, viewport or description")
        for ref in parser.refs:
            parsed = urlsplit(ref)
            if parsed.scheme or parsed.netloc or ref.startswith(("#", "//")):
                continue
            target = (page.parent / unquote(parsed.path)).resolve()
            if target != root and root not in target.parents:
                errors.append(f"{label}: link escapes docs/: {ref}")
            elif not target.exists():
                errors.append(f"{label}: broken link: {ref}")

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"OK: {len(pages)} HTML pages; all local links and basic page structure valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(check())

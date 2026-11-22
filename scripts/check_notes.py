#!/usr/bin/env python3
"""Validate companion Markdown metadata, links, and viewing boundaries (stdlib only)."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTES = ROOT / "notes"
TYPES = {"episode", "observation", "character", "philosopher", "concept", "work", "discussion"}
STATUSES = {"draft", "reviewed", "verified", "published"}
LINE = re.compile(r"^([a-z][a-z0-9_]*):(?:\s*(.*))?$")
ITEM = re.compile(r"^  - ([-a-z0-9]+)$")
LINK = re.compile(r"!?\[[^\]]+\]\(([^)]+)\)")
EP = re.compile(r"^s(\d{2})e(\d{2})$")
EP_MENTION = re.compile(r"\bS(\d{2})E(\d{2})\b", re.I)


def ep_number(value: str) -> int | None:
    m = EP.fullmatch(value)
    return (int(m[1]) * 100 + int(m[2])) if m else None


def front_matter(text: str, path: Path) -> tuple[dict, str]:
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        raise ValueError(f"{path}: missing opening front matter")
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise ValueError(f"{path}: no closing front matter") from exc
    data: dict = {}
    listing: str | None = None
    for line in lines[1:end]:
        if not line.strip():
            continue
        match = LINE.fullmatch(line)
        if match:
            key, value = match.groups()
            if key in data:
                raise ValueError(f"{path}: repeated metadata key {key}")
            if value:
                if value.startswith('"'):
                    try:
                        value = json.loads(value)
                    except json.JSONDecodeError as exc:
                        raise ValueError(f"{path}: invalid quoted value") from exc
                data[key] = value
                listing = None
            else:
                data[key] = []
                listing = key
            continue
        match = ITEM.fullmatch(line)
        if match and listing is not None:
            data[listing].append(match[1])
            continue
        raise ValueError(f"{path}: unsupported YAML line {line!r}")
    return data, "\n".join(lines[end + 1:])


def check() -> int:
    errors: list[str] = []
    ids: dict[str, Path] = {}
    contents: dict[Path, str] = {}
    for path in sorted(NOTES.rglob("*.md")):
        raw = path.read_text(encoding="utf-8")
        contents[path] = raw
        if not raw.startswith("---\n"):
            if path.name not in ("README.md", "INDEX.md"):
                errors.append(f"{path}: missing front matter")
            continue
        try:
            data, body = front_matter(raw, path)
        except ValueError as exc:
            errors.append(str(exc))
            continue
        for key in ("id", "type", "status", "spoiler_limit"):
            if not isinstance(data.get(key), str) or not data[key]:
                errors.append(f"{path}: missing metadata {key}")
        rid = data.get("id", "")
        if rid in ids:
            errors.append(f"{path}: duplicate id {rid} (also {ids[rid]})")
        ids[rid] = path
        if data.get("type") not in TYPES:
            errors.append(f"{path}: unknown type {data.get('type')}")
        if data.get("status") not in STATUSES:
            errors.append(f"{path}: unknown status {data.get('status')}")
        limit = data.get("spoiler_limit", "")
        if limit != "none" and ep_number(str(limit)) is None:
            errors.append(f"{path}: bad spoiler limit {limit}")
        if ep_number(str(limit)) is not None and ep_number(str(limit)) > 109:
            errors.append(f"{path}: exceeds current S01E09 viewing limit")
        kind = data.get("type")
        if kind == "episode":
            if rid != path.stem or ep_number(str(rid)) is None or limit != rid:
                errors.append(f"{path}: filename, id or boundary mismatch")
            match = EP.fullmatch(str(rid))
            if match and (str(data.get("season")) != str(int(match[1])) or str(data.get("episode")) != str(int(match[2]))):
                errors.append(f"{path}: season/episode value mismatch")
            for key, dirname in (("characters", "people/characters"), ("concepts", "concepts")):
                terms = data.get(key)
                if not isinstance(terms, list):
                    errors.append(f"{path}: {key} must be a list")
                    continue
                for term in terms:
                    target = NOTES / dirname / f"{term}.md"
                    if not target.is_file():
                        errors.append(f"{path}: no {key} record for {term}")
                    elif key == "characters":
                        try:
                            target_data, _ = front_matter(target.read_text(encoding="utf-8"), target)
                            first = ep_number(str(target_data.get("first_appearance")))
                            current = ep_number(str(rid))
                            if first is not None and current is not None and first > current:
                                errors.append(f"{path}: character {term} is introduced later")
                        except ValueError as exc:
                            errors.append(str(exc))
            current = ep_number(str(rid))
            if current is not None:
                for m in EP_MENTION.finditer(body):
                    if int(m[1]) * 100 + int(m[2]) > current:
                        errors.append(f"{path}: mentions future episode {m[0]}")
        if kind == "observation" and data.get("episode") != limit:
            errors.append(f"{path}: observation boundary does not match episode")
        if kind == "character" and (data.get("first_appearance") != limit or ep_number(str(limit)) is None):
            errors.append(f"{path}: first appearance and spoiler limit differ")
        if kind == "concept" and EP_MENTION.search(body):
            errors.append(f"{path}: concept pages must be plot-neutral")

    for path, raw in contents.items():
        for match in LINK.finditer(raw):
            target = match[1].strip()
            if target.startswith(("https://", "http://", "mailto:", "#")):
                continue
            filename = target.split("#", 1)[0].split("?", 1)[0]
            if not filename:
                continue
            resolved = (path.parent / filename).resolve()
            if not resolved.is_relative_to(ROOT):
                errors.append(f"{path}: link escapes repository: {target}")
            elif not resolved.is_file():
                errors.append(f"{path}: broken relative link: {target}")
    if errors:
        print(f"Notes validation FAILED: {len(errors)} issue(s)")
        for error in errors:
            print(" -", error)
        return 1
    print(f"Notes validation passed: {len(contents)} Markdown files; {len(ids)} records.")
    return 0


if __name__ == "__main__":
    sys.exit(check())

#!/usr/bin/env python3
"""Check JIT-DW's own Markdown navigation, without imposing checks on adopters.

Editorial smoke test for THIS repository, not a documentation compliance rule
for projects using the Guide. Does not fetch external URLs or claim readability.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AREAS = (
    ROOT / "README.md",
    ROOT / "CONTRIBUTING.md",
    ROOT / "guide",
    ROOT / "docs" / "project-brief.md",
    ROOT / "docs" / "decisions",
    ROOT / "research" / "round-4",
    ROOT / "validation" / "pilots" / "first-private-pilot.md",
)
FENCE = re.compile(r"^[ \t]{0,3}(\x60{3,}|~{3,})(.*)$")
LINK = re.compile(r"(?<!!)\[[^\]]*\]\((<?[^)\n]+>?)\)")


def slug(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"<[^>]*>", "", text)
    text = re.sub(r"[\x60*_~]", "", text)
    text = re.sub(r"[^\w\s-]", "", text.lower(), flags=re.UNICODE)
    return re.sub(r"[\s-]+", "-", text).strip("-")


def headings(markdown: str) -> set[str]:
    result: set[str] = set()
    counts: dict[str, int] = {}
    inside = None
    for line in markdown.splitlines():
        m = FENCE.match(line)
        if m:
            fence = m.group(1)
            if inside is None:
                inside = fence
            elif fence[0] == inside[0] and len(fence) >= len(inside):
                inside = None
            continue
        if inside is not None:
            continue
        h = re.match(r"^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$", line)
        if h:
            key = slug(h.group(1))
            n = counts.get(key, 0)
            counts[key] = n + 1
            result.add(f"{key}-{n}" if n else key)
    return result


def pages() -> list[Path]:
    paths: set[Path] = set()
    for area in AREAS:
        if area.is_file():
            paths.add(area)
        elif area.is_dir():
            paths.update(area.rglob("*.md"))
    return sorted(paths)


def check() -> tuple[list[str], dict[str, int]]:
    issues: list[str] = []
    checked = {"files": 0, "relative_links": 0, "anchors": 0, "fences": 0}
    cache: dict[Path, str] = {}
    for path in pages():
        checked["files"] += 1
        source = path.read_text(encoding="utf-8")
        inside = None
        for line_no, line in enumerate(source.splitlines(), 1):
            f = FENCE.match(line)
            if f:
                token = f.group(1)
                checked["fences"] += 1
                if inside is None:
                    inside = token
                elif token[0] == inside[0] and len(token) >= len(inside):
                    inside = None
                continue
            if inside is not None:
                continue
            for match in LINK.finditer(line):
                target = match.group(1).strip().strip("<>")
                if not target or re.match(r"^(https?://|mailto:|data:)", target):
                    continue
                local, _, anchor = target.partition("#")
                local = local.partition("?")[0]
                dest = (path.parent / local).resolve() if local else path.resolve()
                checked["relative_links"] += 1
                if not dest.is_relative_to(ROOT.resolve()):
                    issues.append(f"{path.relative_to(ROOT)}:{line_no}: path escapes repo: {target}")
                    continue
                if not dest.exists():
                    issues.append(f"{path.relative_to(ROOT)}:{line_no}: missing target: {target}")
                    continue
                if dest.is_dir():
                    if not any((dest / name).exists() for name in ("README.md", "index.md", "INDEX.md")):
                        issues.append(f"{path.relative_to(ROOT)}:{line_no}: directory lacks Markdown entry: {target}")
                    continue
                if anchor and dest.suffix.lower() == ".md":
                    checked["anchors"] += 1
                    text = cache.setdefault(dest, dest.read_text(encoding="utf-8"))
                    if anchor not in headings(text):
                        issues.append(f"{path.relative_to(ROOT)}:{line_no}: missing heading #{anchor} in {dest.relative_to(ROOT)}")
        if inside is not None:
            issues.append(f"{path.relative_to(ROOT)}: unclosed Markdown fence {inside}")
    return issues, checked


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args(argv)
    problems, stats = check()
    print(f"JIT-DW editorial navigation smoke test: {stats}")
    for problem in problems:
        print(f"ERROR: {problem}", file=sys.stderr)
    print("No broken local paths/anchors or unclosed fences." if not problems else f"{len(problems)} issue(s) found")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())

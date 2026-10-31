#!/usr/bin/env python3
"""Project-specific documentation-impact prompts. Advisory only, not a semantic validator."""
from __future__ import annotations

import argparse
import fnmatch
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
PROFILES = ROOT / "validation" / "pilots" / "codex-astrbot" / "profiles.json"


def analyze(profile: str, changed_files: list[str], profiles: dict[str, Any]) -> dict[str, Any]:
    """Produce path-based questions; never assert that documentation is complete."""
    if profile not in profiles:
        raise ValueError(f"Unknown profile {profile!r}; expected {', '.join(sorted(profiles))}")
    if not isinstance(changed_files, list) or any(not isinstance(p, str) for p in changed_files):
        raise ValueError("changed_files must be an array of path strings")
    files = list(dict.fromkeys(p.replace("\\", "/") for p in changed_files if p))
    matched = set()
    suggestions = []
    for rule in profiles[profile]["rules"]:
        paths = [p for p in files if any(fnmatch.fnmatchcase(p, pattern) for pattern in rule["patterns"])]
        if not paths:
            continue
        matched.update(paths)
        suggestions.append({
            "id": rule["id"],
            "question": rule["question"],
            "review_surfaces": rule["review_surfaces"],
            "matched_files": paths,
            "basis": rule["basis"],
        })
    return {
        "profile": profile,
        "mode": "advisory-only",
        "disclaimer": "Path-based hints are not evidence that documentation is missing or complete.",
        "changed_file_count": len(files),
        "suggestions": suggestions,
        "unmapped_files": [p for p in files if p not in matched],
        "decision": "human-review-required",
    }


def to_markdown(result: dict[str, Any]) -> str:
    out = [
        f"# JIT-DW review prompts — {result['profile']}",
        "",
        f"**Mode:** advisory only. **Changed paths:** {result['changed_file_count']}.",
        "**No automatic decision about whether documentation is required.**",
        f"**Input scope:** {result.get('file_list_scope', 'unspecified')}. "
        f"**Source PR:** {result.get('source_pr', 'not supplied')}.",
        "",
    ]
    if not result["suggestions"]:
        out.extend(["No profile rule matched. This is UNKNOWN, not evidence that no docs are needed.", ""])
    for suggestion in result["suggestions"]:
        out.extend([
            f"## {suggestion['id']}",
            "",
            suggestion["question"],
            "",
            "**Affected paths:** " + ", ".join(suggestion["matched_files"]),
            "",
            "**Potential representations:** " + "; ".join(suggestion["review_surfaces"]),
            "",
            "**Basis:** " + suggestion["basis"],
            "",
        ])
    if result["unmapped_files"]:
        out.extend(["## Unmapped paths", "", "No rule matched; ordinary repository review is still needed:", ""])
        out.extend("- " + path for path in result["unmapped_files"])
        out.append("")
    out.extend([
        "## Required human disposition",
        "",
        "For each materially changed fact, record Updated / No update required / Deferred / Unknown, "
        "with evidence and a reviewer.",
        "Do not turn this output into a blocking check before a pilot measures false positives and misses.",
    ])
    return "\n".join(out) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", required=True)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--profiles", type=Path, default=PROFILES)
    parser.add_argument("--format", choices=["json", "markdown"], default="markdown")
    args = parser.parse_args(argv)
    try:
        profiles = json.loads(args.profiles.read_text(encoding="utf-8"))
        data = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise ValueError("Input must be a JSON object")
        result = analyze(args.profile, data.get("changed_files"), profiles)
        result["file_list_scope"] = data.get("file_list_scope", "unspecified")
        result["source_pr"] = f"{data.get('upstream', 'unspecified')}#{data.get('pr', '?')}"
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2) if args.format == "json" else to_markdown(result), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

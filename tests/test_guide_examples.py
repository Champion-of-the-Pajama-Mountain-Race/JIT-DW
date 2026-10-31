"""Execute exactly the examples the Guide promises are runnable.

This validates code snippets, not whether prose is useful to a real reader.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def blocks(filename: str, language: str) -> list[str]:
    text = (ROOT / filename).read_text(encoding="utf-8")
    regex = r"^~~~" + re.escape(language) + r"\n(.*?)^~~~\s*$"
    return re.findall(regex, text, flags=re.MULTILINE | re.DOTALL)


class GuideExampleTests(unittest.TestCase):
    def test_first_success_example_runs_to_exact_output(self):
        sh = blocks("guide/recipes/first-success.md", "sh")
        py = blocks("guide/recipes/first-success.md", "python")
        expected = blocks("guide/recipes/first-success.md", "json")
        self.assertGreaterEqual(len(sh), 2)
        self.assertEqual(len(py), 1)
        self.assertEqual(len(expected), 1)
        with tempfile.TemporaryDirectory() as d:
            path = Path(d)
            (path / "convert.py").write_text(py[0], encoding="utf-8")
            first = subprocess.run(["bash", "-e", "-c", sh[0]], cwd=path, capture_output=True, text=True)
            self.assertEqual(first.returncode, 0, first.stderr)
            second = subprocess.run(["bash", "-e", "-c", sh[1]], cwd=path, capture_output=True, text=True)
            self.assertEqual(second.returncode, 0, second.stderr)
            actual = json.loads((path / "people.json").read_text(encoding="utf-8"))
            self.assertEqual(actual, json.loads(expected[0]))
            self.assertIn("Ada", second.stdout)
            missing = subprocess.run(
                [sys.executable, "convert.py", "no-such-file.csv", "output.json"],
                cwd=path, capture_output=True, text=True,
            )
            self.assertNotEqual(missing.returncode, 0)
            self.assertIn("FileNotFoundError", missing.stderr)

    def test_json_config_contract_example_matches_errors(self):
        code = next(
            b for b in blocks("guide/recipes/source-comment.md", "python")
            if "def read_config(" in b
        )
        namespace = {"__name__": "__jitdw_guide_example__"}
        exec(compile(code, "guide/recipes/source-comment.md", "exec"), namespace)
        read_config = namespace["read_config"]
        with tempfile.TemporaryDirectory() as d:
            path = Path(d)
            good = path / "good.json"
            good.write_text('{"enabled": true}', encoding="utf-8")
            self.assertEqual(read_config(str(good)), {"enabled": True})
            with self.assertRaises(FileNotFoundError):
                read_config(str(path / "missing.json"))
            bad = path / "bad.json"
            bad.write_text('{"enabled":', encoding="utf-8")
            with self.assertRaises(ValueError):
                read_config(str(bad))
            list_root = path / "list.json"
            list_root.write_text("[]", encoding="utf-8")
            with self.assertRaises(ValueError):
                read_config(str(list_root))


if __name__ == "__main__":
    unittest.main()

import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("jitdw_advisor", ROOT / "tools/jitdw_advisor.py")
advisor = importlib.util.module_from_spec(spec)
spec.loader.exec_module(advisor)
PROFILES = json.loads(advisor.PROFILES.read_text(encoding="utf-8"))
FIXTURES = ROOT / "validation/pilots/codex-astrbot/fixtures"


class AdvisorTests(unittest.TestCase):
    def run_case(self, name, profile):
        fixture = json.loads((FIXTURES / name).read_text(encoding="utf-8"))
        return advisor.analyze(profile, fixture["changed_files"], PROFILES)

    def test_codex_linux_sandbox(self):
        r = self.run_case("codex-linux-sandbox-pr52610.json", "codex")
        self.assertIn("linux-sandbox-boundary", [x["id"] for x in r["suggestions"]])

    def test_codex_protocol(self):
        r = self.run_case("codex-protocol-pr57172.json", "codex")
        self.assertIn("app-server-contract", [x["id"] for x in r["suggestions"]])

    def test_codex_auth_copy_without_manual_docs_requirement(self):
        r = self.run_case("codex-auth-pr49361.json", "codex")
        self.assertIn("auth-persistence-copy", [x["id"] for x in r["suggestions"]])
        self.assertEqual(r["decision"], "human-review-required")

    def test_codex_policy_change(self):
        r = self.run_case("codex-doc-policy-pr43423.json", "codex")
        self.assertIn("governance-guidance", [x["id"] for x in r["suggestions"]])

    def test_astrbot_provider(self):
        r = self.run_case("astrbot-decision-provider-pr10775.json", "astrbot")
        ids = {x["id"] for x in r["suggestions"]}
        self.assertTrue({"plugin-provider-contract", "dashboard-config-api", "webui-navigation-localization", "translated-public-docs"} <= ids)

    def test_astrbot_reload(self):
        r = self.run_case("astrbot-reload-pr10788.json", "astrbot")
        self.assertIn("dashboard-config-api", [x["id"] for x in r["suggestions"]])

    def test_astrbot_tls(self):
        r = self.run_case("astrbot-tls-pr10685.json", "astrbot")
        self.assertIn("dependency-install-security", [x["id"] for x in r["suggestions"]])

    def test_astrbot_docs_only(self):
        r = self.run_case("astrbot-docs-pr10879.json", "astrbot")
        ids = {x["id"] for x in r["suggestions"]}
        self.assertIn("translated-public-docs", ids)
        self.assertNotIn("plugin-provider-contract", ids)

    def test_unmapped_not_a_no_docs_result(self):
        r = advisor.analyze("codex", ["codex-rs/unknown/src/internal.rs"], PROFILES)
        self.assertEqual(r["suggestions"], [])
        self.assertEqual(r["decision"], "human-review-required")
        self.assertEqual(r["unmapped_files"], ["codex-rs/unknown/src/internal.rs"])

    def test_duplicates_not_counted(self):
        r = advisor.analyze("codex", ["AGENTS.md", "AGENTS.md"], PROFILES)
        self.assertEqual(r["changed_file_count"], 1)

    def test_windows_separators(self):
        r = advisor.analyze("astrbot", [r"astrbot\core\provider\decision.py"], PROFILES)
        self.assertIn("plugin-provider-contract", [x["id"] for x in r["suggestions"]])

    def test_malformed_input(self):
        with self.assertRaises(ValueError):
            advisor.analyze("astrbot", [None], PROFILES)

    def test_invalid_profile(self):
        with self.assertRaises(ValueError):
            advisor.analyze("not-a-profile", [], PROFILES)

    def test_machine_consumed_docstring_rule(self):
        r = advisor.analyze("astrbot", ["astrbot/core/star/register/star_handler.py"], PROFILES)
        ids = [x["id"] for x in r["suggestions"]]
        self.assertIn("llm-tool-docstring-runtime-contract", ids)
        self.assertEqual(r["decision"], "human-review-required")

    def test_machine_consumed_docs_are_not_silently_passed(self):
        r = advisor.analyze("astrbot", ["docs/en/dev/star/guides/ai.md"], PROFILES)
        ids = [x["id"] for x in r["suggestions"]]
        self.assertIn("llm-tool-docstring-runtime-contract", ids)
        self.assertNotEqual(r["decision"], "no-update-required")

    def test_codex_argument_comment_lint_mapping(self):
        r = advisor.analyze("codex", ["tools/argument-comment-lint/README.md"], PROFILES)
        self.assertIn("argument-comment-contract", [x["id"] for x in r["suggestions"]])

    def test_generator_closure_prompt(self):
        r = advisor.analyze("codex", ["codex-rs/app-server-protocol/src/schema_fixtures_tests.rs"], PROFILES)
        surface = [x for x in r["suggestions"] if x["id"] == "app-server-contract"][0]
        self.assertIn("generated file-set and content equality checks", surface["review_surfaces"])

    def test_advisory_disclaimer(self):
        output = advisor.to_markdown(advisor.analyze("codex", ["AGENTS.md"], PROFILES))
        self.assertIn("No automatic decision", output)


if __name__ == "__main__":
    unittest.main()

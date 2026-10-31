# Contributing to JIT-DW

Thank you for improving the Guide. **You do not have to adopt JIT-DW tooling, add a new Markdown file, or follow an approval checklist to contribute.**

JIT-DW is [Guide first](docs/decisions/0001-guide-first.md): help developers and coding agents make useful documentation choices, not inspect them for compliance.

## An easy contribution

Read [the Guide](guide/README.md), or the [中文十分钟指南](guide/quickstart.zh-CN.md), and notice something that does not help a reader. Improve the smallest appropriate place. Changes that remove clutter, clarify an example, or explain when **not** to use a method are welcome.

For a substantial recommendation, aim to include:
- the actual reader problem and context;
- a practical alternative (sometimes no document is required);
- a short, accurate example, preferably runnable when it claims to be;
- source-backed reasoning if you say a real project uses a particular practice;
- any downside or case where the advice should **not** be copied.

Real case studies and research belong in [research](research/README.md); their job is to support the Guide, not to demand formal proof for every typo fix.

## A few useful boundaries

- Do not move private source code, private PR content, internal execution logs, or trial participant answers into this public repository without authorization. Private pilot materials must stay with the private project.
- Do not turn JIT-DW into a mandatory documentation gate or a document-per-module policy.
- Do not silently assert that a passing code snippet test proves the text is semantically complete.
- Distinguish current implementation information from old design decisions.
- If the project does not yet have a license, do not assume that examples from another repository can be copied wholesale; prefer original examples and links to primary source.

## Checking a Guide change

For edits to examples or navigation you **may** run:

~~~sh
python3 tools/check_guide.py
python3 -m unittest discover -s tests -p 'test_guide_examples.py' -v
~~~

These checks run in this repository's own hosted CI. They only check local links/fences and the two runnable Python teaching examples; they do not certify writing quality or add requirements to downstream projects.

If your contribution is a small prose correction, an ordinary review is enough. The coding author and project maintainers retain judgment.

[Guide](guide/README.md) · [Why Guide-first](docs/decisions/0001-guide-first.md)

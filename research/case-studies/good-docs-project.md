# Case study: The Good Docs Project

**Status:** Evidence-complete for template-system design; not a study of software implementation documentation.  
**Repository:** https://github.com/thegooddocsproject/templates  
**Revision:** de840b374c57502bf1e99c3ccfe05a858553f99f  
**Scope:** Template taxonomy, template deliverables, API reference example, and template review roles.

## 1. Question

What makes a reusable documentation template usable rather than merely a blank outline?

## 2. Repository context

The Good Docs Project maintains reusable technical-writing templates. Its repository is a template system and a community process for producing templates. It is relevant to the design of JIT-DW's workflow kit, but it should not be treated as evidence about how a large software codebase maintains source comments or API documentation.

## 3. Evidence inventory

| Evidence | Type | Source | What it establishes |
|---|---|---|---|
| E1 | P/D | [Templates README](https://github.com/thegooddocsproject/templates/blob/de840b374c57502bf1e99c3ccfe05a858553f99f/README.md#L8-L75) | Templates are grouped by reader task: concept, task, and reference; the README describes how to combine them into a documentation set. |
| E2 | D | [API reference template](https://github.com/thegooddocsproject/templates/blob/de840b374c57502bf1e99c3ccfe05a858553f99f/api-reference/api-reference.md#L1-L40) | A reference template asks for endpoint syntax, description, parameters, request examples, and response examples. |
| E3 | P | [Template deliverables](https://github.com/thegooddocsproject/templates/blob/de840b374c57502bf1e99c3ccfe05a858553f99f/template-deliverables.md#L16-L60) | A template set includes a raw template and a companion guide; deep dives and examples are optional. |
| E4 | P | [Template roles and resources](https://github.com/thegooddocsproject/templates/blob/de840b374c57502bf1e99c3ccfe05a858553f99f/template-roles-and-resources.md#L35-L60) | Template creation has defined coordination, mentorship, and community review roles. |

## 4. What the repository actually does

The README groups documentation by the reader's activity:

- Concept: learn what something is and why it works.
- Task: complete a specific goal by following steps.
- Reference: look up structured facts or specifications.

The API reference template is not just a list of headings. It prompts the author for endpoint syntax, a concise description, parameter names/types/requiredness, a working request, a real response, and explanatory comments where useful.

The template-deliverables guide requires two components:

1. A raw template with a suggested structure and embedded writing tips.
2. A companion guide explaining the purpose of the document type and how to fill in each section.

A deeper guide and a worked example are optional. The same document explicitly warns that different document types have different content needs and should not be forced into one universal structure.

The project also defines roles for template development. Its process includes a coordinator, mentors, community reviewers, and pull-request reviewers; the coordinator is responsible for ensuring a template receives at least three community reviews during the feedback phase.

## 5. Why these practices may exist

**Stated rationale:** Templates are intended to help contributors produce useful documents without needing to invent the structure and writing guidance from scratch. The companion guide carries information that would make the raw template too long or difficult to use.

**Inferred rationale:** Separating the blank artifact from its instructional guide makes the template easier to copy while preserving deeper rationale and advice for authors.

**Unknown:** The repository does not provide controlled evidence that every template improves reader task completion or that the review process always produces consistent quality.

## 6. Comparison with JIT-DW hypotheses

| Hypothesis | Alignment | Evidence and qualification |
|---|---|---|
| Templates need usage instructions, not just headings | supports | The raw template and guide are separate required deliverables. |
| Different document types need different structures | supports | Concept, task, and reference templates have distinct purposes. |
| A single universal module template is sufficient | contradicts | The project explicitly warns against forcing different document types into one structure. |
| Examples are always mandatory | contradicts | Worked examples and deep dives are optional deliverables. |
| Documentation work needs roles and review | supports | The template creation process defines coordination and community review responsibilities. |
| These templates define code-to-doc maintenance | not observed | The repository is about authoring templates, not source-code change impact. |

## 7. Trade-offs and limitations

- A template set has a maintenance cost of its own: template file, guide, examples, and review process may all need updates.
- A template can become too prescriptive if it includes every possible section.
- This project's three broad categories are useful, but they do not exactly match every other taxonomy. JIT-DW should map reader needs rather than enforce labels.

## 8. Findings

- **Observed practice:** Reusable templates are paired with companion guides and a defined authoring/review process.
- **Stated rationale:** Templates should make the writing task easier while retaining enough explanation to use them correctly.
- **Inferred rationale:** Separating the template from its guide reduces clutter in copied documents.
- **Confidence:** High for repository structure and stated process; medium for inferred benefits.
- **What JIT-DW should adopt:** Every substantial template should include purpose, intended reader, when to use it, when not to use it, instructions for each section, and a minimal example where useful.
- **What JIT-DW should not copy:** A mandatory multi-role review structure for every project using the kit.
- **What needs pilot validation:** Whether the companion guide is enough for first-time contributors to complete a useful document.

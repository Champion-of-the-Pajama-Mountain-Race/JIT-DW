# Recipes — optional starting points

These are not required files or compliance templates. Each recipe explains **the reader problem, a minimal example, and when not to use it**. Copy only what helps. Rename, combine, simplify, or delete the sections your project doesn't need.

| Reader problem | Recipe | When to skip it |
|---|---|---|
| People cannot orient themselves inside a subsystem | [Small module README](module-readme.md) | A descriptive path and existing project README already make the boundary obvious |
| An interface's behavior or invariant is unclear | [Source comments and contract examples](source-comment.md) | Better types/names or tests communicate everything important |
| New users repeatedly get stuck before first success | [First successful task](first-success.md) | The existing entry point and CLI help already make that task obvious |
| A change might invalidate a reader-facing explanation | [Write a minimal change note](change-note.md) | The team can resolve it naturally in code review without extra paperwork |

Each example is illustrative unless specifically attributed to a real project. Real-world source-backed explanations are in [case lessons](../06-case-lessons.md). A recipe that encourages filler or duplicate maintenance should be shortened, not completed ritualistically.

[Back to Guide](../README.md).

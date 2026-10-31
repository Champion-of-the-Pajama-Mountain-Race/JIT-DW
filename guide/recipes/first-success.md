# Recipe: guide a newcomer to their first successful task

**Use when:** people can find the repository but cannot reliably reach an observable first result.

**Don't use when:** an existing clear README, command help, or short example already completes that journey. Avoid introducing a docs site just to host one page.

## A small illustrative quickstart

~~~markdown
# First successful conversion

This utility converts a local CSV file to JSON.

## Before you begin

- Python 3.12 or newer
- A local checkout of this project

## Try it

1. Install the project using the instructions in the repository README.
2. Run the project's converter on examples/people.csv.
3. Open the generated result and check that it contains a JSON array.

Expected: each input row becomes one object, keyed by the CSV header.

## If it fails

- Check that the input file exists.
- Confirm you are running the documented version of the converter.
- See docs/reference/cli.md for flags and exit codes.

## Next

To customize output, read docs/how-to/configure-output.md.
~~~

The project, behavior, command, and paths above are **fictional placeholders**, not executable instructions for a real tool. Replace them with exact, tested commands and outputs before publishing. A real quickstart should not say merely “run the converter” without showing the actual command; this example deliberately highlights the structure, not a ready-to-run command.

## Improve the draft before shipping

- Put the real command where step 2 is; avoid guesses about installation.
- Add one representative input and the exact expected output.
- Test the steps in a clean environment or ask a newcomer to do so.
- State supported platform/version limitations.
- Link to a detailed reference instead of embedding every option.

Django's [writing documentation guide](https://github.com/django/django/blob/f4c65fd6a517dd32bd2e732ae3543e550e56f206/docs/internals/contributing/writing-documentation.txt) emphasizes getting the learner to do something useful early. Rust's [rustdoc guide](https://github.com/rust-lang/rust/blob/92b5b8c87c61b20adc9001b41baf587634a74734/src/doc/rustdoc/src/how-to-write-documentation.md) similarly recommends a front-page summary and concrete example.

[Back to recipes](README.md).

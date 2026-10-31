# Recipe: guide a newcomer to their first successful task

**Use when:** people can find the project but cannot reliably reach an observable first result.

**Don't use when:** the README, CLI help or a tested snippet already gets them there. Avoid adding a docs site for one simple first-use path.

## A complete, runnable toy example

The following is an **original teaching example**, not an existing product's quickstart. It shows what it means to give exact setup, execution, expected output, and a failure path. It uses only Python's standard library and a POSIX-style shell.

### 1. Prepare an input file

~~~sh
printf 'name,score\nAda,9\nLin,8\n' > people.csv
~~~

### 2. Create a small converter

~~~python
# save as convert.py
import csv
import json
import sys
from pathlib import Path

source = Path(sys.argv[1])
destination = Path(sys.argv[2])
with source.open(newline="", encoding="utf-8") as stream:
    records = list(csv.DictReader(stream))
destination.write_text(json.dumps(records, indent=2) + "\n", encoding="utf-8")
~~~

### 3. Run and inspect the result

~~~sh
python3 convert.py people.csv people.json
cat people.json
~~~

Expected output:

~~~json
[
  {
    "name": "Ada",
    "score": "9"
  },
  {
    "name": "Lin",
    "score": "8"
  }
]
~~~

The values are strings because a CSV reader does not infer integer types; that is a meaningful limitation the reader should know. If the input path is wrong, Python raises a file-not-found error. A real product's guide should describe its own supported failures and recovery paths.

## Transfer this pattern to your project

Replace the toy code with **the project's actual install command, exact invocation, test input, and expected result**. If shell instructions differ across platforms, say which platform you tested. If a command needs credentials, specify a safe test setup without publishing secrets.

A practical first-use document should answer:
- What will I achieve?
- What do I need beforehand?
- What exact action do I take?
- What tells me it worked?
- Where do I go if it fails or want more?

Django's [writing guide](https://github.com/django/django/blob/f4c65fd6a517dd32bd2e732ae3543e550e56f206/docs/internals/contributing/writing-documentation.txt) stresses getting a learner to a useful action early. Rust's [rustdoc guide](https://github.com/rust-lang/rust/blob/92b5b8c87c61b20adc9001b41baf587634a74734/src/doc/rustdoc/src/how-to-write-documentation.md) recommends a front-page purpose and real example.

**A good quickstart is not necessarily long.** If a working command and one expected line of output are enough, stop there.

[Back to recipes](README.md).

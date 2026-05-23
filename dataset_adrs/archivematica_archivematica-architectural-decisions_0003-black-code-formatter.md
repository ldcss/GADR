---
layout: page
status: accepted
adr: "0003"
title: Black code formatter
deciders:
date:
---

## Context and problem statement

Archivematica code style is inconsistent and controversial. Formatting is a
distraction from content and a constant dilemma in our code review process.

The style guide described by [PEP 8][0] is not specific enough and Python is too
flexible. Every project ends up with its own style and memorizing the rules is
hard.

With the recent rise of auto formatters such *gofmt* or *Prettier*, we see the
value of ceding control to an opinionated tool.

## Considered options

* [yapf][1] - configurable formatter written by Google.
* [autopep8][2] - relies on [pycodestyle][3] to determine what parts of the code
  needs to be formatted.
* [black][4] - it focuses on making formatting totally transparent to the
  developer.

## Decision outcome

Chosen option: "black", because:

* It prioritizes consistency over style.
* It can check that the reformatted code still produces a valid AST that is
  equivalent to the original.
* Zero configuration, sane defaults.
* Adopted by popular projects such [responder][5] or [pytest][6].

## Links

* [Issue 393][7].

[0]: https://www.python.org/dev/peps/pep-0008/
[1]: https://github.com/google/yapf
[2]: https://github.com/hhatto/autopep8
[3]: https://github.com/PyCQA/pycodestyle
[4]: https://github.com/ambv/black
[5]: https://github.com/kennethreitz/responder
[6]: https://github.com/pytest-dev/pytest
[7]: https://github.com/archivematica/Issues/issues/393

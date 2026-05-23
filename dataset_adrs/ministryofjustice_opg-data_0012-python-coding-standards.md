# 12. Python Best Practices

Date: 2020-02-11

## Status

Proposed

## Context

> Readbility counts -- [The Zen of Python](https://www.python.org/dev/peps/pep-0020/)

## Decision

### Code Formatting

* Follow [PEP-8](https://www.python.org/dev/peps/pep-0008/)
* Use pre-commit hooks to enforce these standards where possible

### Types

* Type checking is a bit overkill for small single functions, so we will not enforce this.

### General Style Guide

* Make your comments verbose, not your code, eg:
  * Use list comprehensions and map() where it is sensible to instead of a loop
  * Use ternary operator
* Only use f-strings for string interpolation
* Catch  named errors, don't just use generic `except` blocks
* Be sensible with log levels, debug is useful but we don't need to know *everything*

### Documentation

* Follow [PEP-257](https://www.python.org/dev/peps/pep-0257/) for docstring formatting using [reStructured Text](https://www.writethedocs.org/guide/writing/reStructuredText/)
* Generate documentation with Sphinx

### AWS Lambda Specific Guidelines

* See [Amazon guidelines](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html)

### Standard Tools

* Code Formatting: [Black](https://black.readthedocs.io/en/stable/)
* Linting/Complexity/Error Detection: [Flake8](https://flake8.pycqa.org/en/latest/)
* Type Checking: [MyPy](http://mypy-lang.org/)
* Unit Tests: [PyTest](https://docs.pytest.org/en/latest/)
* Package Management: [Pip](https://pypi.org/project/pip/)
* Emojis: [Emoji](https://pypi.org/project/emoji/)
* Dates: TBD

## Consequences

* Reduced code complexity
* Code that is easy to test
* Code that is consistent and therefore easy maintain by any developer

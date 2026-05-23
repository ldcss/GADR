# 3. Use Type Hinting

Date: 2020-06-05

## Status

Accepted

## Context

Python 3 added support for static type checking (see: https://docs.python.org/3/library/typing.html). Type hinting is not an all or nothing thing, and can be applied in a progressive manner. It's also worth noting that type checks are not applied at runtime.

## Decision

We will use type hinting. Our focus should be on type hints for function arguments and return values, and not aim for full coverage.

## Consequences

Type hinting is new for all of us so we should expect a learning curve and some added effort as we start working with it. There's no requirement that we type hint everything though, so we can easily skip the more complicated problems and come back to them as time allows.

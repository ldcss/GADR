# 2. Avoid runtime dependencies

Date: 2017-06-06

## Status

Accepted

## Context

We don't want to create an SDK that requires customers to add a slew of
external dependencies.

## Decision

We will avoid external runtime dependencies. For instance, we will use the core
Apple networking libraries (e.g. URLSession) instead of introducing a
dependency on something like [Alamofire][1].

External development dependencies (those necessary for contributing, but which
are not bundled with the SDK) will be added as necessary.

## Consequences

There will be some more boilerplate code that we have to write (e.g. for JSON
serialization/deserialization), but we feel the trade-off is worthwhile.

[1]: https://github.com/Alamofire/Alamofire

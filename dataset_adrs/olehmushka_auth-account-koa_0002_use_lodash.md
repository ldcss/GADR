
# Use lodash library for JS

## Context

There is the problem where to store different utilities and write every time the same code on all projects.

## Decision

Use [lodash](https://lodash.com/docs/) possibilities as main package for utilities on the JS microservices, in order to spend less time and write less code. And use utils directory as a wrapper for it in order to be able to replace it any time.

## Status

Accepted

## Consequences

[lodash](https://lodash.com/docs/) is a powerful library written in JS, without any dependencies and this library.

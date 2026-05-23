# 12. remove custom json serialization

Date: 2022-01-18

## Status

Accepted

Supercedes [6. Use custom JSON serialization](0007-use-custom-json-serialization.md)

## Context

Turns out, custom functionality on top of JSON serialization wasn't the greatest.

- 🧱 this added some weight to the FE bundle. Not a ton, but shaving every byte counts for something!
- 🤯 complexity. Right now the goal is decreasing the complexity and number of "custom" stuff in the stack powering my blog.

## Decision

Remove `superjson` and use transform `Date` objects into strings

## Consequences

- Transformation has to happen manually. This involves some setup but fortunately it can be centralized.
- Testing will need to be done on posts to make sure they won't cause crashes. Fortunately right now this can happen at runtime.

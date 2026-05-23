# 3. Test Distributed Files Only

Date: 2021-02-08

## Status

Accepted

Relates [2. Use Google Closure Compiler](0002-use-google-closure-compiler.md)

## Context

It is not uncommon to have successful tests against development sources failing against the production bundle. We must make sure that code distributed to the public works as intended and avoid false positive in testing. The advanced compilation mode of the Google Closure Compiler makes this class of errors more likely to happen as it transforms the development sources radically.

## Decision

Testing will be made against the production bundle to catch compilation errors before they reach our users.

## Consequences

- Longer testing feedback loop as sources must be recompiled before each test run.
- Stronger focus on testing the public interface as internal functions and helpers are out of reach.
# 14. Allow react native

Date: 2022-03-20

## Status

Accepted

## Context

The issue motivating this decision, and any context that influences or constrains the decision.

## Notes

### React can only be default-imported using the 'esModuleInterop' flag

Seems like there are some type conflicts so we have give the `react-native` adapter its own `package.config` and `tsconfig.json`.

Same as we had to do for `web-worker`.

Related to [this](https://github.com/Microsoft/TypeScript/issues/14687#issuecomment-287093051).

## Consequences

What becomes easier or more difficult to do and any risks introduced by the change that will need to be mitigated.

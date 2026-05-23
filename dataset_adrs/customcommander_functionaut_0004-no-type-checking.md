# 4. No Type Checking

Date: 2021-10-12

## Status

Accepted

## Context

Making sure that a function operates with the right input and providing the user with a good debugging experience is not trivial.

Consider this contrived example:

```javascript
function inc(x) {
  if (typeof x != 'number') throw new Error('x is not a number');
  return x + 1;
}

function inc_array(xs) {
  if (!Array.isArray(xs)) throw new Error('xs is not an array');
  return xs.map(x => inc(x)); // <- May or may not throw
}
```

We cannot guarantee that `inc_array` won't throw even if `xs` is an array. If we wanted to give early feedback, we would need to go through each `x` and do the same type checking that `inc` already does. So if the function is invoked correctly we would type check `xs` once and each `x` twice!

## Decision

This project will adopt a *"Garbage In — Garbage Out"* philosophy and deliver a *"no hand-holding"* library.

## Consequences

- Good documentation and examples are not optional.
- Correct usage is not penalised.
- Less effort required to contribute.
- Debugging may be more challenging.

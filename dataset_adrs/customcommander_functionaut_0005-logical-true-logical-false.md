# 5. Logical True, Logical False

Date: 2022-01-01

## Status

Accepted

## Context

Truthy and falsy checks are well-known and established practices however they make it very easy to unintentionally discard valid values.

In this example `speed` can never be set to `0` which may or may not cause bugs:

``` javascript
const speed = n || 50;
```

## Decision

We will adopt the concept of logical truth and logical falsity as [defined in Clojure](https://clojure.org/reference/special_forms#if):

> […]All of the other conditionals in Clojure are based upon the same logic, that is, nil and false constitute logical falsity, and everything else constitutes logical truth, and those meanings apply throughout.[…]

Logical falsity will be defined as either `false`, `null` or `undefined`. Everything else, including `0`, `''` and `NaN`, will constitute logical truth.

## Consequences

This may or may not cause friction when adopting the library. JavaScript developers are used to truthy and falsy values so the concept of logical truth and logical falsity will probably feel odd at first.

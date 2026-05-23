# 10. Use an open source permutation library (js-combinatorics)

Date: 2019-05-30

## Status

Accepted

## Context

In order to check each of the possible hands a person can make with the
available cards, we'll need to generate those hands. This is a common problem
with established open source implementations, there is no need to re-implement
it. 

The npm package `js-combinatorics` is very popular (almost 20k weekly
downloads), has no external dependencies, and has an api to do exactly what I'll
need:

> Combinatorics.permutation(ary, nelem)  
> Creates a generator which generates the permutation of ary with nelem  
> elements. When nelem is ommited, ary.length is used.

Also, since the instructions ask for "production" level code, it's worth noting
that js-combinatorics is licensed with the MIT license. 

## Decision

Use [js-combinatorics](https://github.com/dankogai/js-combinatorics) instead of
writing something bespoke to generate permutations.

## Consequences

No need to test, write, or debug the permutation code.


# ADR 0013: Use IORef for state

Date: 2018-12-01

## Status

Accepted

## Context

In [adr-0012](/docs/architecture/decisions/adr-0012-use-concrete-state-monad.md) we decided to use `StateT` to manage state. This solved the problem of not being able to use `zoom` but it introduced a new problem.

_Massive space leaks_

The performance of the program was abysmal, using strict `State` didn't make a difference. Clearly we need another approach.

Inspired by [The ReaderT design pattern](https://www.fpcomplete.com/blog/2017/06/readert-design-pattern) and [Lensed Reader](https://michaelxavier.net/posts/2016-04-03-Enterprise-Haskell-Pattern-Lensed-Reader.html) it seems like a viable approach would be to put _everything_ in a `ReaderT` and use `IORef`'s to handle mutable state.

Having now tested this approach we can see the performance of the program is dramatically improved. This elimates `StateT` from _most_ of our program.

## Decision

We're using `IORef` for state.

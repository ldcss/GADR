# ADR 0007: mtl style for effects

Date: 2018-09-30

## Status

Superseded by [adr-0012](/docs/architecture/adr-0012-use-concrete-state-monad.md)

## Context

In Haskell we need a way to manage side-effects, particularly for games. There are a _bunch_ of
options including:

- MTL Style
- Using `IO` for everything
- Freer Monads

I haven't used mtl style in anger yet yet so I'm keen to give it a go.

I'm also steaing a lot of ideas from [dino-rush](https://github.com/jxv/dino-rush/) and it
seems to be using MTL style.

## Decision

We're using MTL style.

## Consequences

- We're going to have to write a lot of class instances

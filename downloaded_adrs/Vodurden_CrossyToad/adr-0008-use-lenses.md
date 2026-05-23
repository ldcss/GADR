# ADR 0008: use lenses

Date: 2018-10-25

## Status

Accepted

## Context

Because we're writing a game we have lots of nested state that we need to update, traverse and
otherwise manipulate. Querying data is relatively straightforward in vanilla haskell but
updating nested records is a pain.

This is the problem [lens](https://github.com/ekmett/lens) is supposed to help us with.

Additionally by using lenses we have the option to use the "classy" lenses style to let
individual subsystems of our game target a subset of our State monad instead of requiring the
full state.

## Decision

It's Lens time!

## Consequences

- We're going to need to figure out a way of organising our classes, lens definitions and methods
  such that we can deal with overlapping names

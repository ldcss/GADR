# ADR 0005: Use Hpack

Date: 2018-09-30

## Status

Accepted

## Context

Cabal files are annoying to specify, they tend to have a fair bit of redundancy and I found
them annoying to use in the past.

Pain points include:

- Having to specify `ghc-options` for each target
- Having to specify common dependencies for each target
- Having to manually specify _every exposed module_

[hpack](https://github.com/sol/hpack) solves these problems, so let's use it!

## Decision

We're using [hpack](https://github.com/sol/hpack)!

## Consequences

- Since I'm not using stack, I'll have to run `hpack` manually when I change the file

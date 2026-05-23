# ADR 0003: Nix for dependency management

Date: 2018-09-30

## Status

Accepted

## Context

As per [ADR-0002](adr-0002-use-haskell.md) we're using Haskell. But we need a way to manage
Haskell dependencies.

At the time of writing I'm only aware of two serious options:

- stack
- nix

I believe using raw cabal is also an option, but I have no experience with it so I'm leaving it
alone.

Stack seems to be the de-facto choice for a lot of projects. However, I am currently developing
on NixOS and I've found it tricky to get stack working well.

I have some previous experience setting up nix-based haskell projects, they require some work but
I can steal some of the setup from my previous projects.

Given that the goal of this project is not specifically to learn a new haskell tool I'm going to
stick with what I'm familiar with and continue to leverage nix.

This also has the benifit of letting me manage non-haskell dependencies.

## Decision

I will use `nix` for dependency management

## Consequences

- The availability of haskell libraries will depend on the nixpkgs channel I am tracking
- Intero won't work unless I figure out how to get it to play nice.
- We need to decide on a way to get editors to play nicely with `nix-shell`

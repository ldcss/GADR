# ADR 0006: SDL2 for rendering

Date: 2018-09-30

## Status

Accepted

## Context

We're building a game, which means we need a way to render things, do audio, create windows
and other game-like activities.

We could use an engine like `Helm`, but since this project is about learning and exploring
possible architectures I don't want to take a pre-existing architecture.

We could use [gloss](https://hackage.haskell.org/package/gloss). However I used it in
a previous project and I don't like how it takes over the main loop, particularly as it
made it tricky to integrate into a MTL stack.

Instead I'm going to use the haskell bindings for [sdl2](https://hackage.haskell.org/package/sdl2). It's fairly low level but it's a cross-platform way to get an OpenGL context, and the high-level bindings seem reasonable enough.

## Decision

We're using [sdl2](https://hackage.haskell.org/package/sdl2)

## Consequences

- We're probably going to have to write a fair bit of wrapper code to get everything
  integrated nicely.
- Handling keypresses is probably going to be a pain.
- We have a significant degree of control!

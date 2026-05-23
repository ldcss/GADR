# 7. Use TypeScript for static typing

Date: 2021-08-03 (Backfilled 2021-08-29)

## Status

Accepted

## Context

As mentioned in [ADR #3. Use relatively modern tech stack](0003-use-relatively-modern-tech-stack.md) this project is intended to be a [breakable toy](https://www.oreilly.com/library/view/apprenticeship-patterns/9780596806842/ch05.html#breakable_toys) where I can experiment with other tech.

This project was first implemented in JavaScript. We want to use a static typing system so that we can catch more errors at compile time and to document the interfaces between different functions, components and so on.

## Decision

This project will be migrated over to TypeScript.

## Consequences

We will need to install other dependencies alongside TypeScript to ensure that our tests and linter can support this language.

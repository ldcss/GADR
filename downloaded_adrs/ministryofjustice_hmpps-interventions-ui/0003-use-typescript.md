# 3. Use TypeScript

Date: 2020-11-20

## Status

Accepted

## Context

We want to be confident about the code we write, and for it to be
self-documenting as much as possible. TypeScript is a compiled language with
optional typing. It's a superset of JavaScript, so is familiar to developers
who know JavaScript. It has wide editor support.

## Decision

We will use TypeScript by default.

## Consequences

This adds some overhead to developers, as they need to become familiar with
TypeScript if they aren't. It can also add some overhead when using
dependencies without existing type definitions.

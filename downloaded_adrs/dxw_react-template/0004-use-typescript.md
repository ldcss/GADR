# 4. Use TypeScript

Date: 2019-10-08

## Status

Accepted

## Context

We want to be confident about the code we write, and for it to be
self-documenting as much as possible.
[TypeScript](https://www.typescriptlang.org/) is a compiled language with
optional typing. It's a superset of JavaScript, so is familiar to developers who
know JavaScript. It has wide editor support.

As of writing, TypeScript is used by over
[1.4 million repositories](https://github.com/microsoft/TypeScript/network/dependents?package_id=UGFja2FnZS01MTE3ODUxNjg%3D)
on GitHub.

## Decision

We will use TypeScript by default.

## Consequences

This adds some overhead to developers, as they need to become familiar with
TypeScript if they aren't. It can also add some overhead when using dependencies
without existing type definitions.

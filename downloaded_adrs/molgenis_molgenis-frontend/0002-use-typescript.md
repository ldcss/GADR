# 2. Use TypeScript

Date: 2020-09-04

## Status

Accepted

## Context

We need a way to describe the structure of Javascript objects for readers of the code to be able to understand the structure.
And we need a way to detect null references at build time Javascript.
Our Javascript passes though a build step.
Our Javascript is maintained by people who did not write the code.

## Decision

We will use Typescript as a tool to describe object structure.

## Consequences

Typescript is used to write logic and typing information is added to describe object structure
Typescript support is included in our projects build chain.

# 09. Use TypeDoc to generate API documentation

Date: 2019-11-13

## Status

Accepted

## Context

We want to have API documentation for the code we publish. Rather than writing
separate API docs that quickly get out of date, we would like to be able to
generate it from our code and comments in our code that live next to the thing
they refer to. For JavaScript, the standard is [JSDoc](https://jsdoc.app/), but
with TypeScript, we're already defining the types in our code, and duplicating
that in the associated comments is repeated effort and requires manual action to
keep up-to-date.

[TypeDoc](https://typedoc.org/) is a documentation generator based on JSDoc. It
uses a combination of comments and TypeScripts own types to generate API
documentation automatically.

## Decision

We will use TypeDoc to generate documentation.

We will document all exported code for the benefit of end users.

We will commit the documentation we generate to the repository alongside changes
to behaviour.

## Consequences

If we document our code well, our API will document itself as a build artefact.
This greatly reduces the mainenance burden of keeping our documentation up to
date.

There is a slight learning curve to learning how to write TypeDoc comments that
turn into useful documentation. We can mitigate some of that by setting up
ESLint rules to help us write "correct" TypeDoc comments.

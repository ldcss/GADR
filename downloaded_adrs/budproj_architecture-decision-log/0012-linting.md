# ADR 0012: Linting

* [Table of contents](#)
  * [Context](#context)
  * [Decision](#decision)
  * [Status](#status)
  * [Consequences](#consequences)

## Context

We can code in many different styles. Each developer can write the same sentence in many different ways. It is not a problem in the short term, but our codebase can become a complete mess without any standards in the long run.

## Decision

We've decided to use a linter to avoid this problem, no matter the project size. Each language has its way of linting code, but every stack has at least a single tool to solve this problem.

Also, alongside our linters, we're going to use [editorconfig](https://editorconfig.org/), a great tool to standardize how we configure our text editors.

Some linters can extend properties. If your language linter can do so, we suggest creating a company-wide configuration and extend it in your application.

Below, we've listed the linters we're using for each language:

* **Javascript (React, Node, Typescript, ...):** [ESLint](https://eslint.org/) + [Prettier](https://prettier.io)

## Status

Accepted.

**Suggestion:** Since we accepted this ADR, we suggest all our applications add a hook and prevent committing without passing the linter.

## Consequences

Linting code provides a considerable amount of benefits, but it also came with some costs. It slows the development speed (since you must format your code before committing it), and it can annoy some developers.

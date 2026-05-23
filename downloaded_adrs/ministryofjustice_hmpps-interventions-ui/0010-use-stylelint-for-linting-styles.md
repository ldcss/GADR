# 10. Use Stylelint for linting styles

Date: 2021-02-18

## Status

Accepted

## Context

We want to enforce consistency in our code, and catch as many errors
automatically as we are able to. Linting the code is good practice to achieve
these aims. [Stylelint](https://stylelint.io/) is one of the more popular CSS
linters with support for SASS, and is easily configurable for our purposes.

## Decision

We will check SASS syntax using Stylelint.

We will use the recommended configuration for plugins where possible.

We will use Stylelint to automatically fix linting errors in a pre-commit hook.

## Consequences

Stylelint enables us to agree on and enforce a code style without having to
keep it in the heads of developers, meaning we shouldn't have to discuss
individual code style violations as they come up.

It will save time in code review, as any style issues will have been caught
before the PR is opened.

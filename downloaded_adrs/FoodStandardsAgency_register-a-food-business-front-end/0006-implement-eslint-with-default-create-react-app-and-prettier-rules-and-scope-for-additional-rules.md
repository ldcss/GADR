# 6. Implement eslint with default create-react-app and Prettier rules and scope for additional rules

Date: 2018-05-15

## Status

Accepted

## Context

JavaScript linting is required to enforce consistency of code style and best practices. There are different options for linting tools but ESLint is the most common. Within ESLint, there are many options for rules, plugins, etc.

## Decision

We will use ESLint as our linting tool.

We will extend the `react-app` and `prettier` linting rules.

We will use the Prettier 'recommended' config to disable any conflicting rules and enforce Prettier as the standard.

## Consequences

The app will not compile without strict compliance with the stated rules.

The resulting quality and readability of code will be higher.

Future changes to the linting rules are easy to make.

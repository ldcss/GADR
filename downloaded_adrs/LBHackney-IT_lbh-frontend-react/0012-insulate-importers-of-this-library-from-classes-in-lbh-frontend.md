# 12. Insulate importers of this library from classes in LBH Frontend

Date: 2019-11-28

## Status

Accepted

## Context

Not everything that has a style has a component in
[`lbh-frontend`](https://github.com/LBHackney-IT/lbh-frontend). We build the
`lbh-frontend` dependency into our distributables, making it hard for importers
to gain access to the stylesheets without duplicating some styles (see ADR 11).

React components insulates importers of this library from the internal
implementation details of how those components work. We want to continue to do
that, and not require users to understand the styling hierarchy and class names.

## Decision

When components don't exist in `lbh-frontend` and it doesn't make sense to add
them there, we will create new components in this library.

## Consequences

We will need to build components to cover all of the possible classes, which
means more components.

Importers of this library won't need to know about how the styles are
implemented to use it.

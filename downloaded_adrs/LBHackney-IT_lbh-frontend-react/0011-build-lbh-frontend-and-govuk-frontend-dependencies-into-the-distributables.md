# 11. Build lbh-frontend and govuk-frontend dependencies into the distributables

Date: 2019-11-13

## Status

Accepted

## Context

We are tightly coupled to `lbh-frontend` and `govuk-frontend`. We want to ensure
users having different versions doesn't cause problems.

It's also likely that users of this library will have no direct need of either
`lbh-frontend` or `govuk-frontend` as neither supports React. They also both use
Sass for their stylesheets, and we don't want to force users to do the tooling
to also support Sass themselves.

## Decision

We will bundle `lbh-frontend` and `govuk-frontend` into our distributables.

## Consequences

This decision reduces our dependency graph for users of this library, and
reduces the amount of setup users have to do in order to use it. On the other
hand, bundling stylesheets into this library directly makes it difficult for
users to reuse those styles in their own code without reusing classes. We think
this is a good trade-off.

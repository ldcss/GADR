# 2. evaluate buddy-auth for admin access controls

Date: 2018-09-08

## Status

Pending

## Context


Kuona instances need to be secured - particularly for deployments that have public access.

## Decision

https://funcool.github.io/buddy-auth/latest/#example-session Buddy seems to fit the bill and is compatible with Compojure and Ring. Provides a number of options and possible persistance mechanisme.

## Consequences

More complex setup and deployment requiring encryption key properties.

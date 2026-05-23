# 4. Move Services to top level

Date: 2019-11-01

## Status

Accepted

## Context

Initially the directory structure was to have the language as a top folder and have services below. However this makes it harder to use different language versions of the services together.

## Decision

Keep a monorepo for easier handling the project (it will never be grow too large and will not be maintained by different teams).
Move the services to top level. And have language versions below each service.

## Consequences

This setup make it easy to maintain the project and also makes it easier to use services in different languages together.


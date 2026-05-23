# 9. Use Helmet for HTTP security

Date: 2020-11-20

## Status

Accepted

## Context

We want to make sure we're setting the correct HTTP headers for security e.g.
Content Security Policy to protect against XSS attacks.
[Helmet](https://helmetjs.github.io/) is a package that works well with Express
to make it easy to set various HTTP headers for secutiy.

## Decision

We'll use Helmet to set secure HTTP headers.

## Consequences

Less risk of XSS attacks and exploits.

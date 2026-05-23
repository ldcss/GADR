# 11. Use aXe for automated accessibility testing

Date: 2019-10-16

## Status

Accepted

## Context

We want to be able to ensure our pages are accessible.

[Axe](https://github.com/dequelabs/axe-core) is an actively supported
accessibility testing engine for HTML-based user interfaces that supports all
modern browsers (including IE 9+).

## Decision

We will use axe for accessibility testing. We will integrate it with Jest via
[`jest-axe`](https://github.com/nickcolley/jest-axe), enabling us to integrate
with all of our tests.

## Consequences

Axe should enable us to catch a portion of any accessibility issues that show up
while testing. It requires explicitly running the accessibility checker for a
test case.

This doesn't remove the need for manual testing. Automated accessibility testing
can only find
[around 30% of issues](https://accessibility.blog.gov.uk/2017/02/24/what-we-found-when-we-tested-tools-on-the-worlds-least-accessible-webpage).

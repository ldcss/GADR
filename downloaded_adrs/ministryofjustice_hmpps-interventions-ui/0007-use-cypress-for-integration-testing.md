# 7. Use Cypress for integration testing

Date: 2020-11-20

## Status

Accepted

## Context

We want to be able to automate testing end-to-end user journeys through our
application. Cypress is an alternative to Selenium that runs in the browser to
do this for us, and is used across multiple projects at MOJ.

## Decision

We will use Cypress for integration tests.

## Consequences

There will be some overhead in writing tests in Cypress, but this will ensure
we catch any regressions introduced by changes to the codebase.

There are some limitations to using Cypress as an integration framework,
particularly that it may not be possible to test situations in the browser
where JavaScript is disabled for any reason, which presents some difficulties
in trying to [build a resilient frontend using progressive
enhancement](https://www.gov.uk/service-manual/technology/using-progressive-enhancement#building-more-complex-services).

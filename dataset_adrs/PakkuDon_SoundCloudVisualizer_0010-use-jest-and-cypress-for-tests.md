# 10. Use Jest and Cypress for tests

Date: 2019-11-17

## Status

Accepted

## Context

There are currently no tests in this application. This was partly because there were a lot of options to choose from out of all the testing frameworks or libraries available for JavaScript, and because it felt a bit excessive for a side project.

Since then testing frameworks such as [Jest](https://jestjs.io/) and [Cypress](https://www.cypress.io) have surfaced. Both of these promise a more developer-friendly experience. I figured I should get more practice with these tools and decided it'd be best to try them on an existing project.

## Decision

Jest and Cypress will be used to test this application.

## Consequences

- Components will be unit tested using Jest.
- An end-to-end test will be written using Cypress.

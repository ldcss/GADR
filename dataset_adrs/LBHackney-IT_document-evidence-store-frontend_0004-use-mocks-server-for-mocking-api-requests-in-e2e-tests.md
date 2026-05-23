# 4. Use mocks-server for mocking API requests in e2e tests

Date: 2021-02-03

## Status

Proposed

## Context

When our API requests were being made from the client side, Cypress was able to intercept and mock them during end-to-end tests. Having implemented the change described in [ADR 2](/0002-switch-from-client-side-api-requests-to-server-side.md), our API requests are being made from the server which Cypress has no view of.

We can:

1. Change our production server code to be able to mock it
2. Allow our server to talk directly to external resources during e2e tests
3. Setup some kind of mock server which sits next to our server and intercepts the requests

It's important that:

- our tests run reliably and predictably every time, whether locally or on CI
- we are able to setup and test specific circumstances to ensure we cover important paths through our system
- we are testing as much of our production code as possible

## Decision

Option 1 would mean short-circuiting our production server so some code wouldn't get tested; this code is tested in unit tests but if we can include it in our end-to-end tests, this would give much higher confidence in our test suite.

Option 2 would not meet our criteria above; if the external API went down or our local system's network became unreliable, our tests may fail. It would also require setting up predictable scenarios for testing against in external services, which could be changed by other actors at any time.

We have decided to pursue option 3. There are a number of third party options, [`mocks-server`](http://mocks-server.org) is well maintained and provides an admin API and a Cypress integration to allow us to modify the behaviour of the server from within the test suite, meeting all of our criteria.

## Consequences

New API interactions and scenarios will require setting up fixtures and behaviours in the mock server config, this is a small price to pay to have confidence that our test suite is covering our entire stack.

A secondary benefit of this server is that we can use the mock server when developing locally, removing dependency on external APIs that may not have been completed.

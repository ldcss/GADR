# 3. testing-model-in-DOM-integration-tests

Date: 2019-05-09

## Status

Accepted

Supercedes [2. Using react-testing-library](0002-react-testing-library.md)

## Context

We want to avoid testing implementation details in our integration tests.

We want to use `react-testing-library` which makes it easier to make assertions on the rendered DOM rather than assert implementation details. But mostly because it enable us to find and trigger click events on different UI elements.
e.g. toggling the visibility of different tabs and window groups.

When it comes to asserting the rendered DOM, in most cases we trust the view will render the model properly.  It could be more sensible to only verify the state/model.

But, we had a small problem described in ADR-0002.

## Decision

We will assert both against the session in the provider **and** against the DOM elements to make sure the application view is updating properly.

## Consequences

We'll see...

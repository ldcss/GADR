# 2. Using react-testing-library

Date: 2019-05-09

## Status

Superceded by [3. testing-model-in-DOM-integration-tests](0003-testing-model-in-dom-integration-tests.md)

## Context

We want to avoid testing implementation details in our integration tests.

We want to use `react-testing-library` which makes it easier to make assertions on the rendered DOM rather than assert implementation details. But mostly because it enable us to find and trigger click events on different UI elements.
e.g. toggling the visibility of different tabs and window groups.

But when it comes to asserting the rendered DOM, in most cases we trust the view will render the model properly.
It could be more sensible to only verify the state/model.

## Decision

We will assert against the session in the provider which is accessible through the context. (the BananaContext instance, not a React Context)

## Consequences

We managed to write some intergration tests rendering with `react-testing-library` and then only verifying the resulting session object. But in one instance, we broke the application by deleting a callback, and the tests continued to pass. This was because we were not testing that the DOM was being changed; we only tested the session.  
So, in retrospective, we think it's better to have (and we do) some functions to "read" the resulting DOM elements and make assertions, as well as asserting the session.

# 4. Prevent multiple sagas to be registered by the same key

Date: 2019-06-20

## Status

Accepted

## Context

Container components can inject sagas and have them registered by a specific key. This key doesn't have to be unique. This, however, leads to unexpected problems when running on a production build. In development it's not an issue, because of hot-reloading, but in production, having more than one saga be registered by the same key, fails silently.

What happens is that the already registered saga is overwritten by another saga. The first sagas functionality will no longer be available to the application.

## Decision

Injecting more than one saga with a key that has already been used, will throw an error and will prevent the application from running.

## Consequences

Sagas cannot be accidentally overwritten without warning.

Test coverage decreases, because of the inability to cover hot-reloading by tests. Two responsible test cases have been marked as to skip in [sagaInjectors.test.js](../../app/utils/__tests__/sagaInjectors.test.js#L193-L225) for that.

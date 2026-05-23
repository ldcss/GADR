# 6. ViewModel exposing whole state instead of single data streams

Reverts [ADR 0002](0002_remove_state.md)

Date: 2019-10-06

## Status

Accepted

## Context

After saw the results of ADR 0002 (update stream mess) and read some blog posts regarding "redux like" Android apps,
we should move back to exposing whole state objects from the ViewModel.

## Decision

ViewModels exposing a single state object (sealed class) which is handled by the fragment.

## Consequences

All ViewModel classes have to be refactored and state classes have to be implemented. Therefore also
the unit tests have to be altered to fit the new logic.
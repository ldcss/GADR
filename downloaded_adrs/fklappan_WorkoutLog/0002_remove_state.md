# 2. Remove the state objects from the view models

Reverted by [ADR 0006](0006_viewmodel_exposing_state.md)

Date: 2019-07-29

## Status

Accepted

## Context

I think exposing the whole state from the ViewModel to the fragment moves some logic to the fragment and is error prone
in my opinion.

## Decision

Instead of exposing whole state objects, we expose only single properties which can individually handled by the fragment

## Consequences

Some fragments and viewmodels needs to be refactored. It is no longer possible to log whole state updates within the
Fragment class.
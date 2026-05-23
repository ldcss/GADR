# 4. Extend Application Bar for search feature

Date: 2019-09-15

## Status

Accepted

## Context

We need a consistent way to add menus within fragments.

## Decision

Every fragment handles its menu independently. This is achieved through calling setHasOptionsMenu(true)
and overriding the specific methods needed for creating the menu and handling selection events.

## Consequences

The implementation could differ between the fragments and we need to address that with code reviews.
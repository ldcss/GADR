# 3. Theme namespace naming convention

Date: 2020-08-13

## Status

Accepted

## Context

We need to pick a namespace for themes, and renaming can be tedious.

Only one theme is ever active at a time, so there's no risk in naming collisions except when dealing with child themes.

## Decision

We'll use the `\Theme` namespace for every theme we make except for child themes which will have the namespace `\ChildTheme`.

## Consequences

This will mean we won't need to rename the theme before starting work on it.

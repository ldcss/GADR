# 8. Methods representing events should have a "on"-prefix

Date: 2020-03-09

## Status

Accepted

## Context

Onboarding new engineers on a software project should be fast. Also our future self should be back on track on a project fast. 
Consistent and logical naming can be a benefit here.

## Decision

All "event"-methods within a ViewModel class should have a prefix "on". Events are methods which are called by the view.
(ie. onClickFavorite, onSearchChanged).

## Consequences

The existing ViewModel classes have to be edited.
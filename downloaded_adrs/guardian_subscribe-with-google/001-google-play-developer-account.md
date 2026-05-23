# Google Play Developer account

## Context

Our SKUs exist within a Google Play Developer account which is not linked to the "The Guardian" project (instead it is linked to the "Google Play Android Developer" project).

This means we are unable to programmatically obtain Play related data (i.e. SKUs) via Google APIs.

## Decision

Create a new Google Play Developer account and link it to "The Guardian" project. This allows us to query Google APIS for Play related data.

## Status

Accepted

## Consequences

* Gives us isolation from other Guardian/Google Play data & SKUs (i.e. Android premium subscriptions).
* We'll have to re-create any SKUs in the new account.
* $25 sign up fee for new Play account.

## Positions

* Create a new Google Play Developer account and link it to "The Guardian" project.
* Move our SwG app into the "Google Play Android Developer" project.

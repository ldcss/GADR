# 13. Application layer naming

Date: 2019-05-09

## Status

Accepted

## Context

We need clearing naming for each layer of the Use an LPA service.

There are 3 layers:
- A front service layer through which Actors will access the service.
- A front service layer through which Viewers will access the service.
- A backend service shared by the two front services which will provide data access and some domain logic.

## Decision

The 3 services will be called:
- Actor Front
- Viewer Front
- Api

## Consequences

We have a common naming convention for these layers.

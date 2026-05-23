# 3. This will be a general UI

Date: 2021-02-01

## Status

Accepted

## Context
This project started out as a permission UI specifically for the Armadillo suite. Along the way it became clear that it could
be used for other Fusion Auth applications as well.

## Decision

The server and UI in this project are generalized in such a way that they can be used for any Fusion Auth application.

## Consequences

* No application-specific content/features can be added without some form of configuration
* The project can be reused for other applications

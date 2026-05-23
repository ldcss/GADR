# 9. Service Layer

Date: 2017-09-24

## Status

Accepted

## Context

A Controller is responsible for receiving a request, executing it and returning an appropriate response.

A service layer can be added to remove knowledge of how an operation is performed from a Controller, allowing it to focus on the responsibilities mentioned above.

## Decision

We will use a service layer to ensure that Controllers do not contain business logic.

## Consequences

A Controller will be responsible for pulling the required information from a request, calling the appropriate service layer method and returning an appropriate response.

A Controller will not have direct access to the Pocket APIs or the data repositories.

The service layer will be responsible for executing an action on behalf of a Controller. This may involved communicating with the Pocket APIs and/or storing/retrieving data from the database.
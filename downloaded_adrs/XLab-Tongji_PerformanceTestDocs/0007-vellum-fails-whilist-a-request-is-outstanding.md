# 7. Vellum Fails whilist A Request Is Outstanding

Date: 2018-06-17

## Status

Accepted

## Context

A Vellum node fails whilst a request from Sprout or Dime is outstanding. this will typically result in failure of the request that the Sprout / Dime node was processing (with a return code indicating that it should be retried)

## Decision

Sprout / Dime node sends request which is retried an alternative, Vellum node will be used instead

## Consequences

Request succeeds or fails
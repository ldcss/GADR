# 4. REST Standards

Date: 2020-05-11

## Status

Accepted

## Context

With the absence of a more complete set of organization-wide standards, I want to document some decisions on how the REST endpoints within this service should behave.

## Decision

* Requests MUST respond with the following status codes:
  * `200` if the format of the request was valid, and there was meaningful data found
  * `400` if the format of the request was not valid
  * `404` if the format of the request was valid, but no meaningful data could be found
* JSON responses MUST be in the format of an object, not an array. If a search endpoint needs to return an array, it should be a top-level element of the response object. Rationale: Objects can be extended, arrays cannot.
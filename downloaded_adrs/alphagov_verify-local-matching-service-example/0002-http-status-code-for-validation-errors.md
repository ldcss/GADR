# 2. Http status code for validation errors

Date: 2017-11-21

## Status

Accepted

## Context

There can be validation errors when the request does not match the contract of the endpoint. These errors are mapped to
http status code 422(Unprocessable Entity) with one or many error message(s).

## Decision

Matching Service Adapter(MSA) ignores if the response has any other status code other than http status code 200 (OK). 
So for now we are letting the Dropwizard handle exception and return status code to MSA. 
When there is validation error, it returns http status code 422 with the error message.

## Consequences

There are no custom exception mappers that maps exception to Response object, we wont have control on the 
status code and error message.

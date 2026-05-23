# 2. Use JWT for API Authorization

Date: 2018-10-15

## Status

Accepted

## Context

The API portion of this application will require authentication.

JSON Web Token (JWT) is an open standard described by [RFC 7519]( https://tools.ietf.org/html/rfc7519).

[Additional Information](https://en.wikipedia.org/wiki/JSON_Web_Token).

## Decision

We will use JWT for authentication.

## Consequences

Using JWT allows us to use a best practices pattern for authentication and
support libraries to make the implementation much more secure and efficient.

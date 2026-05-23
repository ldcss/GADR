# 2. Version API via URI path

Date: 2017-10-13

## Status

Accepted

## Context

Versioning APIs can be controversial.  Ideally, APIs don't need to change, or be additive so as not to break backwards compatibility.  Occasionally, some changes require bigger changes.  

We will do our best to be open w/ what we accept and strict w/ what we return

There are lots of ways an API can change:
* Breaking changes across the entire API (all endpoints change from REST to GraphQL for example)
* Breaking changes at a resource level (/v1/booking) needs to change
* Breaking changes in behavior

This decision currently applies to the 1st bullet.

## Decision

All API endpoints will start with the version of the API (e.g. /v1/resource).  We don't anticipate this to change.

## Consequences

Changing this version impacts all endpoints.  Old (v1) endpoints will need to link to other old (v1) endpoints in requests/responses.  There's no way to mix/match

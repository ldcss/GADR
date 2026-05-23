# 3. Session storage using JWT

Date: 2019-02-21

## Status

Superceded by [8. Session storage using an encrypted cookie](0008-session-storage-using-an-encrypted-cookie.md)

## Context

Very small amount of data stored in session

## Decision

JSON Web Tokens (JWT) for session storage (rather than DynamoDB or ElastiCache)

## Consequences

* Less infrastructure components
* Requires additional application libraries for managing the JWT and encryption
* Security will need consideration if storing session data that is sensitive for anything other than short periods (i.e temporary tokens are fine, personal details etc are not)

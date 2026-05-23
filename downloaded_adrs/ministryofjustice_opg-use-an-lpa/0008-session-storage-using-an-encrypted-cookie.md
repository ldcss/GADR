# 8. Session storage using an encrypted cookie

Date: 2019-05-01

## Status

Accepted

Supercedes [3. Session storage using JWT](0003-session-storage-using-jwt.md)

## Context

* We will be storing a very small amount of data in the session.
* Whilst the above holds true we can avoid additional infrastructure by using client side storage.
* The session _may_ hold somewhat sensitive details (e.g. an LPA Share code), thus its content is secret.
* As the cookie is client side, we also need authentication to ensure the message isn't tempered with.

## Decision

To use a cookie who's payload is encrypted with AES GCM. This provides secrecy and authentication.

Not to use JWT, because:
* To ensure message secrecy, additional libraries are needed.
* The resulting cookie value is significantly larger.
* Concerns over the general suitability around using JWT for client side sessions.

## Consequences

* Cookie size will be smaller.
* One package can provide both the secrecy and authentication.
* The overall risks are considered to be less than using JWT.

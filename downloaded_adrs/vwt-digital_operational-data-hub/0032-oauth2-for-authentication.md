# 32. Oauth2 for authentication

Date: 2020-09-21

## Status

Accepted

Implements [6. Implement Security by Design](0006-implement-security-by-design.md)

## Context

Using http protocol and APIs, authentication and authorisation is mostly done by passing some token with every request. Fixed secrets are easy to understand and configure, but somewhat weak in protection. Instead, oauth2 is a stronger mechanism to create tokens, though more complicated. In oauth2 authentication and authorisation are decoupled and the security critical authentication is delegated to the authorization server. Still, oauth2 allows distributed token validation next to validating the token with the server.

## Decision

We will use oauth2 for authentication and authorization.

## Consequences

### Advantages

* Strong authentication and authorisation mechanism.
* Allows distributed token validation.
* Mature and commonly used standard.
* Relying on company authorization server provides user management and single sign-on.

### Disadvantages

* Oauth2 concepts and implementation can be complicated.

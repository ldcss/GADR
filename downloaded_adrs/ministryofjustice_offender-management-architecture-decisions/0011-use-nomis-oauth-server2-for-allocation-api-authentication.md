# 11. Use NOMIS OAuth2 server for allocation API authentication

Date: 2018-11-21

## Status

Accepted

## Context

We need to protect the allocation API with authentication, but we'd rather not
have to come up with an approach to do that ourselves from scratch.

The new [NOMIS OAuth2 server](https://github.com/ministryofjustice/nomis-oauth2-server)
is already being used in production for authentication on almost all of the
NOMIS APIs and some other APIs built in Sheffield. We will need to use it to
authenticate with the Custody API, and the other services which may need to use
the allocation API are very likely to already be using this authentication
method for the other APIs they use.

Clients can use one token (of a particular grant type) to authenticate with all
APIs which use the NOMIS OAuth2 server, which makes things simpler for all
those services - they don't have to work with multiple different authentication
approaches.

The NOMIS OAuth2 server uses JWTs signed with a private key, so relying
services can verify the integrity and authenticity of tokens presented by
clients using the corresponding public key.

We've decided that the allocation manager will be entirely responsible for user
access control and will call other APIs directly, and the allocation API will
be a smaller interface onto its data (see [ADR 0010](0010-allocation-api-has-less-responsibility.md)).
That means that the allocation API doesn't need to know which user it's
returning data for, and we can use a system-to-system approach to
authentication.

We don't know of any other shared approaches to API authentication which are
used in the prison space.

## Decision

We will use the NOMIS OAuth2 server for authentication on the allocation API.

We will use the client credentials OAuth2 grant type for authentication on the
allocation API.

We will verify signatures on presented tokens in the allocation API.

We will respect expiration times on presented tokens in the allocation API.

## Consequences

We need to come up with our own approach to modelling permissions for the API,
using roles and/or scopes in the NOMIS OAuth2 server. We will need to build
support for restricting access based on that into the allocation API. In future
that approach will probably need to account for other clients having more
limited read access to the API than the allocation manager needs.

The allocation manager and any other clients of the allocation API will be able
to use the same client credentials token for this API and several others in
this space.

Clients of the allocation API will be responsible for implementing appropriate
access control around their use of data from the API.

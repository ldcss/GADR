# 004 - Authentication and Authorisation

- Date: 2020/01/28
- Status: Superseded by ADR-008
- Deciders: Daniel Stefaniuk, Jonathan Pearce, Matthew Begley

## Context

The Capacity Status API will enable UEC service providers and DoS Leads to change the RAG status (also known as the Capacity Status) of their services in DoS.

To protect from unauthenticated users and to prevent authenticated users from being able to update capacity status information for services that they do not have permissions for, the Capacity Status API will need to authenticate users via a modern authentication approach, and will need to establish whether the user is authorised to be able to update the capacity status information of the service.

## Decision

The two concerns here are authentication and authorisation.

### Authentication

Authentication of the API is concerned with protecting the API against unauthenticated, unknown, or inactive users. A couple of options were discussed:

- API Key authentication
- OAUTH2 authentication

For the purposes of the private Beta involving a known (and limited) user base, it was decided that protecting the API by means of an API Key authentication mechanism would be the most appropriate. This mechanism is simple to implement on both the API and the client (user) side, and since we are only dealing with one user group for private beta we felt that the OAUTH2 authentication mechanism was overly complex for our immediate use case.

This decision will be re-evaluated should the API move into the next phase of development (public beta).

### Authorisation

Authorisation of the API is concerned with preventing authenticated users from being able to update capacity status information on services that they do not have permission for. It was discussed that Core DoS already manages the permissions of which services a user has permissions to update. The decision was made to leverage this information stored in Core DoS rather than managing and maintaining a separate set of the permissions within the API itself. Although arguably this creates a dependency on Core DoS for the API, it means that there is only one place to hold the permissions, and ensures both Core DoS and the API are always aligned.

## Consequences

- Implementation of authentication mechanism on both API and client side is simple.
- We maintain one core store of user services permissions (in Core DoS), so the API doesn't have to concern itself with maintaining and keeping its own set in synchronisation.
- Since we need to look up the user permissions in Core DoS, the implementation of the authentication mechanism will be slightly more complex in that we will need a way to link a Core DoS user with an API Key. This is not a major concern however, as Django makes it very easy to modify (or extend) its core models.
- API Key Authentication isn't as secure as mechanisms such as OAUTH2, but for our immediate use case for private Beta it is sufficient. This decision will be re-evaluated if the API goes into the next development phase.

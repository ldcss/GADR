# 008 - Authentication and Authorisation (revisited)

- Date: 2020/03/31
- Status: Proposed
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

For the purposes of the private Beta involving a known (and limited) user base, it was originally decided that we would implement API Key authentication using a Django authentication extension application. However, as we got deeper into the development, it became evident that this solution wasn't what we required. Despite the naming of the API Key Authentication application, we found that this application was really an 'authorization' mechanism and not an 'authentication' mechanism. Thus the application hooked into the Django Rest Framework (DRF) via its permission classes (rather than via its authentication classes). This brought with it a number of concerns:

- Usability - Because the application was hooked into DRF's permission classes, an HTTP 403 - Forbidden response was returned from the API if it was sent a request with either no, or invalid credentials. Our desired outcome is for an HTTP 401 - Unauthorized response to be given.
- Security - More importantly, because this application is not hooked into the DRF's authentication classes, the question was raised as to how secure this mechanism really was.

Although we could have overridden the DRF framework and have it raise am HTTP 401 instead of an HTTP 403, this still wouldn't have addressed our concerns over how secure this mechanism actually was. It was therefore deemed that this mechanism was not right for us.

After some more investigation, we found a token based authentication application. This authentication application provided us with everything that the original API Key application provided, and it also hooked into the DRF's authentication classes. Because of this the DRF responded with the desired HTTP 401 - Unauthorized response on receipt of a request containing no or invalid credentials.  Moreover, as far as our users of the API are concerned, there is no difference in process between this token based authentication mechanism and the originally proposed API Key authentication mechanism. The only difference is a technical one whereby the authentication header in the request needs to be prefixed with the text 'Token', rather than 'API Key'.

This decision will be re-evaluated should the API move into the next phase of development (public beta).

### Authorisation

Authorisation of the API is concerned with preventing authenticated users from being able to update capacity status information on services that they do not have permission for. It was discussed that Core DoS already manages the permissions of which services a user has permissions to update. The decision was made to leverage this information stored in Core DoS rather than managing and maintaining a separate set of the permissions within the API itself. Although arguably this creates a dependency on Core DoS for the API, it means that there is only one place to hold the permissions, and ensures both Core DoS and the API are always aligned.

## Consequences

- Implementation of the choosen authentication mechanism on both API and client side is simple.
- We maintain one core store of user services permissions (in Core DoS), so the API doesn't have to concern itself with maintaining and keeping its own set in synchronisation.
- Since we need to look up the user permissions in Core DoS, the implementation of the authentication mechanism will be slightly more complex in that we will need a way to link a Core DoS user with a Token. This is not a major concern however, as Django makes it very easy to modify (or extend) its core models.
- Token authentication isn't as secure as mechanisms such as OAUTH2, but for our immediate use case for private Beta it is sufficient. This decision will be re-evaluated if the API goes into the next development phase.

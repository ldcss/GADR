# 4. Security

Date: 2017-12-01

## Status

Accepted

Amended by [5. Use id_token from Microsoft as Bearer token](0005-use-id-token-from-microsoft-as-bearer-token.md)

Amended by [6. Use Okta as Identity provider](0006-use-okta-as-identity-provider.md)

## Context

Bookit needs the concept of a user so it can identify who booked what bookable and allow certain users to overrule a booking.

This involves both authentication (who you are) and authorization (what you're allowed to do).  For the MVP we are primarily focused on Authentication.

Employees from different domains (Wipro, Designit, Cooper, etc) need to log into the system.  

Protect all endpoints, optionally allow /ping but, if authentication provided, return profile information as well.

## Decision

* We will use Azure AD v2 OpenID Connect to exchange an id_token for an opaque Bookit API opaque access_token

## Consequences

* Assume will only work with Azure AD
* Might have to also allow basic auth with a default admin user/password to access via browser and /management endpoints
* Complicated flows that can break and are dependent on Microsoft
* Need to validate security consequences (using id_token to exchange)
* Need to consider how to do automated testing but still be secure in production/staging
    * Currently will only limit FAKE tokens to localhost and integration environments
* TBD - format of opaque access_token - assume JWT
* TBD - return opaque token as cookie or in response to go into localstorage - assume localstorage

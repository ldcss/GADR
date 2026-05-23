# 5. Use id_token from Microsoft as Bearer token

Date: 2017-12-01

## Status

Accepted

Amends [4. Security](0004-security.md)

Alternative considered [6. Use Okta as Identity provider](0006-use-okta-as-identity-provider.md)

Alternative considered [7. Use Pac4J to validate tokens](0007-use-pac4j-to-validate-tokens.md)

## Context

In the interest of time and getting something to work, we are going to break up the steps further

## Decision

* Instead of exchanging id_token for opaque access_token, the client will always send the id_token as the Bearer token
* Proper validation of the id_token will still occur

## Consequences

* The security implications are uncertain.  This is definitely not what the id_token is inteded for but it's unclear after much googling what the security holes are. 
* If/when we need actual delegated authorization, especially against the MS Graph API, we will need to revisit this and acquire access_tokens

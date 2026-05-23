# 7. Use Pac4J to validate tokens

Date: 2017-12-07

## Status

Decline

Alternative to [5. Use id_token from Microsoft as Bearer token](0005-use-id-token-from-microsoft-as-bearer-token.md)

## Context

http://www.pac4j.org

While exporing alternatives to our custom filter and token validator, we came across pac4j which can deal with Azure AD out of the box.

The driver for this alternative is to have a library where we can point it to the discovery url (https://login.microsoftonline.com/organizations/v2.0/.well-known/openid-configuration) and have it "just work."  Microsoft is a bit off standard where they add {tenantId} to the Issuer URL because this is a multi-tenant endpoint.  While it's not hard, openid connect libraries need to be adjusted to handle this.  Pac4j does this for free.



## Decision

* Use Pac4J to validate MS id_tokens instead of our current custom filter code

## Consequences

* Less unit testing on our end
* Pac4J only supports the Authorization Code flow which is not what we would be using
    * Unless we went with the hybrid flow (id_token + code)
* Pac4J is an additional layer on top of Spring Security (as it can be used with a variety of other frameworks)
    * As such we would have to learn yet another framework to configure security
* There is a HeaderClient that would work with the JwtAuthenticator to handle Bearer tokens but can't hook into the AzureAdClient that we're seeking

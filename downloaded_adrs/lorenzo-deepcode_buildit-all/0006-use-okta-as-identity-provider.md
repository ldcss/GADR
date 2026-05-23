# 6. Use Okta as Identity provider

Date: 2017-12-07

## Status

Spiked - Delay for now

Amends [4. Security](0004-security.md)

Alternative to [5. Use id_token from Microsoft as Bearer token](0005-use-id-token-from-microsoft-as-bearer-token.md)

## Context

Okta is an Identity as a Service provider (similar to Auth0) that can provide authentication and authorization support to an application.  They have a forever free developer account that allows up to 7000 active users/mo (well below our anticipated usage).

Okta provides the ability to authenticate against a variety of providers (okta, social (facebook, github, microsoft azure, etc), SAML, AD/LDAP).  We would use the Microsoft social OpenConnect ID provider.  It will map the Microsoft user into an Okta user, essentially acting as a proxy or facade to Microsoft while providing a more uniform and standards adhering API.

They have integrations into Spring Boot 1.x (via okta spring security starter) and Spring Security 5.x (via Spring Boot 2.x) supports Okta out of the box.

They have a React client SDK instead of using our handrolled client code for Microsoft Azure AD.

The real value add comes when we need to add roles/groups (admin level users).  You get admin screens/dashboards "for free" to add/remove users etc.

Later on, we could add additional social logins (or support AD directly if needed).

Spike can be found at: https://github.com/buildit/bookit-api/tree/okta-spring-boot-1.x

## Decision

* Delay for now - because we think we still need a local user table, we can add this in later


* Use Okta as IdP for Bookit
* Use Okta's React client for client side code
* Use Okta's Spring Boot 1.x starter for 
* Use Okta Access Tokens as Bearer tokens
 
## Consequences

* Spring Boot 2.x supports Okta out of the box but is not released nor does it currently support @EnableResourceServer which is probably what we would need - https://github.com/spring-projects/spring-security/issues/4887
* Likely still need a local user table to quickly do queries (e.g. find "my" bookings, see who booked a room)
    * Also useful as a layer of abstraction/indirection if we need to move to or away from this solution
* Using Access Tokens allow us to support 3rd party API access in the future
    * But would need to figure out how to get user detail information either in the access token or query userinfo endpoint
    * And when/how to keep in sync with our local users
* The forever free developer account has some limiatations
    * Does not provide any SLA
    * Cannot customize verification emails
* Uncertain how we'd acquire an actual MS Graph access token if we needed to access a user's email or calendars.

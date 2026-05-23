# 3. Shibboleth Implementation

* Status: Accepted
* Date: 2019-12-17

## Context
Both Lux and Curate need to authenticate users to enforce authorization. Emory uses Shibboleth to manage
authentication for University applications. Curate has gone through the lengthy process of requesting access to
Shibboleth, and implemented user management through it. Part of the request was enumerating the "attributes" or
metadata Curate needs to receive when a person logs in. Curate currently has three "endpoints", or applications,
that can use its access to Shibboleth (prod, test, and arch).

Lux also has access to Shibboleth, with the same three configured endpoints, and the same attributes.

Lux does need to allow new users to sign in, where Curate does not.

In production, neither application needs to allow users to authenticate from another source.

## Decision
Lux will not use endpoints from Curate's Shibboleth access, instead using its own config. From the Lux side,
a configuration option will be available to use database auth instead, for development, and to ease rollout.
If the configuration option is not present, database auth will be used.

## Consequences
Initial implementation will happen on digital-arch. Once that is stable, and tested, it will be rolled out
test, and after more testing, finally prod. Until testing has been completed, database auth will remain on for
the other systems.

Changes to Shibboleth attributes or configuration for Lux and Curate will not impact the other application,
potentially leading to scenarios where both need to be changed.

## Alternatives

### Use Curate's configuration.
Add three new endpoints to Curate's Shibboleth configuration for Lux to use.
- PRO: Both applications, which are interrelated, receive updates together.
- CON: The indivitual needs of each application are not the same.

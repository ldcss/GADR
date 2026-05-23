# 11. Use Auth0 for temporary user authentication

Date: 2018-07-18

## Status

Accepted

## Context

Our user facing applications will need to authenticate users.

In the long-term, we want to use the standard user sign-on services in CCS for
each appropriate user group.

For suppliers, this is the [Supplier Registration Service (SRS)][service-srs].
For CCS staff it is their G-Suite account.

Using a single authentication service will reduce administration overheads
because we won't have to manage a JML (Joiners Movers Leavers) process. For
users it will also mean they don't have to remember yet another username and
password combination.

However, we want to get moving quickly, and integration with SRS/CCS G-Suite
will take time. For now, we want a simple sign-in service that we can integrate
with quickly, to enable us to test and iterate the application.

## Decision

We will use [Auth0][service-auth0] for authentication on a temporary basis.

Auth0 is an authentication service that uses the OAuth protocol. It provides
and simple integration path, and is free for several thousand active users.

We acknowledge that we are incurring technical debt by not integrating
immediately with SRS and G-Suite, however we believe that this will let us move
more quickly during development.

This decision will also allow us to gain a better understanding of the user
needs around authentication before a decision around the final authentication
solution is made.

We will replace Auth0 with the proper authentication service later in the
development process.

## Consequences

We will integrate with Auth0, but will need to replace this later.

We will work with other projects within CCS to establish the user needs around
authentication, and feed into the decision around the final solution.

[service-srs]: https://supplierregistration.cabinetoffice.gov.uk/
[service-auth0]: https://auth0.com/
[oath]: https://en.wikipedia.org/wiki/OAuth#OAuth_2.0

# 7. Add basic authentication to test environments

Date: 2017-10-26

## Status

Accepted

## Context

Every environment the application is available in, be that development, review,
staging or public are openly available to anybody. There is no access control
at all.  This isn't suitable for a site that could be misinterpreted as the
'real' version either by people or by search engines and other bots. There
needs to be some form of hurdle to overcome in order to prompt people to
consider whether this is the correct site. There should also be a barrier to
prevent access by bots.

## Decision

We have decided to use basic authentication on the service in all environments
apart from the public facing one. This will only be applicable to the
environments hosted within the Rancher environment. The username and password
will not be secret and will be included within the `README` of the application.

## Consequences

Consequences include:

* Test sites will require basic authentication credentials to access

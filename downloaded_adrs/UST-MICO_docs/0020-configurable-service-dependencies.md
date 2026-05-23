# Configurable Service Dependencies


## Context and Problem Statement

Services currently have a static network of dependencies. This makes it impossible to have a service that depends on a SQL based database use a different database that is compatible with the service.


## Decision Drivers

* Should fit in the current domain model
* Easy to add afterwards
* Should support existing services with their static dependencies


## Considered Options

### Let service specify options for dependencies

Let the user specify if the dependency is optional and/or what other services may be used to fulfill the dependency.

Pro: High control over allowed alternatives.

Contra: Can't capture all alternatives.

### Specify if services are a compatible alternative to a different service

Let the user specify if a service can be used as alternative to an existing service.

Maybe add meta-services that are similar to meta-packages in linux package managers.

Pro: Works for all existing services.

Contra: There may still be incompatibilites.

### Add service groups for services that are interchangeable

Same as above but with different implementation.

Let the user define service groups to group services that can be used interchangeable.

Contra: Needs dependency edges to group objects that are not deployable (=> more implementation work)

### Hardcode some service groups

Hardcode some service groups (e.g. Database services). The service groups can have special properties customized for the included services. The services can still be added to the hardcoded groups by a user.


## Decision Outcome

To be decided.

This adr purely documents possible decisions for this problem.

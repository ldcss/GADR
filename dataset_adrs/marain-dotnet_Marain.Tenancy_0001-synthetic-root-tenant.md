# Synthetic Root Tenant

## Status

Accepted.

## Context

Corvus Tenancy, which provides the underpinnings of the Marain Tenancy service, has always had a concept of a root tenant (dating from its earlier, pre-open-source incarnation). This ADR captures aspects of this root tenant that are non-obvious. (We learned that it was non-obvious because some code has been written that was unaware of the special status of the root tenant.)


## Decision

There is a special tenant known as the Root Tenant. It has a well-known id, `f26450ab1668784bb327951c8b08f347`. It is special in three respects:

 * tenants are hierarchical, and the root tenant forms the root of that hierarchy
 * the tenanted storage mechanisms will all fall back to the root tenant to find default connection settings if the tenant being used has not defined tenant-specific settings
 * within Marain services, the root tenant is always represented by a special in-memory instance of the `RootTenant` type, whereas all other tenants are managed by the tenancy service

 That third item is there to support the second: because each service puts its own `RootTenant` into the DI service collection, as a singleton, it becomes possible for the service to attach whatever service-specific fallback settings it requires. We describe the root tenant as "synthetic" because each service creates its own object to represent the root tenant, whereas all other objects representing tenants are obtained via the `Marain.Tenancy` service, typically through the `ClientTenantProvider`.

 We contemplated separating out the first two concerns (which might enable us not to need the third characteristic above) because it has been a source of confusion in the past. However, for the time being we are planning to keep it this way because that alternative approach would require us to introduce an extra mechanism to support these kinds of defaults.


## Consequences

The advantage of having a synthetic `RootTenant` that the service can configure as it requires is that it becomes possible for services relying on tenanted storage to have their storage settings overridden at the per-tenant level, but to be able to pick up service-defined defaults in cases where the tenant does not wish to bring its own storage. This comes for free as a result of using the tenancy mechanism to store these settings. Without the synthetic root, we would need to introduce additional mechanisms to enable service-specific fallbacks.

A downside of this is that it's not currently possible to define global default storage settings that automatically apply to any service that does not choose to define service-specific ones. That's because we cannot usefully define any global properties on the root tenant: with a synthetic root tenant the expectation is that clients will never fetch the root from the tenancy service in any case. (We do in fact allow it to be fetched but the root tenant is special-cased: we return a dummy object so as not to expose the tenancy service's own service-local root tenant settings. And we block any attempts to modify the root tenant.)
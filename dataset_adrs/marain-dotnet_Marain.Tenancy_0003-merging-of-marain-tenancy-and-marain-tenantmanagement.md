# Merging of Marain.Tenancy and Marain.TenantManagement

## Status

Approved

## Context

The original build of `Marain.Tenancy` provided two main things:
- It provided an API over the existing `Corvus.Tenancy` project, allowing us to build multiple services around the same tenancy system without each service needing to be aware of the underlying persistence mechanism for tenants.
- It provided a drop in replacement for direct use of the `Corvus.Tenancy.Abstractions.ITenantProvider`, in the form of the `ClientTenantProvider` in `Marain.Tenancy.ClientTenantProvider`.

However, the service did not impose any particular tenancy model on consumers; it simply exposed the capabilities of the `Corvus.Tenancy` library.

Subsequently, as the functionality of the remaining Marain services was extended to properly support multi-tenancy, it became necessary to define the tenancy model that would be shared across all Marain Services. This is documented in `Marain.Instance` ADRs [0005 - Multitenancy approach for Marain](https://github.com/marain-dotnet/Marain.Instance/blob/master/docs/adr/0005-multitenancy-approach-for-marain.md) and [0006 - Process for onboarding new tenants and enrolling them to use Marain services](https://github.com/marain-dotnet/Marain.Instance/blob/master/docs/adr/0006-process-for-onboarding-new-tenants.md)

The additional code required to support this, available in [the `Marain.TenantManagment` repository](https://github.com/marain-dotnet/Marain.TenantManagement) was built as a wrapper around the existing `Marain.Tenancy` API and is currently only exposed via a Command Line Interface.

This has worked reasonably well to date; the CLI and code provided by Marain.TenantManagement is in use in multiple locations to work with tenants in several different ways, but all based on the underlying model defined in the ADRs linked to above.

However, it has become apparent that in Marain, the two are essentially inseperable. All Marain services (bar Marain.Tenancy) validate requests to ensure that the tenant making the request is enrolled to use the service being called, which requires use of code referenced from `Marain.TenantManagement` and `Marain.Tenancy`.

In addition, new requirements (such as the need for a service to be able to obtain a list of enrolled clients) are difficult to implement efficiently without further blurring the lines between the two libraries.

This has brought into focus the fact that `Marain.Tenancy` is something of an outlier in the Marain world; despite being the service used to manage Marain tenants, it is the only service in the Marain ecosystem that does not fully "buy in" to the Marain tenancy model. This means that as we expand the model to cover new scenarios (including the creation of additional tenant management tooling to simplify onboarding and offboarding, and potentially begin to integrate billing, metering, and so on) we will likely end up either continuing to add extensions to the `Marain.TenantManagement` library, or adding a separate API that acts as a wrapper around `Marain.Tenancy`.

## Decision

To simplify our approach, we will modify `Marain.Tenancy` so that that API it exposes reflects the tenancy model used by the Marain ecosystem. This means that existing functionality provided by the `Marain.TenantManagement` extensions will become API endpoints - e.g. enrollment, client/service tenant creation, etc.

The existing CLIs provided with `Marain.TenantManagement` and `Marain.Tenancy` will be merged and separated out into their own project. They will then form the basis of CLI tooling required for standard tasks in all Marain services. As well as making the tooling simpler to use (by having all functionality available through one tool rather than spread across multiple), this will ensure we maintain good practice in ensuring that all of these tasks can be carried out via their relevant APIs.

## Consequences

### Updates will be required to all Marain services

Since all services use Marain.Tenancy, both to retrieve tenants invoking their endpoints and validate their enrolment status, it is likely that all of these services will require some level of change. To ease the transition, we can leave existing endpoints in place, marked as deprecated when required and remove them in a future release. This will allow us to migrate other Marain services to use new endpoints in a more controlled manner.

### Updates will be required to Marain.Instance

The change to a different CLI tool will require updates to Marain.Instance to use the new tool for service registration.

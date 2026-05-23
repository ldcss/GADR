# Process for onboarding new tenants and enrolling them to use Marain services

## Status

Proposed

## Context

We have defined (in [ADR 0005](0005-multitenancy-approach-for-marain.md)) the way in which we intend to implement Tenancy in Marain instances using the `Marain.Tenancy` service. As noted in that ADR, managing the desired model by hand would be excessively error prone and as such, we need to design tooling that will allow us to create and manage new tenants, and to allow them to use the Marain services they are licenced for.

Before we can build that tooling we need to design the underlying process by which tenant onboarding, enrollment and offboarding will work. This needs to allow new Client Tenants to be onboarded into Marain services without tightly coupling the services so some central thing that knows everything about them.

## Decision

We are envisaging a central control-plane API (referred to for the remainder of this document as the "Management API") for Marain which primarily builds on top of the Tenancy service. This will provide the standard operations such as creating new tenants and enrolling them to use Marain services.

It will also need to allow us to manage concerns such as licensing, billing, metering and so on, but these are out of the scope of this ADR and will be covered by additional ADRs, work items and documentation when required.

### Onboarding

Onboarding is a relatively simple part of the process where we create a new Tenant for the client. We will need to determine how we intend licensing to work and what part, if any, the Management API plays.

### Enrollment

Service enrollment is a more interesting aspect of the process. In order to avoid tightly coupling Marain services to the Management API, we need two things:
- A means of discovering the available services.
- A means of determining the configuration that's needed to enroll for a service, receiving and attaching that configuration to tenants being enrolled, and a defined way of creating the required sub-tenants for services to use when making calls to dependent services on behalf of clients.

As described in [ADR 0005](0005-multitenancy-approach-for-marain.md), we are envisaging that each service has a Tenant created for it, under a single parent for all Service Tenants. These tenants can then underpin the discovery mechanism that allows the management API to enumerate services that tenants can be enrolled into.

Once we have provided a discovery mechanism, we need to define a way in which we can gather the necessary information needed to enroll a tenant to use a service. We are intending to make this work by defining a common schema through which a service can communicate both the configuration it requires as well as the services upon which it depends. Services can then attach a manifest file containing this information to their Service Tenant via a well known property key, allowing the Management API to obtain the manifest as part of the discovery process.

Since the process of enrollment and unenrollment is standard across tenants, the actual implementation of this can form part of the Management API, driven by the data in the manifests. If we ever encounter a situation where services need to perform non-standard actions as part of tenant enrollment, we can extend the process to support a way in which services can be notified of new enrollments - this could be a simple callback URL, or potentially a broadcast-type system using something like Azure Event Grid. Since we don't yet have any services that would need this, we will not attempt to define that mechanism at this time.

Enrolling a tenant to use a service does two things:
- Firstly, it will attach the relevant configuration for the service to the tenant that's being enrolled.
- Secondly, if the service that's being enrolled in has dependencies on other services, it will create a new sub-tenant of the Service Tenant for the service being enrolled that the service will use when accessing dependencies on behalf of the client. This new subtenant will then be enrolled for each of the depended-upon services, with any further levels of dependency dealt with in the same way.

### Example

Consider a scenario when we have two clients and three services:

```
Root tenant
 |
 +-> Client Tenants
 |     |
 |     +-> Contoso
 |     |
 |     +-> Litware
 |     
 +-> Service Tenants
       |
       +-> WORKFLOW
       |
       +-> OPERATIONS
       |
       +-> FOOBAR
```

The dependency tree for the services looks like this:


```
                          +------------+
                          |            |
                  +-------> WORKFLOW   +------+-----------------+
+---------+       |       |            |      |                 |
|         +-------+       +-^----------+      |                 |
| Contoso |                 |                 |                 |
|         |                 |                 |                 |
+----+----+                 |           +-----v------+          |
     |                      |           |            |          |
     |                      |     +-----> OPERATIONS +----+     |
     |      +---------+     |     |     |            |    |     |
     |      |         +-----+     |     +------------+    |     |
     |      | Litware |           |                       |     |
     |      |         +-----------+                       |     |
     |      +---------+                               +---v-----v--+
     |                                                |            |
     +------------------------------------------------> FOOBAR     |
                                                      |            |
                                                      +------------+
```

As can be seen from this diagram:
- Contoso is licenced to use WORKFLOW and FOOBAR
- Litware is licenced to use WORKFLOW and OPERATIONS
- WORKFLOW has dependencies on OPERATIONS and FOOBAR
- OPERATIONS has a dependency on FOOBAR

Let's assume that each of the three services require storage configuration, and have a look at what happens when Litware is enrolled to use Workflow.

Firstly, we will use the manifest attached to the Workflow Service Tenant to obtain the list of required configuration to enroll a tenant for use with Workflow. The Workflow manifest states that Workflow requires CosmosDB storage configuration, and also that it is dependent on Operations and FooBar. We can then use the manifests on the Operations and FooBar Service Tenants to determine what configuration is required for them. Operations is dependent on FooBar, so the process is repeated there. From this process, we can determine that the list of required configuration for Workflow is the sum of four things: Workflow storage config, Operations storage config, FooBar storage config when invoked from Workflow, and FooBar storage config when invoked from Operations.

Then, we will assemble this information (most likely via a Marain "management UI") and begin the process of enrollment. First we enroll the Litware tenant to use workflow by attaching the workflow storage configuration to the Litware tenant. Then, because Workflow has dependencies, we create a sub-tenant of the Workflow Service Tenant that will be used to call these dependencies on behalf of Litware and we attach the ID of the new tenant to the Litware tenant using a well known property name specific to Workflow:

```
Root tenant
 |
 +-> Client Tenants
 |     |
 |     +-> Contoso
 |     |
 |     +-> Litware
 |           +-> (Workflow storage configuration)
 |           +-> (The Id of the WORKFLOW+Litware sub-tenant for the Workflow service to use)
 |       
 +-> Service Tenants
       |
       +-> WORKFLOW
       |     |
       |     +-> WORKFLOW+Litware
       |
       +-> OPERATIONS
       |
       +-> FOOBAR
```

Next, we need to enroll the new WORKFLOW+Litware tenant with the Operations and FooBar services.

We start with Operations, which repeats the process we have just carried out for Litware and Workflow, resulting in a similar outcome: the WORKFLOW+Litware tenant has configuration attached to it for the Operations service, and the dependency of Operations on FooBar results in a sub tenant being created for Operations to use when calling FooBar on behalf of WORKFLOW+Litware, with the ID of the new tenant being attached to WORKFLOW+Litware using an Operations-specific well-known key:

```
Root tenant
 |
 +-> Client Tenants
 |     |
 |     +-> Contoso
 |     |
 |     +-> Litware
 |           +-> (Workflow storage configuration)
 |           +-> (The Id of the WORKFLOW+Litware sub-tenant for the Workflow service to use)
 |
 +-> Service Tenants
       |
       +-> WORKFLOW
       |     |
       |     +-> WORKFLOW+Litware
       |           +-> (Operations storage configuration)
       |           +-> (The Id of the OPERATIONS+WORKFLOW+Litware sub-tenant for the Operations service to use)
       |
       +-> OPERATIONS
       |     |
       |     +-> OPERATIONS+WORKFLOW+Litware
       |
       +-> FOOBAR
```

Next, the new OPERATIONS+WORKFLOW+Litware tenant is enrolled for the FooBar service. The FooBar service has no dependencies so we do not need to create any further tenants; we simply attach the storage configuration for FooBar to the tenant being enrolled and returns. This also completes the WORKFLOW+Litware tenant's enrollment for Operations.

```
Root tenant
 |
 +-> Client Tenants
 |     |
 |     +-> Contoso
 |     |
 |     +-> Litware
 |           +-> (Workflow storage configuration)
 |           +-> (The Id of the WORKFLOW+Litware sub-tenant for the Workflow service to use)
 |
 +-> Service Tenants
       |
       +-> WORKFLOW
       |     |
       |     +-> WORKFLOW+Litware
       |           +-> (Operations storage configuration)
       |           +-> (The Id of the OPERATIONS+WORKFLOW+Litware sub-tenant for the Operations service to use)
       |
       +-> OPERATIONS
       |     |
       |     +-> OPERATIONS+WORKFLOW+Litware
       |           +-> (FooBar storage configuration)
       |
       +-> FOOBAR
```

Next, we continue the Workflow enrollment for the Litware tenant by enrolling the new WORKFLOW+Litware tenant for Workflow's other dependency, FooBar. As with the Operations service enrolling OPERATIONS+WORKFLOW+Litware with FooBar, this does not result in any further tenants being created, just the FooBar config being attached to WORKFLOW+Litware:

```
Root tenant
 |
 +-> Client Tenants
 |     |
 |     +-> Contoso
 |     |
 |     +-> Litware
 |           +-> (Workflow storage configuration)
 |           +-> (The Id of the WORKFLOW+Litware sub-tenant for the Workflow service to use)
 |
 +-> Service Tenants
       |
       +-> WORKFLOW
       |     |
       |     +-> WORKFLOW+Litware
       |           +-> (Operations storage configuration)
       |           +-> (The Id of the OPERATIONS+WORKFLOW+Litware sub-tenant for the Operations service to use)
       |           +-> (FooBar storage configuration)
       |
       +-> OPERATIONS
       |     |
       |     +-> OPERATIONS+WORKFLOW+Litware
       |           +-> (FooBar storage configuration)
       |
       +-> FOOBAR
```

This completes Litware's enrollment for the Workflow service. As can be seen, this has resulted in multiple service-specific Litware tenants being created but Litware is never explicitly made aware of the existence of these tenants, nor is it able to use them directly. They are used by their parent services to make calls to their dependencies _on behalf_ of the Litware tenant.

However, there is a further step: Litware also needs to be enrolled in the Operations service. At present, Workflow is able to use Operations on Litware's behalf using the WORKFLOW+Litware tenant. However, this is an implementation detail of Workflow and something that should be able to change without impacting Litware - as long as it does not result in a change to the public Workflow API. So, in order to allow Litware to use the Operations service directly, the process we went through for Workflow is repeated. The storage configuration for Operations is attached to the Litware tenant, and then a further sub-tenant of Operations will be created for it to use when accessing FooBar on behalf of Litware:

```
Root tenant
 |
 +-> Client Tenants
 |     |
 |     +-> Contoso
 |     |
 |     +-> Litware
 |           +-> (Workflow storage configuration)
 |           +-> (The Id of the WORKFLOW+Litware sub-tenant for the Workflow service to use)
 |           +-> (Operations storage configuration)
 |           +-> (The Id of the OPERATIONS+Litware sub-tenant for the Operations service to use)
 |
 +-> Service Tenants
       |
       +-> WORKFLOW
       |     |
       |     +-> WORKFLOW+Litware
       |           +-> (Operations storage configuration)
       |           +-> (The Id of the OPERATIONS+WORKFLOW+Litware sub-tenant for the Operations service to use)
       |           +-> (FooBar storage configuration)
       |
       +-> OPERATIONS
       |     |
       |     +-> OPERATIONS+WORKFLOW+Litware
       |     |     +-> (FooBar storage configuration)
       |     |
       |     +-> OPERATIONS+Litware
       |
       +-> FOOBAR
```

Then, the new OPERATIONS+Litware tenant will be enrolled for the FooBar service, which results in FooBar storage configuration being attached to the OPERATIONS+Litware service:

```
Root tenant
 |
 +-> Client Tenants
 |     |
 |     +-> Contoso
 |     |
 |     +-> Litware
 |           +-> (Workflow storage configuration)
 |           +-> (The Id of the WORKFLOW+Litware sub-tenant for the Workflow service to use)
 |           +-> (Operations storage configuration)
 |           +-> (The Id of the OPERATIONS+Litware sub-tenant for the Operations service to use)
 |
 +-> Service Tenants
       |
       +-> WORKFLOW
       |     |
       |     +-> WORKFLOW+Litware
       |           +-> (Operations storage configuration)
       |           +-> (The Id of the OPERATIONS+WORKFLOW+Litware sub-tenant for the Operations service to use)
       |           +-> (FooBar storage configuration)
       |
       +-> OPERATIONS
       |     |
       |     +-> OPERATIONS+WORKFLOW+Litware
       |     |     +-> (FooBar storage configuration)
       |     |
       |     +-> OPERATIONS+Litware
       |           +-> (FooBar storage configuration)
       |
       +-> FOOBAR
```

This completes the enrollment of Litware to the Workflow and Operations services. As can be seen from the above, there are three different paths through which Litware makes indirect use of the FooBar service, and it's possible for the client to use separate storage for each. In fact, this will be the default; even if the client is using Marain storage, the data for their three different usage scenarios for FooBar will be stored in different containers.

It should be noted that the client does not get to configure these new sub-tenants directly. In fact, they will be unaware of them - they are essentially implementation details of our approach to multi-tenancy in Marain. They will not be able to retrieve the sub-tenants from the tenancy service or update them directly. That said, it's likely that the management API will allow the configuration to be changed - but without exposing the fact that these sub-tenants exist.

### Default configuration

Whilst we want to allow users to "bring their own storage" for the Marain services, this may not be the most likely scenario. There are effectively four main ways in which Marain can be used:
- Fully hosted, using the default storage for each service (this storage is deployed alongside the service)
- Fully hosted, using managed but non-standard storage (we deploy separate storage accounts per client)
- Hosted, but using client-provided storage (the "bring your own storage" model)
- Self-hosted (i.e. deployed into a client's own Azure subscription), in which case we would expect the storage deployed with the service to be used - essentially the same as the fully hosted option.

In order to make the first and last options simpler to use, we will make the configuration for the default storage available to the enrollment process so it can simply be copied to tenants as they are enrolled, rather than requiring it to be explicitly stated for every enrollment. As such, we need the manifest file schema to allow marking configuration as optional, indicating that defaults should be used if that configuration is not provided. The most sensible location to store this default configuration is on the Service Tenant itself.

### Offboarding

Offboarding needs to be considered further; there are many questions about what happens to client data if they stop using Marain, and these will likely depend on the licensing agreements we put in place. As a result this will be considered at a later date.

## Consequences

Whilst this ADR addresses how tenants are created and configured as part of enrollment, it does not yet cover how they are updated should a new version of a service be deployed that requires different configuration. In this scenario, all tenants that used that service would potentially need to be updated with the new configuration. This may be dealt with by versioning, requiring each tenant to be enrolled for a specific version of each service (with a separate Service Tenant existing for each version of a service). This would require us to take a side-by-side approach to versioning in Marain, but would likely make it much more straightforward to deploy updates and move tenants onto new versions. As such, we are deferring further work on this until we have a better answer to the question of versioning.


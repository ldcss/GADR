# Multitenancy approach for Marain

## Status

Accepted

## Context

Tenancy has always been a first class citizen of all Marain services, however this by itself is not enough to make the system truly multitenanted. In order to do this, we need to determine how tenants should be created, managed and used within the Marain "world".

We would like the option of deploying Marain as either a managed service, hosted by us and licenced to users as a PaaS offering, or for clients to deploy private instances into their own cloud subscriptions. We also want to give clients of the managed services the option for data to be stored in their own storage accounts or databases, but still have us run the compute aspects of the platform on their behalf. This also extends to those clients who are using Marain to implement their own multi-tenanted services: these clients should also be able to isolate their own clients' storage.

In addition, we need to be able to differentiate between a Marain service being available for a client to use directly and one being used as a dependency of a service they are using. For example, the Workflow service makes use of the Operations service. As a result, clients that are licenced to use the Workflow service will be using the Operations service indirectly, despite the fact that they may not be licenced to use it directly.

We need to define a tenancy model that will support these scenarios and can be implemented using the `Marain.Tenancy` service.

## Decision

To support this, we have made the following decisions

1. Every client using a Marain instance will have a Marain tenant created for them. For the remainder of this document, these will be referred to as "Client Tenants".
1. Every Marain service will also have a Marain tenant created for it. For the remainder of this document, these will be referred to as "Service Tenants".
1. We will make use of the tenant hierarchy to group Client Tenants and Service Tenants under their own top-level parent. This means that we will have a top-level tenant called "Client Tenants" which parents all of the Client Tenants, and an equivalent one called "Service Tenants" that parents the Service Tenants (this is shown in the diagram below).
1. Clients will access the Marain services they are licenced for using their own tenant Id. Whilst the Marain services themselves expect this to be supplied as part of endpoint paths, there is nothing to prevent an API Gateway (e.g. Azure API Management) being put in front of this so that custom URLs can be mapped to tenants, or so that tenant IDs can be passed in headers.
1. When a Marain service depends on another one as part of an operation, it will pass the Id of a tenant that is a subtenant of it's own Service Tenant. This subtenant will be specific to the client that is making the original call. For example, the Workflow service has a dependency on the Operations Control service. If there are two Client Tenants for the Workflow Service, each will have a corresponding sub-tenant of the Workflow Service Tenant and these will be used to make the call to the Operation service. This approach allows the depended-upon service to be used on behalf of the client without making it available for direct usage.

Each of these tenants - Client, Service, and the client-specific sub-tenants of the Service Tenants - will need to hold configuration appropriate for their expected use cases. This will normally be any required storage configuration for the services they use, plus the Ids of any subtenants that have been created for them in those services, but could also include other things.

As an example, suppose we have two customers; Contoso and Litware. For these customers to be able to use Marain, we must create Contoso and Litware tenants. We also have two Marain services available, Workflow and Operations. These also have tenants created for them (in the following diagrams, Service Tenants are shown in ALL CAPS and Client Tenants in normal sentence case. Service-specific client subtenants use a mix to indicate what they relate to):

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
```

Contoso is licenced to use Workflow, and Litware is licenced to use both Workflow and Operations. This means that:
- The Contoso tenant will contain storage configuration for the Workflow service (as with all this configuration, the onboarding process will default this to standard Marain storage, where data is siloed by tenant in shared storage accounts - e.g. a single Cosmos database containing a collection per tenant. However, clients can supply their own storage configuration where required).
- The Litware tenant will contain storage configuration for both Workflow and Operations services, because it uses both directly.

In addition, because both clients are licenced for workflow, they will each have a sub-tenant of the Workflow Service Tenant, containing the storage configuration that should be used with the Operations service. The Operations service does not have any sub-tenants because it does not have dependencies on any other Marain services:

```
Root tenant
 |
 +-> Client Tenants
 |     |
 |     +-> Contoso
 |     |     +-> (Workflow storage configuration)
 |     |     +-> (The Id of the WORKFLOW+Contoso sub-tenant for the Workflow service to use)
 |     |
 |     +-> Litware
 |           +-> (Workflow storage configuration)
 |           +-> (The Id of the WORKFLOW+Litware sub-tenant for the Workflow service to use)
 |           +-> (Operations storage configuration)
 |
 +-> Service Tenants
       |
       +-> WORKFLOW
       |     |
       |     +-> WORKFLOW+Contoso
       |     |     +-> (Operations storage configuration)
       |     |
       |     +-> WORKFLOW+Litware
       |           +-> (Operations storage configuration)
       |
       +-> OPERATIONS
```

As can be seen from the above, each tenant holds appropriate configuration for the services they use directly. In the case of the Client Tenants, they also hold the Id of the sub-tenant that the Workflow service will use when calling out to the Operations service on their behalf; this is necessary to avoid a costly search for the correct sub-tenant to use.

You will notice from the above that Litware ends up with two sets of configuration for Operations storage; that which is employed when using the Operations service directly, and that used when calling the Workflow service and thus using the Operations service indirectly. This gives clients the maximum flexibility in controlling where their data is stored.

Now let's look at a slightly more complex example. Imagine in the scenario above, there is a third service, which we'll just call the FooBar service, and that both the Workflow and Operations service are dependent on it. In addition, Contoso are licenced to use it directly. This is what the dependency graph now looks like:

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

In order to support this, we start with an additional Service Tenant for the FooBar tenant.

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

We then enroll Contoso to use the Workflow service. This causes a chain of enrollments whereby a sub-tenant is created for WORKFLOW+Contoso, which is then enrolled to use the Operations service, creating a sub-tenant of OPERATIONS, OPERATIONS+WORKFLOW+Contoso, which is then enrolled to use the FooBar service (since FooBar does not have dependencies, this does not create any further sub tenants). The Workflow service is also directly dependent on FooBar, so WORKFLOW+Contoso is also enrolled to use FooBar resulting in storage configuration for FooBar being added to it.

This leaves the tenant hierarchy looking like this:

```
Root tenant
 |
 +-> Client Tenants
 |     |
 |     +-> Contoso
 |     |     +-> (Workflow storage configuration)
 |     |     +-> (The Id of the WORKFLOW+Contoso sub-tenant for the Workflow service to use)
 |     |
 |     +-> Litware
 |      
 +-> Service Tenants
       |
       +-> WORKFLOW
       |     |
       |     +-> WORKFLOW+Contoso
       |           +-> (Operations storage configuration)
       |           +-> (The Id of the OPERATIONS+WORKFLOW+Contoso sub-tenant for the Operations service to use)
       |           +-> (FooBar storage configuration)
       |
       +-> OPERATIONS
       |     |
       |     +-> OPERATIONS+WORKFLOW+Contoso
       |           +-> (FooBar storage configuration)
       |
       +-> FOOBAR
```

We then enroll Contoso for the FooBar service. Since there are no additional dependencies, this does not result in any further sub-tenants being created, but does add storage configuration for FooBar to the Contoso tenant. As in the first example, Contoso now has two sets of storage configuration for the FooBar service, one for direct use and one for indirect use.

```
Root tenant
 |
 +-> Client Tenants
 |     |
 |     +-> Contoso
 |     |     +-> (Workflow storage configuration)
 |     |     +-> (The Id of the WORKFLOW+Contoso sub-tenant for the Workflow service to use)
 |     |     +-> (FooBar storage configuration)
 |     |
 |     +-> Litware
 |      
 +-> Service Tenants
       |
       +-> WORKFLOW
       |     |
       |     +-> WORKFLOW+Contoso
       |           +-> (Operations storage configuration)
       |           +-> (The Id of the OPERATIONS+WORKFLOW+Contoso sub-tenant for the Operations service to use)
       |           +-> (FooBar storage configuration)
       |
       +-> OPERATIONS
       |     |
       |     +-> OPERATIONS+WORKFLOW+Contoso
       |           +-> (FooBar storage configuration)
       |
       +-> FOOBAR
```

We now repeat the process of enrolling Litware for the Workflow service:

```
Root tenant
 |
 +-> Client Tenants
 |     |
 |     +-> Contoso
 |     |     +-> (Workflow storage configuration)
 |     |     +-> (The Id of the WORKFLOW+Contoso sub-tenant for the Workflow service to use)
 |     |     +-> (FooBar storage configuration)
 |     |
 |     +-> Litware
 |           +-> (Workflow storage configuration)
 |           +-> (The Id of the WORKFLOW+Litware sub-tenant for the Workflow service to use)
 |      
 +-> Service Tenants
       |
       +-> WORKFLOW
       |     |
       |     +-> WORKFLOW+Contoso
       |     |     +-> (Operations storage configuration)
       |     |     +-> (The Id of the OPERATIONS+WORKFLOW+Contoso sub-tenant for the Operations service to use)
       |     |     +-> (FooBar storage configuration)
       |     |
       |     +-> WORKFLOW+Litware
       |           +-> (Operations storage configuration)
       |           +-> (The Id of the OPERATIONS+WORKFLOW+Litware sub-tenant for the Operations service to use)
       |           +-> (FooBar storage configuration)
       |
       +-> OPERATIONS
       |     |
       |     +-> OPERATIONS+WORKFLOW+Contoso
       |     |     +-> (FooBar storage configuration)
       |     |
       |     +-> OPERATIONS+WORKFLOW+Litware
       |           +-> (FooBar storage configuration)
       |
       +-> FOOBAR
```

Since Litware is not licenced to use FooBar, the Litware Client Tenant does not hold any configuration for that service itself.

Finally, we enroll Litware to use the Operations service. In this example, because Operations depends on FooBar, we need to create another sub-tenant of Operations to call FooBar with when Litware uses Operations directly, and enroll this new subtenant with FooBar. This leaves us with the following:

```
Root tenant
 |
 +-> Client Tenants
 |     |
 |     +-> Contoso
 |     |     +-> (Workflow storage configuration)
 |     |     +-> (The Id of the WORKFLOW+Contoso sub-tenant for the Workflow service to use)
 |     |     +-> (FooBar storage configuration)
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
       |     +-> WORKFLOW+Contoso
       |     |     +-> (Operations storage configuration)
       |     |     +-> (The Id of the OPERATIONS+WORKFLOW+Contoso sub-tenant for the Operations service to use)
       |     |     +-> (FooBar storage configuration)
       |     |
       |     +-> WORKFLOW+Litware
       |           +-> (Operations storage configuration)
       |           +-> (The Id of the OPERATIONS+WORKFLOW+Litware sub-tenant for the Operations service to use)
       |           +-> (FooBar storage configuration)
       |
       +-> OPERATIONS
       |     |
       |     +-> OPERATIONS+WORKFLOW+Contoso
       |     |     +-> (FooBar storage configuration)
       |     |
       |     +-> OPERATIONS+WORKFLOW+Litware
       |     |     +-> (FooBar storage configuration)
       |     |
       |     +-> OPERATIONS+Litware
       |           +-> (FooBar storage configuration)
       |
       +-> FOOBAR
```

## Consequences

It is expected that these sub-tenants are created and configured as part of a process of enrolling tenants for specific services they are licenced to use. The means by which this is expected to happen is covered in [ADR 0006](0006-process-for-onboarding-new-tenants.md).

Without appropriate tooling, managing the necessary tenants and their configuration would be complex and error-prone. At a minimum, it will be necessary to script some basic processes to assist in setting this process up. It will also be necessary to ensure that an appropriate level of logging is in place in code that reads this configuration in order to allow setup problems to be quickly diagnosed.

Moving a lot of the service configuration into tenants means that we will also need to produce tooling to set up Service Tenants and their default configurations as part of the deployment process. This will take the place of existing deployment processes that use ARM templates to add configuration directly to the host functions applications.
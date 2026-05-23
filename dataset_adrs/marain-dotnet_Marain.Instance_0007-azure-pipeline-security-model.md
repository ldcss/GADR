# Azure pipeline security model

## Status

Proposed


## Context

This ADR defines an approach for a pipeline security management process.  Itt enables application deployment pipelines to perform all tasks associated with the deployment of typical Azure PaaS-based solutions, in a way that adheres to the principle of least privilege and supports oversight and audit requirements.

Importantly, the process for making such security changes utilises a standard development workflow that allows teams to manage their own configuration with minimal friction, whilst still facilitating centralised oversight when needed (e.g. by the security team).

Before describing the process in detail, here are the sorts of tasks that an application deployment pipeline typically needs to be able to perform:

1. Create resources in the target subscription
1. Perform ARM role assignments in the target subscription
1. Query Azure Active Directory (AAD) for existing applications & service principals
1. Create new AAD applications & service principals
1. Manage those AAD applications & service principals (e.g. application role assignment, deletion etc.)

Let's start by outlining how these requirements are commonly achieved today.

### Create resources in the target subscription
By default, the 'Service Connections' that Azure Pipelines use to authenticate with Azure already provide this, with the option of constraining its access to a given resource group.

### Perform ARM role assignments in the target subscription
If enabled for automated approaches this is typically achieved by one of the following:
* granting the identity behind the service connection the 'owner' role in the target subscription
* a separate identity with the required permissions, whose credentials are available to pipelines

For manual scenarios:
* raising a service desk ticket
* asking someone who has permissions to do it for you

### Query AAD for existing applications & service principals
The main pipeline is restructured to expect the required information to be provided as manually-maintained configuration.

### Create new AAD applications & service principals
If enabled for automated scenarios, this is commonly handled in one of three ways:
* an entirely separate pipeline running under a different identity which does have the necessary permissions
   * this can only be considered fully-automated if the dependent pipeline is able to trigger this pipeline on-demand
* running a subset of the main pipeline, under a different identity which does have the necessary permissions, such that only the tasks that require the elevated privileges are run

For manual scenarios:
* an out-of-band process whereby an individual with the appropriate permissions executes the necessary steps (either manually or using a script)

### Manage AAD applications & service principals
This is largely equivalent to the preceding 'Create' scenario, with the addition of:
* a dependency on the 'Query AAD' requirement
* having permissions to update applications & principals owned by others (where they were created separately)

>NOTE: All of this functionality may have to run multiple times in the case of an evolving application, particularly where scoping of permissions is being applied.


## Decision

In the context of pipelines running in Azure DevOps, an executing pipeline uses an Azure Resource Manager type of [service connection](https://docs.microsoft.com/en-us/azure/devops/pipelines/library/service-endpoints) to authenticate to Azure for any tasks it needs to perform.

Below is a configuration model that defines the security requirements for each such service connection, which is maintained in a Git repository and has a separate pipeline that applies that configuration in Azure.

>NOTE: These YAML fragments would exist as individual files in the Git repo, with a logical folder structure to help organise and reflect ownership as required (e.g. across development teams, products etc.).

```
---
#
# This fragment maintains the shared configuration that defines the permissions used by
# Azure DevOps service connections managed by this system.
#
azurerm:
  custom_role:
    name: acme-azure-deployer
    allowed_actions:
      - Microsoft.Authorization/roleAssignments/read
      - Microsoft.Authorization/roleAssignments/write
      - Microsoft.Authorization/roleAssignments/delete
  required_roles:
  - contributor
  - acme-azure-deployer
azuread:
  required_graph_permissions:
  - 5778995a-e1bf-45b8-affa-663a9f3f4d04      # readDirDataPermissionId
  - 824c81eb-e3f8-4ee6-8f6d-de7f50d565b7      # manageOwnAppsPermissionId

---
#
# Defines the logical environments used as part of application release promotion and their 
# associated Azure subscription.
#
environments:
- name: dev
  subscription: <subscription-id>
- name: test
  subscription: <subscription-id>
- name: prod
  subscription: <subscription-id>

---
#
# Defines an application/system that deploys resources across 2 resource groups and requires
# service connections for 3 environments
#
name: product_a
environments:
- dev
- test
- prod
resource_groups:
- producta-services                       # NOTE: this option relies on a naming convention-based expansion: e.g. 'acme-<environment>-producta-services-rg'
- acme-${ENVIRONMENT}-producta-data-rg    # NOTE: this option uses a simpler token replacement approach

---
#
# Defines an application/system that deploys resources to a single resource groups and requires
# service connections for 2 environments
#
name: product_b
environments:
- test
- prod
resource_groups:
- acme-${ENVIRONMENT}-productb-rg

```

A security management pipeline, running in Azure DevOps, is able to read this configuration model and performs the following tasks to ensure that a least privilege Azure DevOps service connection is maintained per application, per environment:

* Ensures the required resource groups exist
* Maintains the custom role that grants the elevated permissions and maintains its set of assignable scopes (i.e. the resource groups)
* Maintains the required AAD service principals
* Assigns the specified roles to the AAD service principals with the required resource group scoping constraints
* Assigns the required AAD permissions to the service principals

This pipeline needs to run with high-level permissions, therefore it must be tightly controlled to ensure that its elevated rights are not exploited:
* Use of an Azure DevOps project with no user access outside the responsible team
* The privileged service connection is only available within this restricted project and requires explicit authorisation before it can be used by a new pipeline
* The pipeline only triggers for changes on the `master` branch
* The `master` branch is protected and cannot be directly committed to
* Anyone wishing to make changes to the configuration must raise a Pull Request that is subject to a review/approval policy by at least the responsible team
 

## Consequences

### Positive

#### Development Teams
Development teams benefit from highly autonomous pipelines that fully-support their deployment needs and gives them a familiar way to manage the security requirements as their solutions evolve.

#### Security Teams
Teams responsible for security are released from having to directly support security-sensitive pipeline operations without having to cede control of them.  Instead they have a review & approval responsibility for such security changes and complete operational control of the security management pipeline itself.

The security management pipeline operates on a 'desired state' basis and therefore aims to correct any drift in the security configuration that may have occurred since the last run.

Finally, the version-controlled configuration provides a full audit trail of what pipelines had access to which resources.


### Negative
- Given a large enough security configuration repository, the duration of a single run of the security management pipeline could extend to the point where it becomes a pain point (though parallelisation strategies ought to mitigate this)
- The security management pipeline would become a single point of failure.  In the event that it falls into a broken state, whether through bad configuration data or some other Azure DevOps environmental issue, then development teams would be blocked from creating or updating their service connections
- Deletions and renames made to the security configuration model will require more complex synchronisation logic in the pipeline
- A credential key-rotation policy on the AAD service principals would require the associated Azure DevOps service connection to be kept in-sync, which this approach does not address


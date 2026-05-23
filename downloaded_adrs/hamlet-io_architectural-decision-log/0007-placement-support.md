# Placement Support

* Status: accepted
* Deciders: roleyfoley, rossMurr4y, ml019
* Date: 2021-07-03

## Context and Problem Statement

For some time hamlet has had the idea of a `placement` - a mechanism to dynamically determine where resources should be hosted.

Placements are currently part of the hierarchy of the state tree, and the resource groups within the occurrence structure were intended to allow groups of resources to be placed into different provider accounts.

However to date, a number of limitations and inefficiencies stemming from hamlet's original design has prevented full exploitation of the placement concept;
- the assembly of the solution before the engine is run
- the focus of a template run on a single segment
- the generation of account templates uses different concepts to those of product templates
- the maintenance of critical configuration information such as environment to account mappings external to the cmdb.

The introduction of dynamic cmdb loading and the input pipeline processor with full cmdb qualification presents an opportunity to address these long standing issues and complete the implementation of placement support. The question is how.

## Decision Drivers <!-- optional -->

* reuse existing concepts and ways of doing things as much as possible
* given a cmdb, no other configuration information should be necessary to deploy a product

## Considered Options

This ADR extends on the decision made in [ADR-0002](./0002-layer-deployments.md) - Layer Level Deployments and provides more design detail, primarily by the enrichment of link semantics.

## Decision Outcome

Chosen option: "Extend link semantics", because it addresses the decision drivers best (see below) and aligns with the ADR-0002 decision previously made.

### Positive Consequences <!-- optional -->

* reduced configuration complexity - everything in one place
* better validation of configurations
* links have proven very flexible so expect the proposed changes to be re-purposed for other things in the future
* straightforward transition process once infrastructure in place

### Negative Consequences <!-- optional -->

* Expansion of semantics of existing concepts may be harder to document, understand and explain than dedicated new concepts

## Design Detail

### New Link Semantics

Currently, a link goes from one occurrence in a solution to another _within_ the same solution solution.

This option builds on existing link processing by adding support for a link to target an occurrence in _another_ solution as follows;

1. A link targets an occurrence within a solution.
1. A link consists of two parts;
- those attributes that identify the `District` of a solution
- those attributes that identify an occurrence within the solution.
1. Occurrences within a solution are identified by a standard set of link attributes
     - `Tier`
     - `Component`
     - `Subcomponent`
     - `Instance`
     - `Version`

   Thus these attributes must be present on a link, or be inherited from the occurrence on which the link is configured.
1. The `Subcomponent` attribute replaces use of type specific attributes such as `Port`.
1. An optional `Type` attribute is added to ensure links to same named subcomponents can be resolved. Its value is the desired component type of the link target. A side effect of this is that for any link, the `Type` attribute can be added to document an expectation of the type of the intended target allowing misconfigured links to be identified in some cases.
3. `District types` will be configured via a `districttypes` plugin directory, with each directory having an `id.ftl` file to define the district type.
4. Each `DistrictType` has a name and defines an ordered set of layers used to identify the `District` of a solution. In turn, the input filter attribute associated with each layer is used as the attribute in the link used to identify the layer within a district.
5. In order to resolve a link, the desired district must be known, and a value for each of the layers identifying the district of a solution must be known.
6. To identify the district, a link must have a `DistrictType` attribute whose value matches the name of one of the known districts. It has a default value of `self` which means the link will use the district type associated with the solution from which the link originates.
7. As an initial implementation, the following district types will be defined in the shared provider with the indicated layer ordering;
    - `segment` = `Product`, `Environment`, `Segment`
    - `account` = `Account`
    - `tenant` = `Tenant`
8. In the same way that a link can inherit occurrence identifiers from the source component, it inherits layer identifiers from the source solution.
9. Link indirection is supported by an optional `LinkRef` attribute within a link object. If present, other link attributes will be merged into the resolved link with the resolved link taking precedence. This permits the user of the `linkRef` to still control attributes such as `IncludeInContext`.
10. `LinkRef` resolution is recursive so, a `LinkRef` can resolve to a link containing a `LinkRef` attribute.
11. The value of a LinkRef attribute is used as the attribute name in a `LinkRefs` configuration object, with the attribute value
being the desired link definition.
1. `LinkRef` definitions can be provided via a `LinkRefs` attribute within a blueprint, or via the `Solution`, `Product` and `Tenant` layer configurations. The effective target link is generated by merging matches in the same order, permitting partial definitions at different layers, with usual precedence order applying.
1. As with any other blueprint configuration, modules can inject `LinkRef` definitions into the blueprint but not override any layer based definitions.
1. LinkRef attributes provide a convenient mechanism to centralise qualification of links shared across multiple components, as is commonly the case with placements.

### New Components

This option also introduces two new components - `Subscription` and `HostingPlatform`.

#### Subscription

A `Subscription` component represents a provider specific mechanism for purchasing hosting capability, such as an `account` with AWS or a `subscription` with Azure. 

The "external" namespace is used to flag attributes involved in the importing of any component. The `Subscription` component supports importation of the identifier for the provider, as well as the provider specific identifier for the `Subscription` and the deployment framework to be used by default.

`Subscription` components will typically be used with a `tenant` district type solution. They can also use the component location information (see below) to connect to another `Subscription`. The example of this is a master account in AWS.

The `Subscription` component supports the importing of externally created subscriptions as well as creation via hamlet. Mixed usage is expected to be common, e.g. a master account for AWS is created externally with all subsequent accounts then being created via `Subscription` components.

#### HostingPlatform

A `HostingPlatform` component represents a place within a subscription where resources can physically be deployed.

The `Engine` attribute of the `HostingPlatform` determines what type of hosting is provided. Initially, an engine value of `region` will permit placement of resources within a region of a `Subscription`.

HostingPlatform components will typically be used within an `account` district type solution. For an engine type of `region`, a region value must be provided.

The `HostingPlatform` component relies on the component location information (see below) to provide details of the associated `Subscription`. Thus at least one `Subscription` must be defined in order to use the `HostingPlatform` component.

As an example of usage, for AWS or Azure it would be normal to see this component in each `account` district type solution, with instances for each region that is active in the account. It is also likely that other components within an `account` district type solution, such as registries, would also link to this component in order to establish where account solution resources should be deployed. So when deploying an S3 based registry, a region would need to be provided as a command line option to select the desired template to generate, with the HostingPlatform then being used to determine if a given registry should be included (see below on ResourceGroup placement).

### Locations Occurrence Attribute

All component solutions will now support a `deployment:Locations` attribute, the purpose of which is to provide the mechanism for a component to document its requirements for information related to the placement of other components.

Each location is represented as a key within the `deployment:Locations` attribute, with each key having a **mandatory** `Link` attribute.

Locations will be included in the metadata of resourcegroups when defining a component type, and will specify if the location is mandatory or optional, and what component types can be targetted by the link. This will permit Location information to be checked for completeness.

Being an occurrence attribute, the `deployment:Locations` attribute can be populated directly on a component for maximum granularity, but equally be configured via `DeploymentProfiles`, and enforced via `PolicyProfiles`. These also give the ability for the locations to be varied based on component type, for example to select different registries.

In general, it is expected that a LinkRef will be used for location links to centralise any qualifications, for example differentiation between non-production and production environment placements.

### ResourceGroup placement
Placement of a resource group will be done by way of a location with the same name as the resource group. The target of the location will reflect information needed by the component implementation. A common example will be a link to a region based `HostingPlatform` occurrence. In this case, the occurrence will be expected to offer `PROVIDER`, `ACCOUNT`, `REGION` and `DEPLOYMENT_FRAMEWORK` attributes.

### Other Location Uses

Over time, other uses of locations are expected, such as the selection of registries from which code should be sourced.

The current baseline and network processing could also be merged into location processing, perhaps with predefined values of `_baseline` and `_network` or with a standard set of `_` based linkRefs being offered by each. A component requiring these would still need to declare them for validation and documentation purposes.

### Assessment

* Good, because it reuses existing concepts (layers, district types, solutions)
* Good, because it improves documentation of dependency requirements between components
* Good, because placement information is contained within the CMDB
* Bad, because a degree of expertise in deployment profiles (a more advanced fature) is required for more advanced use cases.

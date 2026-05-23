# 52. ODRL policy

Date: 2020-09-21

## Status

Accepted

Implements [4. Create software defined everything](0004-create-software-defined-everything.md)

Implements [12. Data catalog specifies all data components](0012-data-catalog-specifies-all-data-components.md)

Implemented by [53. Project company data](0053-project-company-data.md)

## Context

Permissions on objects have to be specified in a clear and specific way. The [Open Digital Rights Language (ODRL)](https://www.w3.org/TR/odrl-model/) is a policy expression language that provides a flexible and interoperable information model, vocabulary, and encoding mechanisms for representing statements about the usage of content and services. The ODRL Information Model describes the underlying concepts, entities, and relationships that form the foundational basis for the semantics of the ODRL policies.

Policies are used to represent permitted and prohibited actions over a certain asset, as well as the obligations required to be met by stakeholders. In addition, policies may be limited by constraints (e.g., temporal or spatial constraints) and duties (e.g. payments) may be imposed on permissions.

The ODRL specification can be added to the [data catalog](0012-data-catalog-specifies-all-data-components.md) to keep data storage and permissions on the data stored closely related. Also permissions on other components, like projects, can be specified using ODRL.

Specifying ODRL can be done in the JSON format as described by [53. Project company data](0053-project-company-data.md).

## Decision

We will use ODRL to specify permissions on components on the platform as implemented by [53. Project company data](0053-project-company-data.md).

## Consequences

### Advantages

* Permissions are described in a clear and specific way.
* Deployment of permissions can be automated to prevent inconsistency between documentation and actual situation.

### Disadvantages

* The JSON format used can be hard to read and write for humans.


## References

* https://www.w3.org/TR/odrl-model/, retrieved 9 October 2020

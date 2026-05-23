# API Design and Background

## Status

Proposed

## Context

Most line of business applications deal with common semantic entities - people, organizational units and their relationships.

There are very common attributes of those entities - names, and contact details for example.

Application vendors like Microsoft, SalesForce and others, alongside organizations like ISO have codified common schema for many of these elements, but they are usually surfaced in a particular application model, like a Directory Service, or a CRM.

However, most Line of Business applications would benefit from a standard, but extensible, and application-agnostic API over these Line of Business entities.

Microsoft Graph appears to have a long-term goal of providing some or all of these features, but it seems to be doing so in a way that supports "loose integrations" around the Microsoft 365 ecosystem, rather than being foundational elements of general purpose applciation development.

The Marain.LineOfBusiness project codifies APIs and schema for the common semantic entities we find in Line of Business applications that we have developed across multiple domains, from B2B to B2C applications, including (but not exclusively) financial services, retail, banking, logistics, and HR.

The initial bounds of the domain of interest could include

People (and their relationships)
Organizational Units (and their relationships)
Relationships between people and organizational units

Scope might expand to include

Educational information (qualifications, institutions)
Employment information (employer/employee, roles)
Personal Financial Information (e.g. income/outgoings)
Contractual relationships
Travel and residency (address history, location information) 

The intention is to provide the layer above the storage infrastructure that you need for many/most Line of Business applications, and encourage the use of standardized schema (derived from formal and de facto industry standards) for those entities, so that you can focus on application workflow and logic, rather than the persistence of entities and their relationships.

It should also provide patterns you can follow when designing the APIs that store and query domain-specific information related to your particular application. In part this is to encourage the notion that you should Open Source those domain entities and APIs too, as they provide common underpinnings of communal value, rather than your unique value, and will encourage 3rd parties to adopt and integrate your platform, especially using low-code technologies like Microsoft Flow and Zapier.


## Decision


## Consequences


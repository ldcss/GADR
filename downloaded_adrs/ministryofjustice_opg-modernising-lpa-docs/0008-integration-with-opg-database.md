---
layout: layouts/adr.njk
title: "Integration with the OPG database"
weight: 1
date: 2022-03-15
review_in: 12 months
tags:  
    - adr
    - open_standards
    - apis
    - integration
    - open_data
    - common_platforms
areas_of_coverage: ["Digital Service"]
status: "accepted"
contributors: ["John Nolan"]
adr_number: "0008"
---

## Context

We need to ensure we can integrate to our OPG database as it holds all the data for our LPAs.

It is used by many parts of OPG. A few of these are

- Case Managers
- External scanning service
- Public facing services (Make a LPA, Use a LPA, View a LPA)
- Internal Services and APIs

## Technical

All our services in some way integrate with the OPG database, whether this is directly or via an API or service in between.

The database contains all our LPA information from creation on Make a LPA, scanning of the documents, case workers working on the case, through to the Use a LPA service.

Modernising will be no different, but we must decide on the best way to do this as we enter our Beta phase.

### Availability

As the LPA data is stored within the OPG database, we need to be aware that it can be taken offline at any point for planned or unscheduled reasons.

If there is down time of the database, then we need to plan for how we handle this.

Should we defensively code and provide a degraded service?

Should we build the integration points to handle downtime, allowing the service to run to an extent and retroactively complete any operations pending.

Whatever the decision is within the architecture, it should be decided ahead of any build and is outside the scope of this ADR.

### Interoperability - How does this enable the exchange of information

It is essential to be able to communicate with our Case Management System and the database which contains existing LPA data.

In order for all other services to take advantage of the Modernising work, we need to ensure interopability between the services.

### Developer Knowledge - How well known is this in our current skill sets

**Overall**: 8/10

Developers already work against shared APIs and internal services to the OPG database.

### Support/Open Source - Is it well supported

N/A

### Scalability

As long as the correct technology is chosen to sit between the database, Modernising and other services, we should be able to scale any points of interaction between the services.

## Ethics

### Mitigate against being tech deterministic

N/A

### Ensure you conduct inclusive research

N/A

### Think big and imagine what the impact of your work can be

Integrating with Sirius and the database during the Modernising user flows will allow us to progressively approve LPAs as they are created. If there is a safeguarding issue early on in the process, then we can catch it sooner.

It also allows us to capture earlier those who are eligible for discounts to LPAs and therefore reducing the need for refunds post registration.

### Interrogate your data decisions

When we integrate with the database, it is important to ensure we only have access to the data we need and nothing more.

If the part of the service is responsible for adding data and validating that data, then the integration point should for example only allow adding of data and getting a confirmation of valid or not from the integration. We should not be returning data and comparing it on the Modernising side.

### Decision

We should integrate with the OPG database via an internal API and not directly with the case management system or the database itself.

### Consequences

We need to explore the best way to integrate and define any processes and data models that will ensure that case management work and Modernising flows match for data consistency.

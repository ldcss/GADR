---
layout: layouts/adr.njk
title: "Github for source control"
weight: 1
date: 2021-07-05
review_in: 12 months
tags:  
    - adr
    - open_standards
    - tools
    - techniques
    - deployment
    - integration
areas_of_coverage: ["Digital Service"]
status: "accepted"
contributors: ["John Nolan"]
adr_number: "0003"
---

## Context

We want to store our source code in a open source, cloud based git provider.

## Technical

### Interoperability - How does this enable the exchange of information

Github is accessible via built in APIS and allows us to open source our code for others to raise issues and ourselves, share details on releases and updates.

### Developer Knowledge - How well known is this in our current skill sets

**Overall**: 10/10
Developers work every day within Github for existing services.

### Support/Open Source - Is it well supported

We have an Enterprise licence for Github giving us a channel for any support queries.

Github allows us to open source our code when we are ready.

### Scalability

Github is cloud based and incredibly popular giving us a reliable solution for hosting our code.

Should we need to move for any reason, we are using Git which enables us to move to a new provider.

## Ethics

### Mitigate against being tech deterministic

There are other providers we could use, but doing so would not bring any great benefit over our already established best practices for existing services and level of support we have with the Enterprise version.

### Ensure you conduct inclusive research

N/A

### Think big and imagine what the impact of your work can be

Allowing the access of our code via the platform will encourage others to be able to help contribute and reuse our services built.

The more we can share with others, the stronger our solutions will be.

### Interrogate your data decisions

We should ensure that our repositories are marked as Open Source as soon as we feel comfortable.

### Decision

We should continue to use our Ministry of Justice Github Enterprise account for our source code.

### Consequences

We will be able to use our existing management infrastructure for user management and deployments without the need for additional cost or resources.

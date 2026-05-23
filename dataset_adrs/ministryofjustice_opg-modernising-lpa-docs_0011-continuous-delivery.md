---
layout: layouts/adr.njk
title: "Continuous Delivery"
weight: 1
date: 2022-03-18
review_in: 12 months
tags:  
    - adr
    - techniques
    - deployment
    - open_standards
    - integration
areas_of_coverage: ["Digital Service"]
status: "accepted"
contributors: ["John Nolan"]
adr_number: "0011"
---

## Context

The [GOV.UK technical guidance](https://www.gov.uk/service-manual/technology/deploying-software-regularly) specifies that software should be deployed regularly.

Principles from the GOV.UK guidance are as follows and we will hold ourselves to them.

* deploy little and often
* deploy quality software
* use auditable deployments
* use zero downtime deployments where possible

## Technical

### Developer Knowledge - How well known is this in our current skill sets

**Overall**: 9/10
All our teams use Continuous Delivery in their services and it is a standard practice for all.

### Decision

Build the service with Continuous Delivery in mind and as the default. This will require the following elements to be in place

* build a single artifact rather than variations for different environments
* have multiple deployment environments
* manage variable configuration
* secure passwords and keys
* use smoke tests - software tests that check if the most important functions are working

### Consequences

* [Automated testing](./0010-automated-testing) will need to be of a high enough standard to give Product Owners confidence in the process
* Builds and deployments are repeatable
* Deployments are quicker
* Fast feedback cycle

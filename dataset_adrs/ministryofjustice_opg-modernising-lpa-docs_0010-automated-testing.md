---
layout: layouts/adr.njk
title: "Automated Testing"
weight: 1
date: 2022-03-18
review_in: 12 months
tags:  
    - adr
    - techniques
    - deployment
    - testing
    - stability
    - integration
areas_of_coverage: ["Digital Service"]
status: "accepted"
contributors: ["John Nolan"]
adr_number: "0010"
---

## Context

The [GOV.UK technical guidance](https://www.gov.uk/service-manual/technology/quality-assurance-testing-your-service-regularly) specifies that tests should be automated where possible.

## Technical

### Interoperability - How does this enable the exchange of information

Using automated tests allows us to run locally and in the pipeline. This enabled others to openly see and consume any data produced by the tests.

### Developer Knowledge - How well known is this in our current skill sets

**Overall**: 9/10
All our teams use automated tests in their services.

### Support/Open Source - Is it well supported

This is dependent on the framework used.

## Ethics

### Think big and imagine what the impact of your work can be

Having our automated tests run on the pipeline means we have confidence in our build and others who rely on the code can have confidence that it is doing what it should be.

### Decision

Include and implement automated code coverage tests, accessibility tests, and security and penetration testing

### Consequences

* Increased overhead on initial development
* Increased confidence in future changes not causing issues
* Testing can be integrated into release processes without requiring manual intervention

---
layout: layouts/adr.njk
title: "Centralised OpenAPI Specification"
weight: 1
date: 2022-02-08
review_in: 12 months
tags:  
    - adr
    - open_standards
    - apis
    - language
    - integration
areas_of_coverage: ["Digital Service"]
status: "proposed"
contributors: ["John Nolan"]
adr_number: "0007"
---

## Context

We need a way to centrally define our data model that would allow us to have a source of truth for our data.

Reducing human error and duplication of code, we should reference our core data model wherever possible to maintain a centrally approved schema.

This could include

- Domain model
- Validation requirements
- Response messaging
- Object definitions (such as LPA ID or Post Code)

## Technical

### Interoperability - How does this enable the exchange of information

OpenAPI would allow us to use `$ref` to point to a centralised and publicly available schema for common domain objects.

Using standard HTTP protocols for making these links and a commonly accepted standard for the structure of the schema will enable great interopability.

### Developer Knowledge - How well known is this in our current skill sets

**Overall**: 6/10
Many of our teams have implemented OpenAPI specs in their services. Those that haven't do have knowledge of RESTful APIs and JSON or YAML to be able to work with it.

To the extent of managing a central specification and maintaining the changes in it, this is new ground and would need an investigation around best practices and automation techniques.

### Support/Open Source - Is it well supported

OpenAPI is a open source collaboration project.

### Scalability

If we don't have safety measures in place, such as versioning of core schemas, then there is a risk of down stream consequences causing issues in code bases and APIs that rely on it.

We need to research best practices of how we take advantage of the de-duplication and centralisation without increasing work load and error rates in our services.

## Ethics

### Mitigate against being tech deterministic

N/A - Uses a popular and accessible pattern and language

### Ensure you conduct inclusive research

N/A - the use of this technology does not have an effect on marginalised groups directly.

### Think big and imagine what the impact of your work can be

A publicly available data schema would allow anyone outside of OPG to develop solutions. This could lead to new applications on the market that solve problems in sectors we can't fund research into.

It increases the understanding of what the LPA is in wider society. Solicitors and charities for example would be able to align their practices more accurately. They will also be able to feed back into the model with real life experiences.

### Interrogate your data decisions

N/A - there is no place for personal data to be stored within OpenAPI Specifications.

### Decision

We should investigate the use of a centralised OpenAPI Specification. Within that research we should ensure we are not over engineering the solution and that the benefits would outway the cost of maintenance.

### Consequences

We will be able to maintain a single source of truth model in all our work.

Outside of the benefits of API design, using modern tooling we can ensure our classes within our code match our centralised model.

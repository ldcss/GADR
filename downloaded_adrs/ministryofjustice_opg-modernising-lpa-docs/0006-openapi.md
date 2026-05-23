---
layout: layouts/adr.njk
title: "OpenAPI Specifications"
weight: 1
date: 2022-02-01
review_in: 12 months
tags:  
    - adr
    - open_standards
    - apis
    - language
    - integration
areas_of_coverage: ["Digital Service"]
status: "accepted"
contributors: ["John Nolan"]
adr_number: "0006"
---

## Context

We need a way to communicate our APIs intent to consumers. We should display all options available as well as required data and validation associated with integrating with our APIs.

Any changes to the schema of our API should be testable via this specification.

## Technical

### Interoperability - How does this enable the exchange of information

OpenAPI is a common format used across a wide range of services.

As a result of its popularity, our main languages, Golang, Python and PHP all support the OpenAPI Standard.

There is great support for OpenAPI through third party services and tools that we can take advantage of. A great example of tools available can be found on [OpenAPI.Tools](https://openapi.tools/).

A few examples are

- Automatic Documentation Generators
- Mock Servers
- Testing
- Data Validators
- CI Automation checks

You can use JSON or YAML format for the structure and both are well known standards.

GOV.UK have excellent [guidance on how you should document your APIs](https://www.gov.uk/guidance/how-to-document-apis) in their [API Design Guidance](https://www.gov.uk/government/collections/api-design-guidance) page.

### Developer Knowledge - How well known is this in our current skill sets

**Overall**: 8/10
Many of our teams have implemented OpenAPI specs in their services. Those that haven't do have knowledge of RESTful APIs and JSON or YAML to be able to work with it.

### Support/Open Source - Is it well supported

OpenAPI is a open source collaboration project.

### Scalability

If we have many services with many OpenAPI specifications, there could be issues of maintaining them all.

If we do not have a well defined domain to work from, we run the risk of duplication of schemas and being out of sync with style, definitions, parameters and responses. This can result in poorly implemented code to get around inconsistencies or badly written specifications without style validators in place.

We should look into practices that help define a centrally accepted domain and styles that can be pulled from and validated against for all services and implementations.

There is a risk of development slowing down and bugs entering code should we not pay attention to best practices from the start. We should investigate these options with the teams as soon as possible.

## Ethics

### Mitigate against being tech deterministic

N/A - Uses a popular and accessible pattern and language

### Ensure you conduct inclusive research

N/A - the use of this technology does not have an effect on marginalised groups directly.

### Think big and imagine what the impact of your work can be

Using OpenAPI Specifications gives us a library of great resources of all our internal and external integration capabilities.

We could take a list of them and add them to a government API register to allow other 3rd parties and internal government services to find integrations we provide.

### Interrogate your data decisions

N/A - there is no place for personal data to be stored within OpenAPI Specifications.

### Decision

We should use OpenAPI Specifications for all internal and external APIs.

### Consequences

We will be able to maintain an up to date, testable and descriptive resources of all our available integrations across multiple services.

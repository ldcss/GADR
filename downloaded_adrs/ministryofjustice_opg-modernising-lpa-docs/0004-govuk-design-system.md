---
layout: layouts/adr.njk
title: "GOV.UK Design System"
weight: 1
date: 2021-07-13
review_in: 12 months
tags:  
    - adr
    - common_platforms
    - open_standards
    - framework
    - tools
areas_of_coverage: ["Digital Service"]
status: "accepted"
contributors: ["John Nolan"]
adr_number: "0004"
---

## Context

We need to follow strict government guidelines on design and accessibility. The design should be consistent across all pages and work for as many browsers as possible.

## Technical

### Interoperability - How does this enable the exchange of information

[GOV.UK Design System](https://design-system.service.gov.uk/) is open source and used across all digital government services.

Any new patterns that we create can be contributed back with our research included.

We should take advantage of other services research and contributed design patterns and feedback ours.

### Developer Knowledge - How well known is this in our current skill sets

**Overall**: 8/10
Developers have knowledge of the design system and work with it on a regular basis.

The use of tooling and testing around front end development is not as strong so will require more focus when implementing.

### Support/Open Source - Is it well supported

The [GOV.UK Design System](https://design-system.service.gov.uk/) is completely open source and is required for all public facing government services.

It has its own team as well as a large community of designers, user researchers, content and developers contributing to it.

### Scalability

The [GOV.UK Design System](https://design-system.service.gov.uk/) has 4 different types of assets to consume.

There will be custom patterns and components that we need to build, but because of the use of SASS and Javascript, we will be able to stick to the same standards as the design system and take advantage of the built in variables.

#### SASS

Allows us to only require styling resources needed.

We can generate our styles dynamically and keep up to date with the latest styling changes and colours due to SASS variables.

#### Javascript

Contains all the code we need to progressively enhance the user interface.

We only need to import modules that we required and all functionality can be updated for bug fixes or new features via npm.

This will remove the need for custom Javascript to be written in most cases.

#### Assets

Contains all images and fonts required for running a Government service. We can keep up to date by always ensuring we import at build time the latest assets available.

#### Nunjucks

Depending on the technology we want to use, this could be useful. Being able to use these templates, we can ensure we will always have access to the latest components available and maintain our code base with a set of pre configured templates.

The use of Nunjucks as the templating language should be discussed in another ADR.

## Ethics

### Mitigate against being tech deterministic

Due to GDS standards, we are required to choose this design system.

### Ensure you conduct inclusive research

All the components and patterns are centrally managed and community driven to include user research in each to a high level. This gives us the advantage of having a high degree of confidence that we are using the right tool for our development.

### Think big and imagine what the impact of your work can be

As we use the design system, we will find ourselves using custom patterns and components. We should make sure we contribute back as much information as possible to help other services take advantage of our research.

### Interrogate your data decisions

Where possible we should stick to the standards defined by the [GOV.UK Design System](https://design-system.service.gov.uk/).

If we do decide to move away from the standard, it should be done with the correct research to back the decision and fed back to the [GOV.UK Design System](https://design-system.service.gov.uk/) team.

### Decision

We should and have to use the [GOV.UK Design System](https://design-system.service.gov.uk/).

### Consequences

We will be able to work at a high cadence and understanding as the [GOV.UK Design System](https://design-system.service.gov.uk/) is used throughout all our services on a day to day basis.

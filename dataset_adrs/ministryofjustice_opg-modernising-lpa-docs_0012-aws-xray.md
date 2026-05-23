---
layout: layouts/adr.njk
title: "AWS X-Ray"
weight: 1
date: 2022-03-21
review_in: 12 months
tags:  
    - adr
    - observability
    - tools
    - language
areas_of_coverage: ["Digital Service"]
status: "accepted"
contributors: ["John Nolan"]
adr_number: "0012"
---

## Context

We want a way to trace, analyse and debug our distributed systems across our cloud architecture.

This will give us the ability to

* Find bottle necks in our services
* Discover hidden errors within our stack
* Identify areas of improvement
* Justify continuous improvement work
* Helps in diagnosis during incidents and tracking change from releases

## Technical

### Developer Knowledge - How well known is this in our current skill sets

**Overall**: 5/10
Our teams are starting to use this functionality in their services.

Capturing data is the first part of this, however there are more things that need to be learned and implemented. We should help and encourage those wanting to learn to do so.

A few areas where our maturity can be improved are.

* Thinking about Observability in ticket creation as part of the Product Lifecycle
* An understanding of what to track and what not to track
* Teams able to continuously improve bottlenecks found in their workflow
* Teams are able to see their service health and actively check
* Understand and set their own benchmarks for what good looks like
* Implement the right level of alerting to support observability
* Look at the possibility of a Observability Community of Practice to help share learnings across teams

### Decision

We should use [AWS X-Ray](https://aws.amazon.com/xray/) to monitor and maintain a healthy service.

### Consequences

* Chosen languages may not support its features
* Observability should be part of ticket prep and refinement to facilitate.
* Code should be written from the start to add the feature
* Continuous improvement will become a part of the Product lifecycle
* Ownership of monitoring
* Benchmarks set for acceptable parameters

---
layout: layouts/adr.njk
title: "AWS WAF"
weight: 1
date: 2022-03-22
review_in: 12 months
tags:  
    - adr
    - observability
    - tools
    - security_threats
    - observability
areas_of_coverage: ["Digital Service"]
status: "accepted"
contributors: ["John Nolan"]
adr_number: "0013"
---

## Context

We want to ensure our services are protected to a high standard via a Web Application Firewall.

Our services run on AWS and already implement [AWS WAF](https://aws.amazon.com/waf/) where needed.

We currently run the following default rules on our PHP applications as well as custom built rules specific for our tech stacks.

* CommonRulesSet
* KnownBadInputs
* PHPRulesSet

Depending on the technology used on the service, we ensure we have the correct rules in place, for example, SQL injection, XSS and many others specific to language and infrastructure choices.

## Technical

### Developer Knowledge - How well known is this in our current skill sets

**Overall**: 9/10
Our teams are starting to use this functionality in their services.

### Decision

We should continue to use [AWS WAF](https://aws.amazon.com/waf/) in any new services and build upon on knowledge and experience of existing implementations.

### Consequences

* Visibility of near real time web traffic and alerts
* Automated alerting against rules set
* Managed rule sets for new and existing threats
* Rules need to take into account our customer behaviours, e.g. multiple users from a corporate network on the same IP Address
* There is a risk to false positives happening on front ends. As a result, developers will need to take this into account when debugging issues on a service
* There is a minor cost to enabling AWS WAF on services

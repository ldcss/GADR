---
layout: layouts/adr.njk
title: "Multi Region by Default"
weight: 1
date: 2022-04-08
review_in: 12 months
tags:  
    - adr
    - data_privacy
    - security_threats
    - techniques
    - deployment
    - stability
areas_of_coverage: ["Digital Service"]
status: "accepted"
contributors: ["John Nolan"]
adr_number: "0015"
---

## Context

We want our services to be resilient to data center failure. If a data center or region goes down, we want to be able to switch to a new region quickly with minimal to no data loss.

Region failure is rare but does happen. Common situations for region failure are

* Natural disaster
* DDOS attacks
* Data Center outages

### Decision

Our other services already are or are in the process of using Multi Region Architecture.

We should continue to use this strategy for any new architecture.

### Consequences

#### Positive

* It is quicker to build our services as multi region from the start rather than retroactively
* We can fail over to another region in case of an outage
* If we are unable to use a particular region due to Government policy changes, we can quickly move

#### Negative

* Initial building times are slightly longer
* Developers will need to factor in multi region when designing their services

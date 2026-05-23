# 1. Deployment on-prem & as a SaaS

## Status

Accepted, 2019/05/31

## Context

In global health there are two deployment constraints that push against one
another:  the desire for iNGO's, government agencies, multi-laterals, etc to
lower the barrier to acquiring software solutions by utilizing a SaaS model,
and that of many governments to exercise self-reliance and sovereignty of their
software and their data by being able to reasonably deploy software on premise
in their own data center.

With regards to SaaS, most customers of the software are able and willing to
pay reasonable monthly fees, especially if those fees are predictable over a
suitable project timeline.  For organizations that want to offer PCMT as a
SaaS they likely will expect the number of instances to be quite low:  likely
less than 25 in the next 5 years.  Thus the key attributes for those running
PCMT as a SaaS and for those consuming PCMT as a SaaS are reasonable fees and
lead-times for signing a new instance on.

When a government agency deploys the software in their own data center a
principal concern is that of limited resources.  Limited both in hardware and
the maturity of the data center, as well as on the technical staff available.
There are few organizations within PCMT's user-base that have extensive 
experience running highly available services or complicated deployment stacks.

We have a number of choices that are available to us:

1. Multi-tenancy development in theory can achieve the greatest 
   cost-per-customer since the same application code on the same hardware
   can serve more than one customer.  However it can significantly increase
   the scope and development of each feature as each needs to consider how
   many customers would share the same resources without impacting one-another.
   It can also increase deployment cost and complexity as each instance needs
   to be configured and monitored for many clients.
1. Multi-single-tenancy is really a single tenancy model that utilizes advances
   in containerization, oftentimes cloud providers, and deployment tools to 
   manage many single instances, one per customer, in such an automated fashion
   as to make it nearly indistinguishable from multi-tenancy.
1. Serverless is an approach to reduce overhead for developers by shifting 
   resource management to a provider.  It's included here for completeness, 
   and while it may make development practices easier, the deployment of a 
   serverless architecture on-prem in PCMT's context is non-trivial.

## Decision

We will build PCMT to be [multi-single-tenant][multi-single-tenant] utilizing 
containers as the basic unit of deployment.  Each instance of PCMT will be 
served by one or more containers, and where each container serves only one 
function for one PCMT instance.

We will build simple tools, in the category of Infrastructure as Code, that
helps provision computing resources both in one cloud provider as well as
on-prem, configure the instance of PCMT, and aid in the maintenance life-cycle 
of that instance:  upgrades, backups, archiving, destruction.

We will provide complete IaC deliverables that are able to provision resources
outside of PCMT's scope, such as email & DNS.

We will build PCMT so that it runs in as little as 2GB of RAM, 2 cores of a 
modern CPU and 10GB of storage which is a reasonable requirement of most on-prem 
data centers.  As of May 2019 this targets a $30 / month per PCMT
instance price-point in one cloud provider, with plenty of opportunity for 
additional per instance and per month reductions in cost.

[multi-single-tenant]: https://www.linkedin.com/pulse/architecture-constraints-end-multi-tenancy-gregor-hohpe/

## Consequences

The development team will not need to scope and build each feature to be
multi-tenant.

The development team will need to properly scope and build PCMT and its
supporting deployment tools to run both in the cloud and on-premise using
a basic set of IaC tools that are free and simple to use.

PCMT's scope and performance characteristics will be constrained in-part by 
what can be reasonable run within 2GB of RAM and 2 CPU cores with 10GB of 
storage.

Those wishing to deploy PCMT as a SaaS will have a starting point, however they
likely will need to invest more in order to run a large number of instances,
reduce the deployment lead-time, or reduce the per-instance cost.

---
Copyright (c) 2019, VillageReach.  Licensed CC BY-SA 4.0:  https://creativecommons.org/licenses/by-sa/4.0/

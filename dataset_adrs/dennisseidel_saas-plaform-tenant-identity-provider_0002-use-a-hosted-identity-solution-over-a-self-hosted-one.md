# 2. Use a hosted Identity Solution over a self hosted one.

Date: 2019-02-05

## Status

Accepted

## Context

We need an identity provider for our platform. This could be a host (SaaS) solution vs a self hosted solution. While the Cost & Lockin is higher at scale with a SaaS the self hosted has a higher Management Effort & Less Security & Expensive Bootstraping. From an evolutionary architecture perspective it is not core to value generation and does not change rapidly[source](https://www.youtube.com/watch?v=8bEsNT7jdC4&t=112s&index=57&list=WL) - identity will mostlikly the same (OpenIDConnect, Login page ...) but it will be hard to change in the future if you decided for one provider.

## Decision

We will use a SaaS solution as we don't have the skill to host our own solution in the efficient quality. And from a evolutionary architecture perspective the system is commondity or support.

## Consequences

This will make it easier to get started fast and reduce the security risks of misconfiguration/missing upgrades & reduce the bootstraping cost. But It will lead to higher cost if we scale large enough. This could be mitigated by keeping the posibility to migrate to a self hosted solution, by using the standards.


## Links
* https://www.thoughtworks.com/radar/techniques/hosted-identity-management-as-a-service
* https://www.thoughtworks.com/radar/platforms/keycloak
* https://www.thoughtworks.com/radar/platforms/auth0
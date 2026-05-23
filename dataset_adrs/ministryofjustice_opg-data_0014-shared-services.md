# 14. shared services

Date: 2020-05-15

## Status

Accepted

## Context

As we move to a structure where products share services rather than being purely isolated systems, we are moving away from a model where the API Gateway acts solely as a pathway into the Sirius Backend API. Early integrations such as providing LPAs to __Use and LPA__ or passing files from the __Digital Deputies Reporting Service__ were thin layers of translation over the existing Sirius API.

The next phase of our API work is to move to a model where multiple products share and use an API that owns all its data, and encapsulates a need in the OPG domain. Our first example is the Use an LPA codes service, which provides data for both Sirius Case Management and the Use an LPA service, but is independent of both.

This is in parallel to work that is splitting Sirius into smaller services, with the expectation that the two streams of work will eventually converge as a set of isolated services that can be recomposed into new products, our "Service Swarm".

## Decision

Shared services will sit behind the OPG Data API Gateway and follow the [0009-api-domain-structure.md](api domain structure decision). Shared services will be isolated and own a particular domain for our applications. That is, they own a particular business process or kind of data, for example the generation and expiry of access codes.

These services currently live within the boundary of the "Sirius" account, but are deployed independently.

## Consequences

This new model requires that product teams build and test with known contracts with appropriate mocking of the service during development stages (see [0013-pact-broker.md](Pact Broker decision)).

This approach also means that cross team communication around needs and contracts is essential during kickoff and improvements.

Services must have ownership from a team. This is currently the "Integrations" team, who own, maintain and interate the API as product work.

This model opens up the opportunity for us to reduce the amount of duplication across our products by providing independent services for common patterns (i.e. Authentication).

Use of the [0009-api-domain-structure.md](common domain structure) means that services can live in either Lambdas, ECS tasks or elsewhere depending on the need, with the API Gateway as a stranglepoint for moving
 implementations as needed.

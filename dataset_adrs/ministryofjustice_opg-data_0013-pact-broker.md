# 13. Pact Broker

Date: 2020-04-06

## Status

Proposed

## Context

We will use Pact to maintain contracts required of web services by the consumer and provider of an interaction.

## Decision

Our pact workflow is described in the diagram below (this is the deputy-reporting service, but could apply to any implementation).

![Workflow diagram for deputy reporting](https://github.com/ministryofjustice/opg-data-deputy-reporting/raw/master/docs/pact/pactdiagram.png?raw=true)

Which amounts to the following steps on both sides of the interaction.

1. Consumer system team creates a Pact contract required for its interaction with the Provider.

2. Consumer team creates a branch to build their new contract and pushes it to Github.

3. Push to github pushes the new pact file to the broker.

4. Push to the broker triggers a provider verifcation workflow. This tests the validity of the changes against the current API from the provider.

5. Results of the verification workflow tag a build as valid or invalid.

## Consequences

Pact broker gives us a tool to maintain API contracts between systems.

We have to maintain the broker as a system.

Any limitations in Pact will impact our workflows and technology choices. For example, forcing application/json over multipart.

Some duplication of effort between OpenApi specifications and Pact files in terms of defining the API.

Pact does not replace interactions between teams or normal development processes. A consumer team should discuss requirements before pushing an initial Pact file change, or use the Push as a starting point for discussion.

## Related links

*[Pact](https://docs.pact.io/)
*[Pact in the Deputy Reporting Integration](https://github.com/ministryofjustice/opg-data-deputy-reporting/tree/master/docs/pact)

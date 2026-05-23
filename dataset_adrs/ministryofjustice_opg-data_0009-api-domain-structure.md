# 9. API Domain Structure

Date: 2020-02-03

## Status

Proposed

## Context

We need to establish a domain structure which

* Is product agnostic
* Is consistent across the opg-data service

## Decision

We will adopt the pattern:

[pull-request-id].[account-stage].[microservice-domain].api.opg.service.justive.gov.uk

Where [pull-request-id] is for ephemeral dev environments.
Where [account-stage] is the stage in our path to live/accounts i.e. dev,pre and empty for prod services.
Where [microservice-domain] is the scoped domain of the microservice/integration in in question.

* hey

### examples

#### root:

* https://api.opg.service.justice.gov.uk

#### integration:

* https://deputy-reporting.api.opg.service.justice.gov.uk

#### environments per integration:

* https://pre.deputy-reporting.api.opg.service.justice.gov.uk
* https://dev.deputy-reporting.api.opg.service.justice.gov.uk

#### pr raised on an environment per integration:

* https://pr-1234.dev.deputy-reporting.api.opg.service.justice.gov.uk

## Consequences

# 10. API Repo Structure

Date: 2020-02-03

## Status

Proposed

## Context

AWS infrastructure such as API gateway endpoints and lambdas are deployed via terraform, and so are represented at a filesystem-level by terraform .tf files

## Decision

Repo naming convention:
opg-data-[microservice-domain]

* .tf files pertaining to API Gateway infra to be stored in the [opg-sirius-api-gateway repo](https://github.com/ministryofjustice/opg-sirius-api-gateway)
* .tf files pertaining to a specific integration (eg lambdas) are managed in the integration-specific opg-data-[microservice-domain] repo, which is then 'deployed over' the API Gateway

for example, files for deputy-reporting /reports endpoint are saved in [opg-data-deputy-reporting](https://github.com/ministryofjustice/opg-data-deputy-reporting)

## Consequences

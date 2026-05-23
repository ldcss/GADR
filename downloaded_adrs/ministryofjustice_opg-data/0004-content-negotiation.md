# 4. Content Negotiation

Date: 2020-01-22

## Status

Proposed

## Context

It is becoming more common to recognise that a specific format of a resource is the combination of content type AND version.

## Decision

For the reasons explored in [2. API versioning strategy](0002-api-versioning-strategy.md),

* We will implement versioning via Content Negotiation using the Accept header, as per option 5, below. This seems the most future proof, most RESTful solution.

This necessitates our own vendor content type, which we will call `opg-data`

`application/vnd.opg-data.[version]+[representation]`

Representation will default to `json` and version will default to `latest`

Some Examples:

* `application/vnd.opg-data.v1+json` (v1 presented as JSON)
* `application/vnd.opg-data.v1+yml` (v1 presented as YAML)
* `application/vnd.opg-data.v1` (v1 presented as JSON)
* `application/vnd.opg-data` (latest version, presented as JSON)
* `application/json` (latest version, as JSON)

## Consequences

* An agreed content-type, with sensible fallbacks.
* Versioning is controlled in the headers
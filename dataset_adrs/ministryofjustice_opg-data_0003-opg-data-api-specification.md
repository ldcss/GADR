# 3. OPG-Data API Specification

Date: 2020-01-22

## Status

Proposed

## Context

### A pragmatic approach

We need to arrive at an API spec that is fully formed, without spending an inordinate amount of time creating something from scratch, when other mature specifications exist and can be leveraged to suit our needs well.

Most major tech corporations have arrived at their own slightly differing proprietary implementations of a RESTful API spec, and none are completely awful or completely successful.

Some are more mature than others, such as JSON:API [https://jsonapi.org](https://jsonapi.org), which "has been properly registered with the IANA. Its media type designation is application/vnd.api+json."

It is also [open-source](https://github.com/json-api/json-api).

> "By following shared conventions, you can increase productivity, take advantage of generalised tooling, and focus on what matters: your application."

## Decision

Our RESTful API implementation will be heavily based on JSON:API, and our documentation will focus mainly on hilighting those points where it differs.

We will also summarise and elucidate key points as needed.

## Consequences

Where our documentation does not cover any aspect of the API specification, it should be assumed that the [JSON:API](https://jsonapi.org) standard applies, and should be observed.

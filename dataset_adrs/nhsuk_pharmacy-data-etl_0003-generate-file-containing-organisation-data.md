# 3. Store local copy of Organisation Data

Date: 2017-06-12

## Status

Accepted

## Context

The [NHS Organisation API](http://api.nhs.uk/organisations) holds information about pharmacies.
The [Connecting to Services](https://github.com/nhsuk/connecting-to-services) applications needs to make use of Pharmacy data.

## Decision

The NHS Organisation API will be scraped nightly to generate a file containing pharmacy data.

## Consequences

A daily snapshot of pharmacy data in JSON format is available for consumption by multiple applications,
enabling the whole dataset to be analysed and indexed.

The Organisation data will be scraped every night. This amounts to approximately 12,000 requests against the API over
the course of a 1 hour period.

The Organisation API will not be queried in real time, insulating the application against failure of the Organisation API.

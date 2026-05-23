# 2. Store ETL output in Azure

Date: 2017-06-12

## Status

Accepted

## Context

The output from the ETL is only available in the container and needs to be exposed to consuming applications.

## Decision

When the ETL has completed the output will be stored in an Azure blob, Azure being the current preferred cloud platform.
The output file will be exposed on a publicly available URL.

## Consequences

Pharmacy data is available to other applications from a publicly available URL.

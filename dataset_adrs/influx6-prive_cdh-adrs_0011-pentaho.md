# Pentaho ADR


## Status

Accepted

## Context

We currently have certain specific feeds being parsed using pentaho, these are legacy feeds which transform data feed files into PriveXMl format. These feed parsers will require migration into new CDH ETL feeds parsers based on defined standard library.

## Decision

Due to limited resources and time constraints, we will defer the feed migration from pentaho to the CDH ETL till adequate human resources are available, more so an indept understanding of exactly how the parsers work is required, which will require talking with Christopher on this.

## Consequences

We will be running the Pentaho service alongside the ETL and CDH service.
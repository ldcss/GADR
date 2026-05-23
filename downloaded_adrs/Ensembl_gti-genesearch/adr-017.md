# ADR 016: Mixed-type sequence joins

## TL;DR
Use new field in Ensembl REST service to map non-gene sequences to genes

## Context
There is a new field returned by the Ensembl /sequence REST endpoint, `query`. 
This is to supported the scenario where multiple gene IDs are POSTed and non-gene sequence (cds, protein) requested. 
The ID spaces are different, so query contains the original ID used in the search.

The approach taken has been to use "query" as a special field used in the join that is equivalent to ID. This isolates the changes to the sequence search implementation.

## Status
Testing

## Consequences
Has added complexity to the sequence search logic.
More work needed to post-process returned objects sanely as the sequences are just attached to the gene level, not to any sub-level.

## Tags

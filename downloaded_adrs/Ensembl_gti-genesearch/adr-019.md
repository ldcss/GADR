# ADR 018: Sub-document filter queries

## TL;DR
The htsget-based EBiSC search needs to have queries by genotype, but only show genotypes that match. This has called for a hybrid query/filter approach.

## Context
In order to filter out sub-documents that don't match, `QueryUtils.queryAndFilter` has been implemented to carry out recursive query and filter on a supplied object and return an optional object with sub-documents filtered out (this object is empty if no match has been found).

This method is now used by `HtsGetVariantSearch` in query and fetch methods (see `queryAndFilter` method in this class)

## Status
Testing

## Consequences
Behaviour in htsget is different to that in, say, Elastic, which doesn't do sub-document filtering at the moment. This might be possible in future e.g. seeing if there is a specific Elastic query that can be run, or performing secondary filtering.

## Tags

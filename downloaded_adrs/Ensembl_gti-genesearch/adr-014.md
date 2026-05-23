# ADR 014: Range based join 

## TL;DR
Added support for range based querying, driven by need to join from gene to variants based on genomic location

## Context
The current model for joining between genes and variants is via the annotation field, matching on gene IDs. 
This is not sustainable in future for two main reasons:
1. EVA have expressed their opinion that range based querying is the only efficient way to do this with the current MongoDB schema
2. Restricted data for EBiSC/HipSci is only available via a HTSlib based endpoint which responds solely to range queries
To this end, we need to support range based joins as well as term based joins

## Decision
The main changes can be made fairly easily in `JoinMergeSearch`, but require the following changes to `JoinStrategy`:
1. A `JoinType` enum to trigger RANGE vs TERM
2. Changing the key fields from single strings to arrays.
The latter is a simple way to encode the fields required (seq region, min, max) though note that species/assembly may also be required. 
In an ideal world, `JoinStrategy` would have a defined generic type with these fields explicitly declared, but this is the simplest approach for now.
This change has triggered matching changes in all objects that use including `SubSearchParams`.

The implementation provided currently has separate query and fetch methods for range-based joins, which are separate to the term-based methods.

`RangeBasedJoinGeneSearch` provides a range-based join from gene to variation.

## Status
Under development

## Consequences
Inner join is not currently supported. More work is needed to consider how best to do this
Grouping is not supported as this is not appropriate for variation searches.

Different code for range and term searches could be abstracted out into separate classes.

MongoSearchBuilder is currently hardcoded for EVA, this needs generalising

## Tags

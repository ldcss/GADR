# ADR 015: Single type indices

## TL;DR
Switch from one index with multiple types to multiple indices.

## Context
Elastic now recommend that there should only be one document type per index, and this feature will be dropped in future:
https://www.elastic.co/guide/en/elasticsearch/reference/current/removal-of-types.html

To this end, we will make this change now to avoid future pain. This is particularly important as we bring in variants and other types into Elastic.

## Status
Under development

## Consequences
more config needed
more flexibility

## Tags

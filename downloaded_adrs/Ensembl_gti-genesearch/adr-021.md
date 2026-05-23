# ADR 021: Remove _all for joint queries

## TL;DR
Elastic Search version 6.0 deprecated _all option:

https://www.elastic.co/blog/minimize-index-storage-size-elasticsearch-6-0
and replaced it with copy_to :
https://www.elastic.co/guide/en/elasticsearch/reference/current/copy-to.html)

This option was set for genomes index file.

## Context
Index definitions

## Status
Evaluation

## Consequences
Some subsequent 'full text queries would not work anymore'

## Tags

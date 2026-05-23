# 2. Use MongoDB for the back-end data store

Date: 2020-04-22

## Status

Accepted

## Context

The existing print holdings system keeps all data in MySQL. While this allows
flexible querying, it is also computationally expensive and is difficult to
scale.

Known use cases largely involve computing things specific to a clusters'
holdings and HathiTrust items, so one way to parallelize queries is in a
map-reduce fashion - compute something about each cluster, then process the
data from each cluster into a final result.

## Decision

We will use MongoDB for a persistent data store. Each print holdings cluster
will be a document, and will contain holdings, HathiTrust items, and shared
print commitments for that cluster as sub-documents.

## Consequences

We will be able to use MongoDB's threading, sharding, and map-reduce
functionality to more easily scale query performance than with MySQL.

We will not be able to query the database using SQL.

We will need to develop the ability to merge or split clusters.

Ad-hoc queries that involve computing something about multiple clusters at once
will be more difficult to express. We are not aware of any such use cases
currently.

To produce a consistent data model, OCLC numbers and HathiTrust items must
belong to exactly one cluster. This implies that if a HathiTrust item has
a Zephir record with more than one OCLC number, we will put those OCLC 
numbers in the same cluster.

# 2. Use Neo4j as Persistence

Date: 2020-06-06

## Status

Accepted

## Context

We need to save information into a persistence layer in order to query and explore the data. The data we will be working with heavily relies on describing relationships which is well suited for a graph like structure.

## Decision

We will use Neo4J as the persistence layer. It is a fairly popular graph database, well documented and mature product.

## Consequences

We will need to use Cypher query language to create, read update and delete data.
This will also increase the deployment complexity of Topo.

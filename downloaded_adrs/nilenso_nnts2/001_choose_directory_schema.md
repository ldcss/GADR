# Choosing nested directory schema
<!--[proposed | rejected | accepted | deprecated | … | superseded by [ADR-0005](0005-example.md)] optional -->
* Status: proposed
* Date: 16-09-2019

## Context and Problem Statement
NNTS2 supports nested directories for every organization. What is the best schema/database to represent this nested structure?

## Decision Drivers
The ease of these operations
* View all directories for an org
* Get immediate parent/child directories
* Add a directory in a another directory (parent)
* Move/delete directories
* Using inherited permissions for directories
* Future migrations of data
NNTS2 use case is read-heavy than write-heavy. In most cases we are looking at immediate parent/child relationships. But in case of inherited permissions, the queries become more complicated.

## Considered Options
* Directory structure represnted as a json within org schema
* __Adjacency tree__ in relational database with application layer extracting the directory structure
* Postgres ltree extension
* Nested set model in relational database
* Closure table for directories
* Materialized path
* Neo4j, graph database

## Decision Outcome
Chosen __Adjacency trees__ with calculation of tree json in application layer. This is the best option for read/write queries on immediate parent/child directories.

### Positive Consequences
* Queries for only one level directories quite fast.
* Can be used in any type of relational database.

### Negative Consequences
* Will have to make sure that going from parent child rows --> tree json is efficient and fast.

## Pros and Cons of the Options

### Directory Structure for an org as json in organization schema
<!-- [example | description | pointer to more information | …]  optional -->
* Bad because user has to make sure every write is updating the json correctly.
* Bad because the database has no inherent structure. Just stored as text.
* Good because get all directories for org is a very short query
* Bad because finding immediate parent child relationships will involve going through the full map

### Adjacency tree with tree formation in application layer
* Good because add/edit/move/delete can be done seamlessly and without issues
* Bad for read queries if we try to get tree at sql layer
* Good for read queries if we are calculating tree structure at application layer
* Bad as we have to implement non-cyclic tree constraints

### Postgres ltree
* Good for ease of queries
* Bad as you can have missing nodes. Doesnt strictly follow tree convention
* Bad as its a postgres specific extension
* Bad as not supported by honeysql atm

### Materialized path
Store the full path at every node to represent the structure
* Good for queries containing path from root
* Bad for queries containing partial path (not starting from root). Will have to go through the full index in that case

### Nested set model (MPTT)
* Good for read queries, especially for getting subtrees from any node
* Bad for write queries as all nodes need to be updated for lft,rgt indexes

### Closure table
Keeping relationships in a separate table than the content table.
* Good, as we are not getting full data all the time when we just want structure
* Bad, as even immediate parent child queries require asking two tables.

### Neo4j
* Bad as this will be an additional database for a simple SPA.

<!--## Links  optional -->

# Use MongoDB for Operation service

* Status: [accepted]
* Deciders: [[@kakarotto67](https://github.com/kakarotto67)]
* Date: [2019-09-10]

Technical Story: [Move Operation API to MongoDB](https://github.com/kakarotto67/mlmc/issues/2)

## Context and Problem Statement

Operation API need some data storage to be able to list/commission/decommission/launch missiles.

## Decision Drivers

* Easy to use storage
* Fast storage
* Dynamic and/or schemaless storage

## Considered Options

* [MS SQL Server](https://www.microsoft.com/en-us/sql-server/sql-server-2019)
* [MongoDB](https://www.mongodb.com/)

## Decision Outcome

Decided to use MongoDB since

* The product growths without strict requirements, so entitites are changed very often. In this circumstances schemaless approach is better than predefined schema approach
* No need to use RDBMS just to store some random missiless on a stock
* I wanted to get some experience in MongoDB

### Positive Consequences

* Implementation will be faster and easier since schema is going to be changed lot of times

### Negative Consequences

* n/a

## Links

* n/a

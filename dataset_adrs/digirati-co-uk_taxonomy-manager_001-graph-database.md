# Selection of Graph Database software for SKOS taxonomy management

* Status: accepted
* Deciders: [@garyttierney](https://github.com/garyttierney), [@danielgrant](https://github.com/danielgrant), [@robmarch2](https://github.com/robmarch2)
* Date: 2019-05-23

Technical Story: DTM-34

## Context and Problem Statement

Persistence and retrieval of SKOS taxonomies require a storage layer that supports storing rich, free-form linked data.
Such a data model could be represented in a traditional RDBMS, however, doing so would require a specialized serialization and deserialization implementation whereas graph databases can typically store RDF natively.

## Decision Drivers <!-- optional -->

* High availability/Fault tolerance
* Learning curve
* Maintenance overhead
* Vendor lock-in

## Considered Options

* Apache TinkerPop
* Apache Jena Fuseki
* PostgreSQL

## Decision Outcome

Chosen option: Apache Jena with underlying PostgreSQL persistence store and a custom persistence layer, because it provides a highly available database persistence that is widely available as a managed service. We opted against using Apache Jena's SDB to achieve this as it has been in a state of "maintenance only" since June 2013.

### Positive Consequences

* PostgreSQL can be clustered, making it highly available
* PostgreSQL is broadly available as a managed service
* We can utilise the same PostgreSQL database for storing additional data (e.g. users, roles, etc)

### Negative Consequences

* We have to design our own schema and code for interacting with the PostgreSQL database

## Pros and Cons of the Options

### Apache TinkerPop

TinkerPop is less of a graph database implementation and more of an abstraction layer over various graph database backends.
It presents a frontend consisting of a query language named "Gremlin", that uses a method chaining style of syntax to build graph queries.

Some of the backends TinkerPop supports are listed below:

* Azure CosmosDB
* Amazon Neptune
* Neo4J

#### Query example (TinkerPop: Gremlin)

```gremlin
g.V().has('id', 'http://example.com/skos-concept').out('skos:broaderConcept').values('skos:preferredLabel')
```

#### Persistence example (TinkerPop: Gremlin)

```gremlin
g.addV('skos:concept').property('id', 'http://example.com/skos-concept').property('skos:preferredLabel', 'value')
```

[Query language reference documentation](http://tinkerpop.apache.org/docs/current/reference)

* Good, because it supports various graph database backends.
* Good, because it relies on a standardized query language, making the persistence implementation almost graph database agnostic.
* Bad, because the query language is not designed for simple CRUD operations, and instead for determining relationships across graph edges.
* Bad, because it's an extremely heavyweight generalized solution for data fitting a very specific model.
* Bad, because there is an extremely high learning curve associated with the Gremlin query language compared to something like SPARQL or SQL.
* Bad, because it's built for Groovy first and the JVM second.

### Apache Jena Fuseki

Fuseki is a hosted backend for the Apache Jena SPARQL engine.
It allows storage of RDF data by first serializing it to turtles and querying it back using the Jena API, or by executing SPARQL queries.

#### Query example (Jena: SPARQL)

```sparql
PREFIX skos: <http://www.w3.org/2004/02/skos/core/>
SELECT ?broader
{
  <http://example.com/skos-concept> skos:broaderConcept ?broader
}
```

#### Persistence example (Jena: API)

```java
RDFConnectionFactory connection = /* ... */;
connection.load("<http://example.com/skos-concept> <http://www.w3.org/2004/02/skos/core#broaderConcept> <http://example.com/skos-broader-concept>");
```

* Good, because it can store SKOS in its native representation (RDF)
* Good, because it has an extensive Java API available.
* Good, because the query and persistence options are intuitive and easy to use.
* Bad, because it is the only maintained open source SPARQL server available.
* Bad, because it is self-hosted and would require maintenance (as well as deployment of a new unfamiliar technology).

# Database Technology (Relational/Graph)

Technical Story: [Evaluate database technologies #46](https://github.com/UST-MICO/mico/issues/46)

## Context and Problem Statement

We want to use a state of the art database that can store services/applications according to our data Model and is easy to integrate with [Spring Boot](0001-java-framework.md).


## Decision Drivers

* Integration with [Spring Boot](0001-java-framework.md)
* Different versions of a service will be stored as individual services
* Applications will be seen  as concrete instances of services

### Data Model Relational

```eval_rst
.. graphviz::

    graph G {

        {
            subgraph cluster_0 {
                label="not deployable"
                style=dotted

                service [label=Service, shape=rectangle]
                serviceID [label=<<U>ID</U>>]
                serviceVersion [label=Version]
                serviceName [label=Name]
                serviceExtra [label="..."]

                predecessor [shape=diamond]
                depends [label="depends on" shape=diamond]
                has [shape=diamond]

                versionRange [label="Version Range"]

                serviceDescription [label="Service Description", shape=rectangle]
                serviceDescriptionID [label=<<U>ID</U>>]
                serviceDescriptionProtocol [label=Protocol]
                serviceDescriptionType [label="Type (REST, gRPC)"]

            }


            subgraph cluster_1 {
                label="deployable"
                style=dotted

                isA [shape=diamond]
                includes [shape=diamond]

                application [label=Application, shape=rectangle]
                applicationID [label=<<U>ID</U>>]

                deployInfo [label="Deploy Information", peripheries=2]
                vizData [label="Visualization Data", peripheries=2]
            }
        }

        service -- {serviceID, serviceVersion, serviceName, serviceExtra}

        service -- has [label=1]
        has -- serviceDescription [label="1..n"]

        service -- depends [label=1]
        depends -- versionRange
        depends -- service [label="1..n"]

        service -- predecessor [label=1]
        predecessor -- service [label=1]

        serviceDescription -- {serviceDescriptionID, serviceDescriptionProtocol, serviceDescriptionType}

        application -- {applicationID, deployInfo, vizData}

        application -- includes [label=1]
        includes -- service [label="1..n"]

        application -- isA [label=1]
        isA -- service [label=1]

    }

.. important::

    The :samp:`Service Description` entity in the model describes a :term:`Service Interface`.
```

### Data Model Graph

```eval_rst
.. graphviz::

    digraph G {

        {
            service [label=<<U>Service</U>>]
            serviceID [label=<<U>ID</U>>, shape=plaintext]
            serviceVersion [label=Version, shape=plaintext]
            serviceName [label=Name, shape=plaintext]
            serviceExtra [label="...", shape=plaintext]

            x [shape=point]
            versionRange [label="Version Range", shape=plaintext]

            serviceDescription [label=<<U>Service Description</U>>]
            serviceDescriptionID [label=<<U>ID</U>>, shape=plaintext]
            serviceDescriptionProtocol [label=Protocol, shape=plaintext]
            serviceDescriptionType [label="Type (REST, gRPC)", shape=plaintext]


            application [label=<<U>Application</U>, <U>Service</U>>]
            applicationID [label=<<U>ID</U>>, shape=plaintext]

            deployInfo [label="Deploy Information", shape=plaintext]
            vizData [label="Visualization Data", shape=plaintext]
        }

        service -> {serviceID, serviceVersion, serviceName, serviceExtra} [dir=none]

        service -> x [dir=none]
        x -> service [taillabel="depends on"]
        x -> versionRange [dir=none]

        service -> service [label=predecessor]

        service -> serviceDescription [label=has]

        serviceDescription -> {serviceDescriptionID, serviceDescriptionProtocol, serviceDescriptionType} [dir=none]

        application -> {applicationID, deployInfo, vizData} [dir=none]

        application -> service [label=includes]

    }

.. important::

    The :samp:`Service Description` entity in the model describes a :term:`Service Interface`.
```


## Considered Options

* Relational database:
  + __MySQL__
  + MariaDB
  + PostgreSQL
  + SQlite
* Graph database:
  + Neo4J

## Decision Outcome

Chosen option: The graph database Neo4J, because it fits our data model best.

## Pros and Cons of the Options

### Relational database

* Good, because team already has sql knowledge
* Good, because Spring Boot integrations and ORM for java available
* Good, because sql scheme
* Bad, because sql scheme needs to be defined
* Bad, because data migrations to new database format need to update schema and data

### Graph database

* Good, because applications and services naturally form a graph
* Good, because Spring Boot integrations and OGM for java available
* Good, because node/edge properties are dynamic
* Bad, because new query language
* Bad, because no rigid schema like in sql databases and therefore more necessary checks (e.g. type, exists) in code

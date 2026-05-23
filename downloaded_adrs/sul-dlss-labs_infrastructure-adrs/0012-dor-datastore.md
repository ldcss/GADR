---
layout: default
title: ADR-0012
nav_order: 15
permalink: records/0012/
---
# Replace Fedora 3 with alternative datastore

* Status: drafted
* Decider(s): <!-- required -->
  * Julian Morley
  * Andrew Berger
  * Vivian Wong
  * Tom Cramer
  * Hannah Frost
  * Infrastructure Team
    * Justin Coyne
    * Mike Giarlo
    * Peter Mangiafico
    * Jeremy Nelson
    * Justin Littman
    * Naomi Dushay
    * John Martin
    * Aaron Collier
* Date(s): <!-- required -->
  * drafted: 2021-01-05

## Context and Problem Statement <!-- required -->

As described in [ADR-0001](0001-migrate-off-fedora-3.md)], it is necessary to migrate from Fedora 3 as a repository for DOR metadata. Since the drafting of that original ADR significant progress has been made in isolating Fedora 3 from other SDR systems. In addition, COCINA has been adopted as a data model for DOR digital objects and the Fedora data model has been mapped to the COCINA data model.

The purpose of this ADR is to propose an alternative datastore.

## Decision Drivers

* Support CRUD and querying/indexing of JSON data.
  * Support for fulltext search (for metadata, not binary files) is desirable. (Note: There is not yet a clear use case for this.)
* Support transactions.
* Support for large number of records.
  * Currently 2 million digital objects.
  * Expect significant growth in number of digital objects.
  * Depending on implementation, may possibly have multiple records per digital object.
* Ability to migrate JSON model changes.
* Broad community support for datastore and expected long term viability.
* High availability deployment configurations.
* Local Docker deployment configurations.
* Can be supported by Operations team.
* Robust export support (e.g., if needed to exit the technology)

## Unknowns

There will be requirements for versioning metadata. The requirements for versioning are not fully understood at this time. While it can be assumed that versioning support can be implemented with most datastores (e.g., as implemented for Sinopia with MongoDB), this requires more consideration before making a final selection.

## Considered Options

* MongoDB
* PostgreSQL
* AWS Dynamo
* CouchDB
* ElasticSearch
* Fedora 6

## Decision Outcome

NOT YET.

## Pros and Cons of the Options

### MongoDB

* Pro
  * JSON-native datastore with rich support for CRUD operations and querying.
  * Positive experience using MongoDB for Sinopia.
  * Well documented and broad community support.
  * On-premise and cloud (AWS DocumentDB and MongoDB Atlas) high availability deployment configurations.
    * Note that AWS DocumentDB does not support public endpoints.
  * Docker images available.
  * Built in mechanism for change notifications.
* Con
  * Operations team does not have experience supporting on-premise.
  * Infrastructure team experience with MongoDB is minimal.
* Unknown
  * We do not have direct experience using MongoDB with large number of records.

### PostgreSQL

* Pro
  * Postgres is a performant, scalable, well-tested, open-source solution in wide use.
  * Postgres is the most common replacement for Fedora in the Samvera community.
  * Operations team and infrastructure team have deep experience with PostgreSQL.
  * On-premise and AWS high availability deployment configurations.
  * Docker images available.
* Con
  * JSON support is "bolted on".
    * Our experience (SUL-PUB, RIALTO, TechMD service) is that the JSON support is adequate if storing JSON, but updating or querying JSON data is suboptimal.
    * Keeping data in a JSON field and other fields in sync is complicated.
  * Infrastructure team experience with using PostgreSQL to store JSON is minimal.

### AWS Dynamo

* Con
  * Based on our experience with Taco, the support for JSON is not optimal.
  * AWS only, no on-premise option.

### ElasticSearch

* Pro
  * Strong JSON support.
* Con
  * Not typically used as datastore of record.

### Fedora 6

* Cons
  * Poorly supported.
  * Few users.

## Links

* Supersedes [ADR-0001](0001-migrate-off-fedora-3.md) -->

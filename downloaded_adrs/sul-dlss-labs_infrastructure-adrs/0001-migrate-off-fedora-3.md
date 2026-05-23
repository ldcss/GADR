---
layout: default
title: ADR-0001
nav_order: 4
permalink: records/0001/
---
# Replace Fedora 3 with Alternative Metadata Store

* Status: superseded by [ADR-0012](0012-dor-datastore.md)]
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
  * drafted: 2019-11-06

## Context and Problem Statement <!-- required -->

Fedora 3 is unsupported and has been unsupported for four years; it is unlikely to be supported in the foreseeable future. It also requires a difficult-to-support version of the Java Virtual Machine. And yet, Fedora 3 is the cornerstone of our management "repository," in which all SDR content is managed and from which said content flows to access and preservation environments. At the same time, there is a dwindling number of organizations in the cultural heritage community who are still using Fedora 3.

## Decision Drivers <!-- optional -->

* Fedora 3 is unsupported and unlikely to be supported
* Fedora 3 will be harder to install on newer operating systems
* The Fedora 3 data model is not inherently validatable
* The Fedora 3 community is disappearing, so we are increasingly going it alone
* Fedora 3 is a critical piece of SDR infrastructure and represents an enormous risk
* Samvera software that supports Fedora 3 is outdated and maintained/supported only through our own efforts, preventing us from using mainstream Samvera software
* We have (unverified) concerns about the scalability of Fedora 3

## Considered Options <!-- required -->

* Do nothing
* Keep using Fedora 3 & DLSS Infrastructure Team takes over maintenance of Fedora 3 and Fedora 3-supporting software in Samvera community
* Replace Fedora 3 as a metadata store with PostgreSQL
* Replace Fedora 3 with latest Fedora version

## Decision Outcome <!-- required -->

No decision made yet. See status field above.

## Pros and Cons of the Options <!-- optional -->

### Do Nothing

* Pro
  * Less work (for now, until it falls apart)
* Con
  * See decision drivers above.

### Maintain Fedora 3

* Con
  * See decision drivers above.
  * Lack of resources and time to absorb Fedora 3 into our portfolio
  * Lack of expertise with Java development
  * Completely out of step with community trends

### Replace Fedora 3 as a metadata store with PostgreSQL

* Pro
  * Postgres is a performant, scalable, well-tested, open-source solution in wide use
  * Postgres is the most common replacement for Fedora in the Samvera community, now that Valkyrie is catching on
  * Postgres supports both schemaless data (JSON) and schema-based data, with built-in indexing, relationships, and transactions
  * Should we decide to make more use of cloud-based hosting services, Postgres is easier to support and most cloud providers have a native Postgres-backed service (for cost reduction)
  * Peer institutions such as Princeton, Northwestern, and BPL are using Postgres
  * Postgres works well with ActiveRecord and other Rails patterns (assuming we stay with Rails)
* Con
  * Fedora functionality missing in Postgres includes "object" versioning (and services pertaining to binaries, which DOR does not use)
* Note (leaning toward Pro)
  * Postgres incentivizes changing our metadata model to be based on JSON (see also: COCINA data model)

### Replace Fedora 3 with latest Fedora version

* Pro
  * Continuing to use Fedora keeps us aligned with the broader repository community (Islandora/Fedora), though perhaps not with Samvera community trends
* Con
  * Fedora has many fewer users and maintainers than Postgres
  * There is a significantly smaller set of tools that interoperate with Fedora (and RDF) compared with Postgres (and JSON and/or relational data)
  * Fedora has proven to be challenging for new developers to become conversant with, especially compared with relational databases like Postgres
  * Fedora lacks transactions, necessitating quasi-transactional functionality at higher layers, which means more code to maintain and opportunities for errors
  * Fedora 4+ still has scalability concerns, and we have no reason to believe Fedora 5 or 6 are/will be any better
    * And it is unclear how similar future versions of Fedora will be to Fedora 4.
  * Fedora is not known to be natively supported by any cloud providers, meaning custom work if we move infrastructure to the cloud
  * Fedora does not provide querying of relationships natively; requires a sidecar index such as Solr which complicates the architecture
* Note (leaning toward Con)
  * Fedora 4+ incentivizes changing our metadata model to be based on RDF

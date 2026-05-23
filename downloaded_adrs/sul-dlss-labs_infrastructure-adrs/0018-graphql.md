---
layout: default
title: ADR-0018
nav_order: 21
permalink: records/0018/
---
# Efficient retrieval of Cocina objects

* Status: accepted
* Decider(s):
  * Andrew Berger
  * Infrastructure team
* Date(s):
  * Accepted: 2023-09-01

## Context and Problem Statement

This work is motivated by improving performance in Argo, especially for cocina objects with large numbers of files. A cocina object with 5000 files was timed at 12 seconds to render in Argo. This is due to:

* The time taken to retrieve the object from the database (timed at 3.5 seconds).
* The time to instantiate and validate the cocina object in both DSA and Argo.
* The time to send the cocina object over the network.
* Argo making 5 requests for a cocina object to render a single item details page.

## Decision Drivers

* The performance improvement for rendering cocina objects in Argo.
* The amount of new machinery / infrastructure that must be put into place to address the problem.
* The opportunity to reuse new machinery / infrastructure to address other use cases.

## Considered Options

* Add a Graphql endpoint to DSA to support partial retrieval
* Extend the existing REST endpoints to support partial retrieval
* Caching of cocina objects by Argo

Partial retrieval improves performance by only retrieving the large parts of the cocina object (viz., the structural) when needed. A partial improving strategy requires changes to the cocina models gem to allow cocina objects to omit required attributes.

Caching improves performance by reducing the number of times that a cocina object must be retrieved.

## Decision Outcome

Add a Graphql endpoint to DSA because:

* Partial retrieval is a core feature of Graphql.
* Graphql has a well-supported Rails engine (ruby-graphql), so adding it to the DSA Rails app was not a significant burden.
* Graphql has the possibility to be re-used to address other use cases.

### Positive Consequences

Using a Graphql endpoint reduces the rendering of a cocina object with a large number of files to under a second.

### Negative Consequences

An additional component was added to DSA, which is already a large codebase.

## Pros and Cons of the Options

### Add a Graphql endpoint to DSA to support partial retrieval

A Graphql endpoint allows a client to request only the parts of a cocina object that are needed. In turn, the Graphql server only retrieves the requested parts from the database.

* Pro: Partial retrieval is a core feature of Graphql.
* Pro: Graphql has a well-supported Rails engine.
* Pro: In the future, Graphql may address other possible use cases, including patching cocina objects (instead of the current approach of updating an entire cocina object) and providing a facade over multiple APIs / services (to reduce the number of calls that are required to retrieve all of the data for a cocina object, reduce client complexity, and make it easier to split out services).
* Con: Requires adding an additional component to DSA.
* Con: Infra team is not familiar with Graphql.
* Con: ruby-graphql is split into a free/pro versions. As our usage increases, it may be necessary to license the pro version (similar to our licensing of sidekiq pro).

### Extend the existing REST endpoints to support partial retrieval

* Pro: Does not require adding additional components to DSA.
* Con: Does not address other possible use cases.

### Caching of cocina objects by Argo

Rails integration with caching solutions provides approaches for caching cocina objects to minimize the number of requests made to DSA.

* Pro: Confines changes to Argo.
* Pro: Uses machinery that is already part of Rails.
* Con: Because of the way that Argo is deployed (multiple processes on multiple servers), the recommended approach is to use memcache. However, a memcache system is significant infrastructure and is not supported by Ops.

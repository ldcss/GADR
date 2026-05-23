# 6. use-mongodb

Date: 2020-08-21

## Status

Accepted

## Context

Dalmatian configuration is sourced directly from AWS so that the latest
information can be worked against when running this app locally.

Each time we start the local server a new YML file is created. When the server
is restarted the contents are always thrown away and treated as ephemeral.

We need a structured way to query and mutate data within the app that is not
passing around the same YML file all the way through the application. Having
resources allows us to build a more conventional Rails app with restful routing.

The structure of dalmatian.yml is fragile. There is no shared schema, versioning
or domain model to allow us to set robust expectations upon its interface.
It is subject to change from the upstream of Dalmatian Core, for which this app
seeks to provide helper support for. The Dalmatian config file (dalmatian.yml)
is likely to change to meet the needs of Dalmatian Core. If this app depends on
the structure of this YML file rigidly the tool risks being overly brittle and
breaking whenever the structure changes.

Rails applications are provisioned by default with Postgres as a relational
database. There would be overhead in creating and maintaining a schema to
support a structure that we have no direct control over from this application.

In the past when dxw have used a document store, Mongodb and the Mongoid gem
have served well. Given we do not plan to host the application the choice of
tool has less impact, though we could externally host or spin up a mongo
container should we choose to.

## Decision

Use MongoDB for Dalmatian data instead of Postgres and ActiveRecord.

## Consequences

- We will be able to quickly convert the contents of the dalmatian.yml into Mongo
without having to construct a careful schema first
- We will be able to turn on Mongo DynamicFields which will automatically add new
fields to the object representation, lowering the surface area of breakages
- New fields that are found in dalmatian.yml should not cause a break but will
still require a code change before they are used. Extending should be ok
- If a field that this service was depending on is removed from dalmatian.yml
this application will start erroring. This choice does not remove the need to
manage how breaking changes to dalmatian.yml are made

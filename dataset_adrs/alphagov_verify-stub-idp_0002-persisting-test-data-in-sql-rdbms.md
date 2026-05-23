# 2. Use dropwizard functionality to secure API

Date: 2018-02-15

## Status

Accepted

## Context

We need to be able to persist test data for users of Stub IDP.

Currently we use Infinispan to store user data so that RPs can configure
their own users in the Stub IDPs we create for them and a YAML file for
storing federation config for Stub IDP. We cannot deploy Stub IDP to PaaS
with Infinispan so we need to move the user data into a persistent
data store and eventually move the fed config into a database as well.

## Decision

We decided to use PostgreSQL RDBMS because it is currently best
supported RDBMS on PaaS.

We also decided that the data about the users is saved as JSON in the DB.
This might change in the future once we know what the eIDAS integration
requirements will be.

As a start, we are going to be using the following data model:

![Stub IDP ER Model](images/ida-stub-idp-er-diagram.png?raw=true "Stub IDP ER Model")

The "data" field in the "users" table is where the user data will be saved
in JSON format. The object structure will be the same as the object
currently saved to Infinispan.

## Consequences

We'll be able to persist users data which can survive system restarts.

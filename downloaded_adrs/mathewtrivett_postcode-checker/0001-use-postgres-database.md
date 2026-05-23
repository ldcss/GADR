# Use Postgres as our database

## Context

Our postcode checker uses a database to store valid service areas and allowed post codes.

Currently our requirements involve looking up a postcode using the [postcodes.io](https://postcodes.io).

In future we may want to build features that involve more sophisticated geolocation capabilities. Most databases do not support geolocation natively.

Postgres is the most geolocation capable SQL database. In future we can enable the PostGIS extension.

## Decision

We will use Postgres for our database.

## Status

Accepted

## Consequences

Postgres is a mature and widely adopted open source database. It serves our immediate needs. Using Postgres allows us to enable more complex geolocation features in the future using the PostGIS extension.

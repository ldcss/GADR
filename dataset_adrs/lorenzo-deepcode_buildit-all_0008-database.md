# 8. Database

Date: 2017-12-27

## Status

Accepted

Amended by [9. Use JPA](0009-use-jpa.md) - originally used JDBC

Amended by [10. JPA manages schema](0010-jpa-manages-schema.md) - originally managed via schema.sql & data.sql and reset each deploy

## Context

Bookit needs to persist the locations, bookables, and bookings so that the data survives multiple instances and deployments over time.

## Decision

* Use SQL approach as opposed to NoSQL solution - the model is simple and ACID transactions keep multiple users separate
* Use H2 for unit testing & local development - speeds up execution time and reduces external dependencies
* Use AWS RDS Aurora (MySQL) for integration/staging/production - better HA & continuous snapshots (enabled for production)
    * Use MariaDB JDBC driver - has native Aurora support for failover

## Consequences

* At the time, Aurora support for PostgresSQL was in Preview
* We originally used Derby but the SQL syntax was a bit different than what MySQL supported.  H2 allowed us to share schema.sql and data.sql across both database implementations
* After implementation, AWS announced RDS Aurora "serverless" - potentially move there down the road
* MySQL doesn't appear to have robust support for local datetimes

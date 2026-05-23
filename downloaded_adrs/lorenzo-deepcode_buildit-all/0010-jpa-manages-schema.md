# 10. JPA manages schema

Date: 2017-12-27

## Status

Accepted

Amends [8. Database](0008-database.md)

## Context

Originally, we used Spring Boot's Database Initialization support to automatically create and intialize our database via schema.sql and data.sql scripts.  Each deployment (application initialization) would execute these scripts.  Our implementation would drop the database and recreate it each time.  While this accelerated our development (avoid data migrations), it's not sustainable

## Decision

* Leverage Hibernate's (our JPA implementation) ddl-auto feature to update the staging/production databases (we will continue to drop/recreate all other databases....local, integration).
    * recreating in integration ensures a clean database for each run.  In addition, it validates that we can recreate a database from scratch

## Consequences

* Hibernate does warn against utilizing this feature "in production."
* We can "test" the update in staging.  There is a risk that Hibernate updates a schema naively which may result in dropped data
* This approach won't address how we can add static data (locations & bookables for now) over time.
* Hibernate won't drop columns that are no longer used.  Add only.  
* Also won't migrate data for you.  Schema only.
* If any of the above prove onerous, we can address by introducing a database migration tool such as Liquibase or Flyway.
* This did cause us to hit a memory limit (previously set to 256MB).  Had to bump to 512MB.

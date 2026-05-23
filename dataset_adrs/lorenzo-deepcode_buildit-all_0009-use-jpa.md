# 9. Use JPA

Date: 2017-12-27

## Status

Accepted

Amends [8. Database](0008-database.md)

## Context

Originally, we utilized a Spring's JdbcTemplate to quickly CRUD our entities against the data store.  While this was quick and easy, we did most of our filtering in the application as opposed to SQL WHERE clauses.  As we continued, each addition to our entities required a lot of boilerplate code.  

Spring has great JPA support and Boot uses Hibernate out of the box.  Our entity models are still relatively simple, but using JPA reduces a lot of the boilerplate code, and opens up a lot of additional features "for free."  Specifically, we can utilize JPA to manage our schema updates (naively, later if we need something more robust we can look to Liquibase or Flyway).  It also simplifies joins, where clauses, and gives us more database independence.

## Decision

* Use JPA to map objects into database tables
    * Use Hibernate as the JPA implementation - Spring Boot's default
* Leverage Spring Data's JPA support to implement queries via Repository interface patterns

## Consequences

* While the tests will ensure the code is correct, we will need to ensure the code performs appropriately and does not encounter N+1 or combinatorial query explosion.
* Will still need to figure out the best approach to support our local datetime overlapping interval logic in WHERE clauses
* Consider utilizing Spring Data's RestRepository support to expose repositories directly (very fast time to market, should have started with this)

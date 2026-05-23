# PostgreSQL as the RDBMS

Date: Thu Sep 19 21:42:04 CEST 2019

## Milestone

0.1.0

## Context

For the project a RDBMS need to be chosen and adopted.

## Decision

- [PostrgreSQL](https://www.postgresql.org/) will be the relational database management system of choice.

## Consequences

Why:

- Open source.
- Free.
- Available for many operating systems.
- Its SQL implementation closely follows ANSI standards.
- Widely used and well documented, so finding help is no issue.
- Supported by many platforms for deployment (Amazon, Azure).
- Official docker support.
- For my use case, a very simple database, this looks so appealing, fast and easy to use.

Why not:

- Not the bleeding edge technology.
- Not the fastest DBMS
- Not so much adopted in the commercial world.

## References (optional)

- [Official Website](https://www.postgresql.org/)
- [SQLite vs MySQL vs PostgreSQL](https://www.digitalocean.com/community/tutorials/sqlite-vs-mysql-vs-postgresql-a-comparison-of-relational-database-management-systems)
- [Wikipedia](https://en.wikipedia.org/wiki/PostgreSQL)

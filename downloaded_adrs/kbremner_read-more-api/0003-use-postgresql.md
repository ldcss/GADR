# 3. Use PostgreSQL

Date: 2017-09-24

## Status

Accepted

## Context

A particular database technology needs to be chosen for the storage of data.

Historically Microsoft's SQL Server has been the default choice for ASP.NET applications. SQL Server could only be run on a machine running Windows until the release of SQL Server 2017.

PostgreSQL is a popular choice for use with other web frameworks (i.e. Rails) and is widely used on a range of platforms, including Linux, MacOS and Windows.

PostgreSQL is open source and free to use for commercial use. SQL Server has a free version for development purposes but require the purchase of a license for commercial use.

## Decision

We will use PostgreSQL for the storage of data.

## Consequences

No license purchase is required to run the application in production.

The database can be run on a machine running Linux, MacOS or Windows.

An additional dependency is required to allow the application to connect to a PostgreSQL database (Npgsql).

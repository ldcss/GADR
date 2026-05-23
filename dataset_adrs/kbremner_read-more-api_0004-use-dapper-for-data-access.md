# 4. Use Dapper for Data Access

Date: 2017-09-24

## Status

Accepted

## Context

Many ASP.NET applications use [Entity Framework (EF)](https://docs.microsoft.com/en-us/ef/), an Object Relational Mapper (ORM) that helps access data stored in database.

EF allows data in a database to be accessed by extending a DbContext class and adding properties to this extending class of type DbSet. DbContext and DbSet provide methods for performing basic CRUD operations against entities in a database that are defined in model classes. These model classes contain annotations that define the table name, columns and relationships with other entities. When a query is performed, EF handles creating instances of model classes and filling them with the received data.

Some properties are lazily loaded, with the queries related to fetching the required data only being run when thoses properties are accessed. This approach is commonly used when accessing a property representing a relationship with another entity.

A DbContext by default tracks changes to entities returned as the result of queries, with changes being saved when a call is made to a DbContext's SaveChanges or SaveChangesAsync methods.

The DbContext and DbSet classes provide methods that can be used to fetch data, with the ability to apply limitations on what data is returned. EF will generate the required query, execute it, parse the response data and return the appropriate entity model instances.

EF supports migrations written as classes with Up and Down methods, to support upgrading and rolling back, respectively. These methods are implemented by adding calls to a provided MigrationBuilder instance.

Dapper is a library that is commonly referred to as a "micro-ORM". It provides methods to support executing SQL queries and parsing the results to create instances of particular model classes. Unlike EF, Dapper does not support the tracking of changes and queries must be written using SQL.

Dapper was developed for the StackOverflow website to address performance issues, as outlined in [this blog post](https://samsaffron.com/archive/2011/03/30/How+I+learned+to+stop+worrying+and+write+my+own+ORM).

## Decision

We will use Dapper with the [repository pattern](http://blog.mantziaris.eu/blog/2016/10/24/the-repository-and-unit-of-work-pattern/) to access data stored in the database.

## Consequences

Queries and migrations will need to be written in SQL.

A mechanism for handling migrations will need to be implemented.

The use of the repository pattern decouples the business logic from the Data Access Layer (DAL), allowing for Dapper to be easily replaced with an alternative DAL in the future, if required.

Dapper reduces the "behind the scenes" complexity involved in accessing data, making it easier to debug issues with particular queries.

As Dapper does not track changes or support lazy loading of properties, Dapper can, in some circumstances, provide performance improvements over EF.

The retrieval of entities related to a particular entity will have to be performed either at the point of retrieving the original entity or via another method. Lazy-loaded properties for relationships is not supported.
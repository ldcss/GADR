# 12. Place immutability logic behind repository facades

Date: 2022-04-19

## Status

Accepted

## Context

Maintaining immutable database records has added some complexity which has polluted the service layer with lots of code that isn't directly related to the business rules. This mixture of code required for maintaining immutability combined with the business logic is confusing and blurs the boundary between the two.

## Decision

We will create a new abstraction layer of `RepositoryFacades` which will contain any complexity required to keep the database in order, keeping this separate from the business logic in the service layer. These facades should behave as CRUD repositories and the caller should be able to call the save methods without concerning themselves with whether a given entity is immutable or not. Read methods should return a fully populated entity with all relational links established. 

## Consequences

- The service layer should now be primarily calling `RepositoryFacades` rather than the `Repositories`
- When writing code to manage database state this should be created in a `RepositoryFacade`
- This will provide a clear distinction between database management logic and business logic

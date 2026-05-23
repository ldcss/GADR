# ADR 013: Query language enhancements

## TL;DR

## Context
The following minor language improvements need to be made:
* querying by number explicitly for a field
* querying by text match vs an exact term match 
* generic NOT support

## Decision
To support these, `QueryHandler` needs to have a `DataTypeInfo` instance to figure out what type each field is. This has some knock-on effects in parsing a string into a query.

In order to make testing simpler, `DefaultQueryHandler` will remain `DataTypeInfo` agnostic and a new sub-class `DataTypeAwareQueryHandler` created which uses an internal `DataTypeInfo` to figure out the type. 

The main place where this comes in is in `FetchParams` which transforms a string into a list of `Query` objects. This functionality will be shifted out of the `FetchParams` object and into a generic `SearchBasedService` method.

In addition, `FieldType` and `QueryType` have now converged so that `QueryType` can be retired. This means that some of the query builders will need updating to deal with things like `GENOME`, `ID` and `ONTOLOGY`.

`Query` now also has a `not` property so that a query handler can decide if a query is "not" or not. The search implementation should deal with this.

## Status
Under development

## Consequences

## Tags

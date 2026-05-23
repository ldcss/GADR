# ADR 007: Variant search

## TL;DR

A Search instance has been provided that supporting querying the EVA Mongo database, as have endpoints using that search.

## Context

We need to be able to search the EVA database for variants related to genes in our databases. The EVA REST API is currently too limiting in what it returns and can quickly overwhelm the client so the Mongo database provides a reasonable level of access.

## Decision
We have implemented the following endpoints:
* `MongoSearch` - a generic Search implementation using `MongoSearchBuilder`. This is tested using Fongo, a "fake" Mongo in memory implementation
* `VariantSearch` - a join/merge implementation using `MongoSearch`
* Variation endpoints (query, fetch, info, object) using `VariantSearch`

MongoDB differentiates between nested hashes and nested arrays, and requires different filter syntax (`$elemMatch`). In order to accommodate this, field names are appended with `-list` to indicate that they are arrays. The `-list` suffix is removed when creating filters and projections. For instance:
```
{
annot:{
  ct:[
  	{ensg:1, so:2},
  	{ensg:3, so:4}
  ]
}
}
```
To query for elements in `annot.ct`, `MongoSearchBuilder` interprets `annot:{ct-list:{ensg:1, so:2}}` as a query to sub-field `annot` and then to elements in the array `ct`. In Mongo terms, this is:
```
{ "annot.ct" : { "$elemMatch" : { "ensg" : "OS01G0100100", "so" : 1631 } } }
```
These name changes are shown in the corresponding `FieldInfo` objects.

Further more, MongoDB differentiates between '1631' and 1631, whilst our generic JSON parser does not. This means `MongoSearchBuilder` needs to inspect fields and add them to the filter document as `Double` if they are purely numeric.

## Status
Under development

## Consequences
The current Mongo search implementation does not support counts, facets or sorts. These need to be investigated.

We need support for counts from the join mechanism.


## Tags
Search, MongoSearch, VariantSearch

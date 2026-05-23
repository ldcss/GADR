# ADR 001: Transformation of results to arrays

## TL;DR
We need to support returning results as 2d array, not arrays of hashes - implemented as a toggle to force reformatting on the endpoints.

## Context
Developers from BioConductors pointed out that the current format of data returned as hashes e.g.
```
results:[
   {id:"123", "name":"xyz", genome:"homo_sapiens"},
   {id:"456", "name":"abc", genome:"homo_sapiens"},
   {id:"890", "name":"def", genome:"homo_sapiens"}
]
```
would be better returned as:
```
results:[
   ["123", "xyz", "homo_sapiens"],
   ["456", "abc", "homo_sapiens"],
   ["890", "def", "homo_sapiens"]
]
```
This would be better for several reasons:
* smaller payload
* client would probably need to do this (esp for R) so why not do it already
* might work better with tabular views (CSV, web interfaces)

However, this is not a universally desirable result - the gene documents are inherently nested so we would want to support both approaches.

This might be applied at a variety of levels, but is best done as far away from the interactions with ES etc as possible.

## Decision
We will implement this as an option for `FetchService` and `QueryService` endpoints with a defined toggle parameter array=true/false. The services will then reformat the data accordingly, but the underlying searches will return data in the same format.

## Status
Beta

## Consequences
* The implementation we've chosen will be relatively unobstrusive
* There may be an impact on performance - on the fly re-mapping adds a certain level of computational load, which will need to be assessed.
* Column headers are essential for a client to make sense of this data. This has already been implemented so that `fields` is returned by both `query` and `fetch` endpoints.
* If this is generally used, it might become the default.
* Will not work with subfields unless target is used to flatten

## Tags
QueryResult, QueryService, FetchService, format

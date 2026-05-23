# ADR 002: Improved support of field specification

## TL;DR
We need to improve how output fields are specified as we start to combine data from multiple searches in results. This will be done with a specialised object

## Context
As we start pulling back data from multiple searches, we run the risk of ending up with multiple parameters (fields, targetFields, targetFields2 etc. etc.)

A better approach is to pass in specifications using a nested hash or similar so fields can be targeted to individual searches e.g.
```
{
"genes":["id","name","description"],
"variations":[""]
}
```

However, for simplicity, this needs to support simple field specifications too e.g.
```
["id","name","description"]
```
or even
```
"id","name","description"
```

## Decision
Mixing arbitrary arrays and hashes in Java is not well supported and requires casts etc. We will instead create a specific class, `org.ensembl.genesearch.QueryOutput`, capable of representing this kind of nested structure.  `build()` methods will be provided to support parsing various specifications.

## Status
Beta

## Consequences
`Search` and all implementing classes will need to switch from specifying fields as strings to supplying one of these objects.

## Tags
Search, JoinAwareSearch, GeneSearch, QueryOutput

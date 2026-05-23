# ADR 003: Search interface refactor

## TL;DR
Now that we can support targets in both Query and QueryOutput, target and targetQueries will be removed so that for join queries, both to and from queries and fields will be represented in the normal query and field arguments.

## Context
Query and QueryOutput example for simple query:
```
q={"name":"BRCA2"}
fields=["id","name","genome"]
```

Query and QueryOutput example for transcript join:
```
q={"name":"BRCA2"}
fields=["id","name","genome",{"transcripts":["id","seq_region_start"]}]
```

Query and QueryOutput example for sequence join:
```
q={"name":"BRCA2","sequences":{"type":"protein"}}
fields=[{"sequences":["id","desc","seq"]}]
```

One consideration is whether searches should need to have the default search type specified in the queries and fields e.g.
```
q={"genes":{{"name":"BRCA2"}}
fields={"genes":["id","name","genome"]}
```

The best idea here is to use different endpoints for different searches e.g. `/api/genes` to get genes, `/api/variations` to get variations etc.

## Decision
We have decided to remove target and targetQueries from the interface as they will rapidly become unsustainable as the range of joined queries increases. At present, the "default" search will not require a separate section.

## Status
Beta

## Consequences
`Search` and all implementing classes will need be be refactored to use QueryOutput and Query instead of targetFields and target. JoinAwareSearch will need a comprehensive overhaul.

## Tags
Search, JoinAwareSearch, GeneSearch, ESSearch, SequenceSearch, DivisionAwareSequenceSearch

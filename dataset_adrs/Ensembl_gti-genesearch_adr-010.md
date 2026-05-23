# ADR 010: Inner joins

## TL;DR

JoinMergeSearch has been extended to support "inner-join" style queries where a result set is restricted to those objects which have a corresponding object in a joined search (e.g. genes with matching variants)

## Context


## Decision
The simplest approach is to create a new query to use in "from" instead e.g.
```
search a:
x:1, b:{c:2}
where b is a separate dataset joined by a.n to b.m
step 1:
find all a.n where a.x=1 -> list[a.n]
step 2:
query b for b.n=list[a.n] and b.c=2 and retrieve b.m -> list[b.m]
step 3:
query is now n:list[b.m], b:{c.2}
```
However, since there may be n-m relationships between the joined objects, you still need to retain the original "from" query (`x:1` in this case).

This has been implemented in `JoinMergeSearch.innerJoinQuery` which creates a new query and inserts into into a new instance of `SubSearchParams` which is then passed to the standard join query mechanism (now abstracted out into ).

These new methods are now used by `query` and `fetch`, and are triggered by `isInnerJoin` which returns true if the request is for an inner join. Currently, this is triggered with the magic field `inner` in the "to" query e.g. `{variants:{inner:1, annot:banana}}`. This magic field is stripped from the query before execution.

## Status
Under development

## Consequences
`inner` cannot be a field in a joined query. Perhaps some other form of encoding is needed here.

Note that `count` is an output field, but `inner` is a query field. Logically, this makes sense, but there may be a better way of doing this.

## Tags
Search, JoinMergeSearch, SearchType

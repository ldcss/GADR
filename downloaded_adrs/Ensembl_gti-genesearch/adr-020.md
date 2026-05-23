# ADR 018: Range-based inner joins

## TL;DR
htsget requires an inner join to only show genes which have matching variants. This has been implemented as a post-query filter.

## Context
`JoinMergeSearch.queryWithRangeJoin` and `JoinMergeSearch.fetchWithRangeJoin` now accept a boolean `inner` argument. If this is set, the "from" row is retained in the results or sent to the consumer respectively.

## Status
Testing

## Consequences
Counts will be inaccurate as they cannot be calculated without joining from every element in the set. In this case, the result count is set to -1 as a placeholder indicating no accurate count is available.

## Tags

# 6. Batch Loading

Date: 2020-12-18

## Status

Proposed

## Context

Like many database systems, MongoDB supports batch updates to data that are
significantly faster than individual updates. In some cases when loading data,
we must do many updates to a particular document. If we need to search for and
deserialize the document each time, the load operation may suffer from a
polynomial slowdown -- that is, each update takes progressively longer as the
document grows in size.

## Decision

When loading data, we should perform all updates to a given document at the
same time. In particular, we should minimize the number of times we deserialize
any given cluster.

## Consequences

This increases overall complexity of the system, but allows loading data in a
timely fashion especially for large clusters.

For best performance, input data should be sorted by OCLC control number (OCN)
before loading into the system. This may require additional complexity in the
management of the data files loaded into the system. In particular, for best
performance, holdings from multiple institutions should be sorted together by
OCN and loaded at the same time. The system can still handle unsorted data, it
just has the potential to be significantly slower. This is likely to be more
important for an initial load or full reload than for incremental updates.

When data is sorted this way, the most frequent write operation is adding
multiple subdocuments to a given document - for example, adding multiple
holdings for a given OCN to its cluster. To ensure the updates happen in the
most performant way for MongoDB, we call the MongoDB `$push` operation with all
the subdocuments directly. This also allows us to ensure that the write
operation completes successfully (see ADR #0005).


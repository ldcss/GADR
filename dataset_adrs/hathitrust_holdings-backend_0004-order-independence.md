# 4. Order Independence

Date: 2020-05-05

## Status

Accepted

## Context

The new print holdings system has a persistent backend to which we build
incrementally. Data updates from any source may come at any time. Since data is
loaded incrementally, effects based on the order in which data is loaded could
have substantial long-term effects. It would also be very difficult to
understand and debug concrete state that depended on a past state.

In the current system, for holdings records with multiple OCNs the OCN is set
once at scrub time and retained until the member re-sends holdings data.  The
chosen OCN is dependent on what items are in the repository at the time the
data is scrubbed. This causes a potential issue where:

- a member submits a holding record with multiple OCNs
- if no OCN matches a HathiTrust item, the first OCN is used
- a HathiTrust item matching one of the OCNs is later ingested
- if it matches an OCN other than the first one, it will still not match the member holding

An option to avoid this would be to require that members submit only one OCN
per holding, but there are sometimes valid reasons to submit multiple OCNs
(e.g. bound-withs, deprecated OCNs, etc).

The current holdings validation/normalization process also checks the current maximum
OCN using an OCLC API:

```bash
curl -s "https://www.oclc.org/apps/oclc/wwg" | egrep -o '"oclcNumber":"[0-9]+"' | egrep -o '[0-9]+'
```

## Decision

The concrete state of the database should depend only on the data that was
loaded, not on the order in which it was loaded.

This particularly includes (but is not limited to) the clusters that data items
(OCNs, holdings, HathiTrust items, shared print commitments) are attached to.

This decision may be revisited if a situation arises that makes it infeasibly
expensive or impossible to maintain strict order independence, but the
consequences of breaking that must be documented and well-understood.

## Consequences

Scrubbing and normalization processes should depend only on the data in the
file, not on the state of other data in the system that could cause different
results based on the state of that data.

Reliance on data truly external to the system is acceptable, but the state of that data 
at the time of processing must be retained with the input data such that the process can
be replicated later. (The reliance on the "current maximum OCN" falls in this category)

There should be automated tests that ensure so far as feasible that:

- Swapping the order in which any two pieces of data are loaded should result
  in the same result

- Deleting and re-adding a piece of data should not cause changes

This also implies the need for careful thought about validation and
normalization of the concordance file to ensure that clusters do not change
based on the order in which the concordance file is loaded.

In deciding on implementation options, we should prefer options that make it
easier to maintain ordering independence.

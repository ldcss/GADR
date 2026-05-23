# 5. Concurrency

Date: 2020-12-18

## Status

Proposed

## Context

Loading holdings data to MongoDB is largely CPU bound. For optimal performance
when loading data, we want to have multiple processes or threads loading data
simultaneously.

Because of the possibility for clusters to split or merge while loading data on
HathiTrust items or concordance data, loading data in parallel suffers from a
number of concurrency hazards. In particular, it is possible for one process to
attempt to update a document which has been deleted by another process or which
is about to be deleted and reclustered by another process.

MongoDB does not support proactive locking of individual documents, but it does
support transactions which can detect conflicts between updates to documents
involved in multiple simultaneous transactions.

## Decision

* Wrap any operation that suffers from potential write conflicts in
retryable transactions.

* Ensure that update operations modify the expected number of documents; retry
  operations that do not.

* Test handling of concurrency hazards.

## Consequences

Underlying MongoDB update operations return information on the number of
modified documents, but the ActiveRecord-style Mongoid interface does not
expose this information. Write operations therefore must call MongoDB
operations directly rather than using the Mongoid interface.  When this
involves adding sub-documents, extra work is necessary to ensure the
associations between the parent document and sub-document are reflected in
Mongoid.

This increases overall complexity of the system, but with the current
configuration of MongoDB allows us to speed up loading by 8-10x over a single
thread. That performance improvement may not be necessary for incremental
loads, but is the difference between being able to reload all data in the
system over a few days vs. several weeks.

Implementing retryable transactions also increases overall resilience of the
system - even in the absence of routine use of concurrency it is still useful
to verify that updates completed as expected and retry them if not.

Testing concurrent operations relying on specific ordering can be difficult.
The approach that `concurrency_spec.rb` takes is to synchronize operations
between threads is to to wait for the presence of a specific file on the file
system before continuing.

Note that even with transactions enabled, reports and analysis
should not be run while data is being loaded as the results will not be
consistent.

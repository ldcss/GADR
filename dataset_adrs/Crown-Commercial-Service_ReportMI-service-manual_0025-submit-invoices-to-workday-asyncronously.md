# 25. Submit invoices to Workday asynchronously

Date: 2018-11-07

## Status

Proposed

## Context

As discussed in [ADR-0023][adr-0023] and [ADR-0024][adr-0024], Report MI will be moving from generating a
regular file extract to using the Workday API for creating management fee
invoices.

As we move to using the API, it becomes less important to batch up the creation
of invoices, and we can move towards a more real-time operation.

The generation of invoices is not part of the critical-path of a management
information submission, so the creation of it shouldn't block or slow down the
experience of suppliers making their return.

As a result, the process for generating the invoice and submitting it to Workday
should happen asynchronously from the rest of the submission.

The best way of achieving this is to add completed tasks to a queue, and have
the API interaction undertaken by a worker.

## Decision

The creation and submission of invoices to Workday will happen asynchronously
using a queue/worker pattern.

When a supplier task is completed, Report MI should add it to a queue. A worker
should read from the queue, generate the invoice and submit to the Workday API.

If the Workday API is unavailable, or an error occurs, the submission should be
retried. After a (to be defined) number of retries, this should be reported for
investigation.

## Consequences

Report MI will need to produce the queue/worker process and define how errors are handled.

[adr-0023]: 0023-workday-integration-principles.md
[adr-0024]: 0024-use-workday-api-to-manage-invoicing.md

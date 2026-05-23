
# Use architecture decision records (ADR) to document architectural decisions

## Context

A way to document and track my design choices is needed, for myself in order to see how project architecture is changing.

## Decision

I will use ADR to document any important architectural decisions I make.

ADRs will be checked into the repository as numbered md files in the folder docs/architecture/adr

I will follow the template described [here](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions)

All Records will contain, Title, Context, Decision, Status and Consequences

If a decision is changed or overruled we don't delete the record, but change the status accordingly (to superseded or deprecated).
If a decision is superseded or deprecated we should add a link to the new decision. In the format Superseded by [link]

## Status

Accepted

## Consequences

Important design choices and the reasons for them will be visible to all developers.

# OPM1: Use ADRS for decision tracking
Date: 2021-01-28

## Status
Accepted

## Context
A microservices architecture is complex and we'll need to make many decisions.
We'll need a way to keep track of the important decision we make, so that we can revisit and re-evalute them in the future.
We'd prefer to use a lightweight, text-based solution so that we don't have to install any new software tools.

## Decision
We've decided to use [Michael Nygard's lightweight architectural decision record (LADR)](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions) format.
LADR is text based and is lightweight enough to meet our needs.
We'll keep each LADR record in its own text file and manage the files like code.

We also considered the following alternative solutions:
* Project management tooling (not selected, because we didn't want to install tools)
* Informal or "word of mouth" record keeping (not reliable)

## Consequences
* We'll need to write decision records for key decisions
* We'll need a source code management solution to manage decision record files

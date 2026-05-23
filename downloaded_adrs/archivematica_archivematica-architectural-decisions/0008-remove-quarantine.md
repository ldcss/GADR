---
layout: page
status: accepted
adr: "0008"
title: Remove quarantine
deciders: Jesús García Crespo, Sarah Romkey
date: 2019-10-13
---

## Context and problem statement

Quarantine is an optional workflow step in Archivematica that places digital
objects in a separate space for a specified period of time for virus definitions
to be updated. It adds complexity to the workflow and is arguably unnecessary
because ingested digital objects generally speaking pre-date the available virus
definitions, which are updated daily. This proposal is to remove quarantine
to simplify Archivematica's workflow and ease maintenance and testing.

## Decision drivers

* Desire to simplify Archivematica workflows
* Need to fix known bugs related to quarantine if it remains supported
* Little evidence of need for or use of quarantine in the user community

## Considered options

* Remove quarantine from Archivematica interface and workflow
* Fix the current issues with quarantine and continue to support it

## Decision outcome

Option 1, because there is no evidence of use in the community to justify the
continued maintenance of the feature and the positive consequences of the
removal of the code outweigh the benefits of the functionality. The virus
scanning micro-service remains unchanged by this decision.

### Positive consequences

* Simplified, easier to maintain workflow
* Removes two processing configurations that users are required to make but
  which are rarely implemented.
* Resolution of the following issues:
* DSpace workflow issue: [#426][1]
* Virus scan not triggered after quarantine: [691][2]

[1]: https://github.com/archivematica/Issues/issues/426
[2]: https://github.com/archivematica/Issues/issues/691

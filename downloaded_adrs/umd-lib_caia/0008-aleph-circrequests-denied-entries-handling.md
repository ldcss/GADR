# 0008 - Aleph "circrequests" Denied Entries Handling

Date: June 26, 2020

## Status

Superseded by [0010-aleph-circrequests-denied-entries-resubmission.md][2]

## Context

For "circrequests", it is assumed that Aleph always provides a complete list
of holds. A hold is considered valid as long as it is in the list provided by
Aleph.

As described [0006-aleph-interaction-assumptions-for-circrequests.md][1],
it was originally thought that it was necessary for this application to track
which holds have been sent to CaiaSoft, as well as any holds that CaiaSoft has
denied, and resubmit them.

When CaiaSoft denies an entry, information about the denied entry is presented
in the CaiaSoft interface. Based on discussions with Hilary Thompson and
Hans Breitenlohner, repeatedly submitting denied entries to CaiaSoft is not
necessary, and merely adds extra work to clear on the CaiaSoft interface.

## Decision

Remove the functionality that tracks and resubmits "denied" entries. 

## Consequences

From this application's perspective, information returned from CaiaSoft
regarding denied entries will not trigger any special action.

As denied entries are displayed in the CaiaSoft interface, it is assumed that
any issues caused by the denial will be handled the staff that have access to
that interface. 

----
[1]: 0006-aleph-interaction-assumptions-for-circrequests.md
[2]: 0010-aleph-circrequests-denied-entries-resubmission.md

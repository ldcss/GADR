# 0006 - Aleph Interaction Assumptions for "circrequests"

Date: June 15, 2020

## Status

Superseded by [0008-aleph-circrequests-denied-entries-handling.md][1]

## Context

For "circrequests", it is assumed that Aleph always provides a complete list
of holds. A hold is considered valid as long as it is in the list provided by
Aleph.

## Consequences

Because Aleph always provides a complete list of holds, it is up to this
application to track which holds have been sent to CaiaSoft, as well
as any holds that CaiaSoft has denied.

A "denied" hold should be resubmitted (possibly using updated information from
the Aleph response) as long as it still appears in the list from Aleph.

----
[1]: 0008-aleph-circrequests-denied-entries-handling.md

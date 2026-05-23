# 0010 - Aleph "circrequests" Denied Entries Resubmission

Date: July 1, 2020

## Context

In the original "caia" implementation, denied items were resubmitted as part
of every submission to CaiaSoft, as long as the item was included in the list
from Aleph.

As denied items were typically being denied multiple times, this was causing
redundant entries to appear in the CaiaSoft interface. So it was decided not
resubmit denied items.

After further consideration, there was a concern that never resubmitting
denied items could result in patron requests getting lost. So it was decided
that denied items should be resubmitted after a sufficient interval (such as
7 days) as long as the denied item is still in the list provided by Aleph.

## Decision

Modify the application so that items denied by CaiaSoft are resubmitted if
they are still being reported by Aleph after a configurable "wait interval".

## Consequences

This decision adds some complexity to the application, especially the
"diff" functionality, which must take into account denied items and the
wait interval.

Also, this may affect upgrades and migrations to new servers, as the application
now has additional "state" (the file containing the denied items and their
timestamps) which may need to be migrated/replicated on the new server. 

Hopefully, however, this functionality will prevent patron holds from being
lost simply because of an initial denial from CaiaSoft.

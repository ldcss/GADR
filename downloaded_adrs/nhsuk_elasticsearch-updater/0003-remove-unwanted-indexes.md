# 3. Remove unwanted indexes

Date: 2018-01-19

## Status

Accepted

## Context

Elasticsearch timeouts can cause 'orphaned' indexes from remaining in the cluster after an update.
Running two updaters simultaneously, as happens for pull requests that last several days, can leave
two indexes with the same alias.

Elasticsearch watches are run to export data to Prometheus throughout the day.
Two new date stamped 'monitor' and 'watch' indexes are created every day to track the status of the watch job.

## Decision

Orphaned and indexes with duplicate aliases will be removed as part of the update.
The indexes created every day by the watch will also be deleted within the elastic-search updater.
This could be done by an Elasticsearch watch, but a license is required to use this functionality.

To avoid adding more infrastructure components to the system rather than having a standalone service, the cleanup will be
performed in the elastic-search updater. This can be moved into another service in future if required.

## Consequences

The elasticsearch-updater will remove orphaned and duplicate aliases as part of the update.
Monitor and watch indexes older than seven days will be removed. There will be a slight overhead as both running updaters will
check for expired monitor and watch indexes, but this should only be a single additional call to Elasticsearch.

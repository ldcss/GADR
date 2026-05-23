# 2. Database migrations are standalone releases

Date: 23/03/2018

## Status

Proposed, should be reviewed

## Context

Database schema migrations are often considered as part of an application change -
"in order to do X we will need a new index Y"

However, this does not work well with a zero-downtime approach, when we have
a single replicated database - we can't deploy version 0.2 of the application
to some servers simultaneously with version 0.2 of the schema to their databases;
we need to deploy changes to the database either before or after the
corresponding application changes

## Decision

Database schema changes should be made independently of application changes.
Where an application needs a change to the database, this may entail extra releases
to make sure the application and database changes can be safely applied and
safely rolled back without compatibility problems.

For example, if there's a need to change a column name from "foo" to "bar"
you may need:
1. An application release that detects and will work with either a "foo" or a "bar"
column
2. A database schema release that renames the column from "foo" to "bar"
3. An application release that removes the logic in release 1, and just works with "bar"

Alternatively, the database change could be made first, using a view or triggers or other
mechanisms so writes and reads to both "foo" and "bar" change the same data. This
is highly dependant on the change needed and the database features available.

The database schema migration change should be treated as a first class release:

1. The change should be run and tested in conjunction with the application
2. The change should be reviewed and approved by an appropriate approver
3. The change should be deployed to the Staging environment, and normal acceptance/smoke tests run
4. The change should be deployed to Production/DR

### A note on backups
Depending on the complexity of the change, you may wish to coordinate a backup snapshot
of the database before running a migration.  This will never be perfect, as with
a zero-downtime system there will still be data being written in the interval between
the backup being started (on a replica) and the migration running, so this data
would be at risk of being lost.

Many database migrations however are totally safe and should not need a backup -
for instance, adding an index or adding a column is a very low risk change.  Nightly
backups should be enough to mitigate against any risk with this sort of change.

### Alternative approach for Event Store using queues to avoid downtime
*Only if really necessary* we could perform coordinated releases using queues
to avoid downtime, for the special case of the Event Store which can be temporarily
suspended while messages get queued.

The approach would be similar to:
1. Modify the event recorder Lambda timing so the event recorder does not run, or point it to a test queue instead
2. Make a new database backup snapshot - it's assumed that for a change this complex, you need a backup
3. Deploy the database change
4. Test the change
5. Re-enable the Lambda

Note that the SQS queue has a limit of 100,000 queued messages - at peak we have
historically received around 75,000 messages an hour.  So this technique is quite time constrained;
if anything goes wrong you only have a small amount of time to fix it.

## Consequences

* Coordinating changes to applications and databases may often require extra complexity in those changes
* More releases will be needed to make sure deployments are safe
* There should be a lower risk of production outages and more opportunities to test each part of the change in isolation

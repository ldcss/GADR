# 3. Database migrations should be designed for zero downtime

Date: 23/03/2018

## Status

Accepted

## Context

See also ADR 0002 "Database migrations are standalone releases"

As our system is designed for zero downtime, we have to be careful that
we don't change the database in a way that causes production issues

## Decision

Where possible, we should avoid database migrations that will lock the database
for any significant amount of time.  This is hard to enforce, but we will
make sure there is documentation in the project README (and here!) on ways
to achieve this.

This mostly affects index creation and changes - we have several years of data
in our database, and adding or changing indexes can be slow.  In general,
you should use the `CREATE INDEX CONCURRENTLY` option to let indexes be
created in a non-blocking way.  See https://www.postgresql.org/docs/current/static/sql-createindex.html

If you want to `ALTER INDEX` or `REINDEX`, they can't be concurrent - in this
case you'll need to look at stopping the Event Recorder lambda, allowing messages
to queue up while the index change is made.  *BEWARE* however that SQS queues
only allow 100,000 messages, and at peak load we have historically sent 75,000
messages an hour, so you have a somewhat limited amount of time to run such a change.
If you have a very complex change, you should consider:

- Dropping the index then running `CREATE INDEX CONCURRENTLY` rather than
altering indexes - generally our reports run intermittently, so it is safe to have
no indexes for a period of time, data will still be appended with no problems
- Performance testing the change - we have a large fake dataset available that
can be used to simulate a production database in a test environment
- Duplicating the database - you could apply the change to a new database containing
a copy of production data, then switch databases, and migrate any missed changes
from the old database to the new.

### Transactional DDL changes
Most Postgresql schema changes can be made transactionally - this is
a great feature, as it allows for making multiple changes and having them
all roll back if something goes wrong.  For example:
```
BEGIN;
  ALTER TABLE fizzbuzz RENAME COLUMN foo TO bar;
  UPDATE TABLE fizzbuzz set foo = 'splat';
COMMIT;
```
In this case the `UPDATE` will fail, so the column rename will be reverted.

*However* note that `CREATE INDEX CONCURRENTLY` does not work in a transaction -
it depends on being able to change the table incrementally, which doesn't fit
the transaction model.  If the index creation fails, you are recommended to
drop the index and re-create it, as it won't be rolled back and may be
partially created.

### Avoiding blocking changes
There is a useful table in [this article](https://www.citusdata.com/blog/2018/02/15/when-postgresql-blocks/) which I've reproduced below (as the article may disappear):

| Runs concurrently with           | SELECT | INSERT UPDATE DELETE | CREATE INDEX CONC VACUUM ANALYZE | CREATE INDEX | CREATE TRIGGER | ALTER TABLE DROP TABLE TRUNCATE VACUUM FULL |
|----------------------------------|--------|----------------------|----------------------------------|--------------|----------------|---------------------------------------------|
| SELECT                           | Y      | Y                    | Y                                | Y            | Y              | No                                          |
| INSERT UPDATE DELETE             | Y      | Y                    | Y                                | No           | No             | No                                          |
| CREATE INDEX CONC VACUUM ANALYZE | Y      | Y                    | No                               | No           | No             | No                                          |
| CREATE INDEX                     | Y      | No                   | No                               | Y            | No             | No                                          |
| CREATE TRIGGER                   | Y      | No                   | No                               | No           | No             | No                                          |
| ALTER TABLE etc                  | No     | No                   | No                               | No           | No             | No                                          |

Our reports should only use SELECT so most operations won't block them.
The Event Recorder however needs to insert data, so you can't run
any of the index modification changes (apart from `CREATE INDEX CONCURRENTLY`) without risking blocking.

Note however that some changes may be fast enough despite blocking - adding a column
for example.  However you should performance test these changes against a
production-sized database to be sure!

## Consequences

These practices should ensure that database changes don't put production systems
at risk - however they may require extra work, especially in making sure
that people follow these guidelines!

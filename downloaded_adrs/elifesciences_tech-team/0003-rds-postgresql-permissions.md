# AWS RDS permissions

## Status

Accepted

## Context

AWS RDS are managed database servers.

eLife uses RDS to alleviate the task of database management tasks like 
distribution, fault tolerance, monitoring. 

eLife uses PostgreSQL RDS instances for several projects.

eLife provisions these RDS instances, their databases and database users using 
Cloudformation.

Because RDS is a *managed* database server, there are constraints in it's usage.

Commonly encountered constraints are:

* no ssh access to the machine(s) hosting the database server
* no 'root' user access within the database
* [a similar-to-but-not-really 'root' user called 'rds_superuser'](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.MasterAccounts.html)

During the life of an application, the database provisioned by Cloudformation 
may be deleted and re-created, losing the permissions the original database was 
created and successfully provisioned with.

If the new owner of the database is not the 'root' user or a member of the 'rds_superuser' role, some non-application activities such as backups and testing may fail with permission errors.

Re-instating permissions in a PostgreSQL database is an involved process.

## Decision

The RDS *root* user provisioned shall always be the `owner` of the application database.

The RDS *application* user will have enough permissions to read and write to the application database.

The RDS *application* user will not have permission to drop/re-create the application database *in continuumtest, end2end and prod environments*.

## Consequences

Applications that depend on creating or destroying their database will fail with permission errors.

Backups and restore can be done purely by using the root user and without the application's knowledge.

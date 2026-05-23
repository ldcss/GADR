# 0005 - Use of files for data persistence

Date: May 11, 2020

## Context

In general, the application is only interested in data related to previous
steps in the current job, or data from the last successful job that was run.
The amount of data needed by a current job from previous runs is very limited. 

To aid in troubleshooting, it is desirable that communications with the servers
be recorded, as well as the results of calculation steps performed by the
application.

While data from previous runs may have diagnostic value, there is little need
to store the data about particular for from long periods of time.

## Decision

Applications that need to store data between invocations typically persists
the application state in a database.

The use of files for persisting data was motivated by the desire to provide
visibility into the "steps" the application took for a particular job, as well
as provide access to the raw data received from and sent to the servers.

The use of files enables easy access to information about a job via tools such
as "vi" or "cat" that are typically installed on a server. Using the job id
as part of the filenames for files associated with the job make it relatively
straightforward to the relevant files.

The use of files allows data to be easily cleaned up simply by deleting files
in the storage directory older than a particular date.

While a database could provide similar functionality, it would likely result in
additional development complexity, as well as make it more difficult to
access and purge data. It would also require additional resources to run the
database in production. Since very little information is shared between jobs,
and preservation of the information of the jobs over long periods of time is
not necessary, the additional complexity a database would bring does not seem
worthwhile.

## Consequences

Avoiding a database requirement is expected to simplify development and
production deployment.

File backups will be needed to ensure that the application functionality can
be properly restored in the event of a server failure.

# 5. ETL

Date: 2021-04-01

## Status

Accepted

## Context

The road registry existed before this version of the software that operates on it. We can't expect operators to start from scratch and redraw every node and segment.

## Decision

We extract the necessary road registry data, in the form of events, from its _legacy_ database, using a tool aptly named `RoadRegistry.Legacy.Extract`. This tools takes a connection string to the legacy database and transforms some of the tables and rows into a very long list of events, each time noting which stream the event will need to go into as well as the event itself (effectively a `(stream, event)` tuple), putting those into a file called `streams.json` (looks like a very big json array) and compresses that file in turn into a `import-streams.zip` file. This file can then be uploaded to an appropriate AWS S3 Bucket (see the AWS Infrastructure repository to determine which one it is in production), either via the tool itself (if you configure it accordingly) or via the AWS CLI.

The reason for disconnecting the extraction and loading from each other via a file is because the legacy database is usually running on premises or in a different cloud (Azure, in case of the legacy road registry) or a developer's machine, but not in the AWS environment. To avoid putting in extra infrastructure for what is essentially going to be a once in a lifetime job, putting AWS S3 between the extraction and loading seemed like a reasonable trade off.

The loading of the extracted events is done via a tool named `RoadRegistry.Legacy.Import`, which takes the uploaded file from an AWS S3 Bucket and a connection string to the road registry event store (probably an RDS instance running in AWS) and appends the events contained in the uploaded file to their respective streams. The order in which the `(stream, event)` tuples appear in the file is the order in which they will be appended to the mentioned stream.

## Consequences

This way the operator can start off from a well known state of the road registry and start uploading future changes. Once this process is deemed stable and production worthy, the mentioned ETL tooling can be removed from both the infrastructure and the codebase.

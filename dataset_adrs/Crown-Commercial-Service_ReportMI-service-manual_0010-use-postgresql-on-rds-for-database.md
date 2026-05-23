# 10. Use PostgreSQL on RDS for database

Date: 2018-07-18

## Status

Accepted

## Context

In [ADR-0002][adr-0002] we outlined the overall technical approach for the Data
Submission Service, and highlighted the components which we expect will be
developed.

The technical approach describes a data storage layer which will be used to
store the data submitted to the service. The storage layer consists of 3 parts:

1. An API layer which services use to interact with the data storage layer. The
technology choice for this was described in [ADR-0004][adr-0004].
1. A storage engine (database) for structured data, such as data submissions.
The technology choice for this is the subject of this ADR.
1. An object store for storing the original, unedited, submissions provided by
suppliers. This will be subject to a future ADR.

## Storing structured data

The Data Submission Service will need to hold and store lots of data relating to
the MI submissions we receive.

This data is mostly structured data, although some of it will vary significantly
framework by framework.

There are various database types available to us - including key-value,
relational, document, graph etc.

We're starting small, with just a few suppliers and a few frameworks, so we have
a good understanding of the data structure we need. However, we also need to be
flexible so we can support the different needs of each framework.

## Managing and hosting the database

There are several options for managing and hosting databases, including
operating our own infrastructure/operating systems, or making use of a Platform
as a Service offering.

In line with other decisions we've made, we want to minimise the overhead of
managing the database.

[ADR-0008][adr-0008] says we will be hosting the Data Submission Service in
Amazon Web Services (AWS). AWS Relational Database Service (RDS) is a managed
database service which supports various database engines. It provides
high-availability with automatic failover, automated patching and backups and
monitoring features.

## Decision

We will use a PostgreSQL database for storing our data. This will support the
structured data we are storing, but provide flexibility to use it as a JSON
document store where necessary.

We will use PostgreSQL in AWS RDS for hosting the database. This will reduce the
technical overheads required to run a resilient service.

Services will not interact directly with the database, but instead will use the
API described in [ADR-0002][adr-0002] and [ADR-0004][adr-0004].

## Consequences

We will need to design an appropriate data structure for the data we are storing
and also configure the AWS RDS PostgreSQL instance to support our needs.

We will need to review this decision as we add more suppliers and frameworks to
the service to ensure we're using the right database product and type.

We will need to work with the CCS operations team to ensure they understand how
management of this database will operate in future.

[adr-0002]: 0002-overall-technical-approach.md
[adr-0004]: 0004-use-ruby-on-rails-for-applications.md
[adr-0008]: 0008-use-aws-for-hosting.md

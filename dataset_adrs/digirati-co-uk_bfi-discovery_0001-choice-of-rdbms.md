# Choice of RDMS

* Status: accepted
* Deciders: Daniel Grant <daniel.grant@digirati.com>, Gary Tierney
  <gary.tierney@digirati.com>, Stephen Fraser
  <stephen.fraser@digirati.com>
* Date: 2021-02-15

## Context and Problem Statement

BFI's IIIF Univeral Viewer auditing platform requires that each event
which is subject to long term persistence is captured in a manner that
is secure, robust and performant.

## Decision Drivers

* Ability for internal BFI staff to leverage their existing experience
  with managing and maintaining the RDMS.
* Ease of deployment and configuration.
* Ease of ongoing maintenance, patching and support.
* Open source, mature and in active support / maintenance.

## Considered Options

* PostgreSQL (https://www.postgresql.org/)
* MySQL (https://www.mysql.com/products/community/)

## Decision Outcome

MySQL is selected as the solution as it aligns provides BFI with an RDMS
with which they already have experience and are able to support and
maintaining in the long term.

### Positive Consequences

* No initial or ongoing licensing costs associated with the use of
  MySQL.
* Ease of ongoing maintenance for BFI owning to their existing
  familiarity with MySQL.
* Availability of multiple storage engines (InnoDB, MyISAM, etc) and
  distributions (MySQL Community Edition, MariaDB, PerconaDB, etc).
* Simple deployment and configuration (e.g., MySQL publish official
  Docker images).

### Negative Consequences

* Certain SQL features are not available (although it is not expected
  that these will be required).

## Pros and Cons of the Options

### PostgreSQL

PostgreSQL is a community driven RDMS implementation. It is an industry
leader in the open source RDMS field and for most use cases will compare
against proprietary RDMS implementations, e.g., Oracle, Microsoft,
Sybase, etc.

It benefits from a full implementation of the SQL standard and as a
result queries from other RDMS become easily portable. In addition, it
caters to more modern web use cases by allowing storage and indexing of
unstructured data, such as JSON, in the same way strictly tabular data
is indexed within the database.

#### Pros

* Digirati has many years of experience designing, deploying, and
  maintaining PostgreSQL databases.

#### Cons

* Replication is a relatively new feature to PostgreSQL and thus may be
  complex to implement if required.

### MySQL

MySQL is an open source RDMS implementation maintained by Oracle. It is
used in many technology stacks and provides a fast storage engine
(InnoDB).

The MySQL user base is somewhat fragmented, with two popular forks
(PerconaDB and MariaDB) gaining more popularity than the upstream
distribution in recent years. MySQL had stagnated for a long time with
regard to bug fixes and new features in the SQL standard. PerconaDB and
MariaDB took charge on bringing MySQL up to speed in their respective
forks, and more recently upstream MySQL has began to adopt these changes
in MySQL 8+ onwards.

#### Pros

* Digirati have years of experience deploying and maintaining mySQL
  databases.
* BFI have experience deploying and maintaining MySQL solutions.
* MySQL offers a straightforward replication implementation.
* Good performance from the InnoDB engine (although it is not as capable
  as its competitor with regard to flexibility - however it is very
  capable at storing flat tabular data).

#### Cons

* Does not cover the full SQL standard, especially in versions before
  MySQL 8.
* Documentation, deployment guides, etc. tend to be split between
  MariaDB and PerconaDB.

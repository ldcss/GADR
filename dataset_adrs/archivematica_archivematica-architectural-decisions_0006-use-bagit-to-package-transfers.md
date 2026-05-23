---
layout: page
status: accepted
adr: "0006"
title: Use BagIt to package transfers
deciders: Justin Simpson, Jesús García Crespo, Peter Van Garderen
date: 2019-01-01
---

## Context and problem statement

The Simon Fraser University Archives is a long-time Archivematica user. They
recognized that there is often a long-period between receiving digital materials
from donors and an archivist creating a Submission Information Package (SIP) for
long-term archival storage. SFU Archives wanted the ability to perform minimal
digital preservation tasks, such as those provided by Archivematica's Transfer
functionality, and then return to the creation of SIPs from backlog at an
undetermined future time, perhaps several years in the future.

This meant that transfer backlogs are used for long-term storage of content and
that users should expect it to be as durable as Archival Information Package (AIP)
storage for maintaining accurate metadata over pipeline upgrades, migrations or
re-indexes. To enable this, the decision was made to package backlog transfers as
BagIt packages, supported by a verbose METS file, as is already done for AIPs.

## Decision drivers

* Preservation of original content and metadata over long-term gaps in
  processing
* Re-use of existing standards and protocols

## Considered options

* Option 1: automatically convert all transfers to SIPs, send to archival
  storage and re-ingest or delete AIPs at a future processing time
* Option 2: send transfers to backlog and, at a future time, arrange into SIPs
  for sending to archival storage

## Decision outcome

Chosen option: Option 2 was chosen because SFU Archives wanted the ability to
create multiple SIPs from multiple transfers. In their use cases, one transfer
does not automatically equal one SIP and one AIP. By sending transfers to
backlog they are able to use the Appraisal tab functionality where users can
create SIPs by combining files from different transfers in the Archivematica
backlog.

However, this creates a new expectation, namely, that transfer
backlogs can be used for long-term storage of content and that users should
expect it to be as durable as AIP storage for maintaining accurate metadata
over pipeline upgrades, migrations or re-indexes. However, prior to release
1.10, transfers stored using Archivematica's backlog functionality could only be
accessed by using the same pipeline that the transfer was created in. If the
pipeline was accidently lost or decomissioned, you would be unable to reindex
and repopulate the backlogged material in a new Archivematica pipeline. The
reliance on maintaining this backlog information in the pipeline's transactional
database (MCPServer) and search index (Elasticsearch) is a significant
preservation risk if the files are kept in backlog for an indefinitely long
period of time, as is the case for SFU Archives and an increasing number of
Archivematica users.

![before_archivematica_backlog](/assets/before_archivematica_backlog.png)

The decision was made to convert the materials in transfer backlogs to mirror
Archivematica's AIPs, namely to use the Bagit and METS standards to
package and describe the transfer materials. As materials go through transfer
processing, event and object information is written to the transfer METS file
wherever feasible. Other relevant information is captured in a logs subdirectory
in an IETF-compliant Bagit package. Functionality was then added in Archivematica
release 1.10 to rebuild backlogs from these self-describing packages in the event
of a lost or destroyed pipeline.

![after_archivematica_backlog](/assets/after_archivematica_backlog.png)

### Positive consequences

Archivematica users that rely on transfer backlog for long-term storage of
digital materials can now be assured that they can rebuild their backlogs from
the transfer Bagit packages that Archivematica creates as of release 1.10. This
significantly reduces the risk of loss of materials during the transfer backlog
phase.

### Negative consequences

Some major changes were introduced to the Archivematica codebase to enable it
to restore from backlog using transfer Bagit packages. Previously, the
information used to accomplish this was maintained primarily in the MCPServer
database and ElasticSearch index. There is a risk that not all previous
functionality to restore from backlog is fully enabled and that some
regressions may have been introduced as a result of this architectural change.

## Links

* Main Archivematica issue in GitHub: [#391][0].
* IETF [Bagit specification][1].
* Library of Congress [METS standard][2].

[0]: https://github.com/archivematica/Issues/issues/391
[1]: https://tools.ietf.org/html/rfc8493
[2]: http://www.loc.gov/standards/mets/

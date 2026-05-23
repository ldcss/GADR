---
layout: page
status: proposed
adr: "0009"
title: Use AMClient (Archivematica API Client) for API calls in Archivematica
deciders: Artefactual Systems Inc.
date: 2019-10-25
---

## Context and problem statement

Artefactual have been working on a client application to provide easier access
to the functions exposed by the Archivematica Application Programming Interface
(API). This application is called [AMClient][amclient-1]. The application also
acts as a Python library which makes it easier to make Archivematica specific
API calls in code. The library was released as a [Python package][amclient-2]
early in 2019.

## Decision drivers

* Desire to simplify development processes in Archivematica and the Storage
  Service.
* Desire to make it easier to maintain components of Archivematica downstream
  and push the effects upstream (modularity).

## Considered options

1. Continue to make calls to the Archivematica API via low-level Python HTTP
   request libraries.
2. Replace low-level calls with a single consistent approach across the
   Archivematica code-base, i.e. use AMClient.

## Decision outcome

Option 2. The AMClient library helps us to create consistency across the
Archivematica code-base. It is already widely used in the default Automation
Tools, and Archivematica Automated Acceptance Tests (AMAUAT).

### Positive consequences

* As the AMClient library is adapted as a Python package its use on the command
  line is extended and so it becomes more useful to those embedding it outside
  of Archivematica.
* As AMClient is extended, tests are added to the package itself, providing a
  greater level of lower-level testing, thusly the Archivematica API. The focus
  of testing in Archivematica can be on manipulating well understood AMClient
  responses where this is appropriate for the unit being tested.
* The number of lines of code required to talk to the AMClient package versus
  that of creating lower-level API calls via a HTTP requests library should be
  fewer.
* Missing functionality, e.g. as described by issue [#905][amclient-3] can be
  added as it is required by Archivematica and the Storage Service. As an
  external package, and something used inside Archivematica, the two take on a
  symbiotic relationship.

### Negative consequences

* The release candidate for version 1.0.0 of AMClient does not yet adhere to
  more traditional Python best practices i.e. it might not be considered to be
  entirely "Pythonic" in how it exposes errors to the calling code. This is
  described in issue [#488][amclient-4]. This effect of not being 'Pythonic'
  may travel upstream to Archivematica and is something for maintainers to be
  aware of. Work on an AMClient 2.0.0 should replace these patterns and then
  cascading those changes down to Archivematica should still be easier than
  working with and replacing the calls that exist in Archivematica using a HTTP
  requests library.

## Links

* Epic-level issue describing this ADR and other pieces required to implement
  it: [#543][amclient-5].
* ADR 0001: [Unification of METS creation][amclient-6] sets a precedent for
  this work to take place.

[amclient-1]: https://github.com/artefactual-labs/amclient
[amclient-2]: https://pypi.org/project/amclient/
[amclient-3]: https://github.com/archivematica/Issues/issues/905
[amclient-4]: https://github.com/archivematica/Issues/issues/488
[amclient-5]: https://github.com/archivematica/Issues/issues/543
[amclient-6]: https://adr.archivematica.org/0001-unification-of-mets-creation.html

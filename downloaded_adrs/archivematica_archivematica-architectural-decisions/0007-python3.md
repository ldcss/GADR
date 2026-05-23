---
layout: page
status: accepted
adr: "0007"
title: Refactor to Python 3
deciders: "Justin Simpson, Sarah Romkey, Darren Craze, Joel Simpson, David Juhasz, Jesús García Crespo, Pieter Van Garderen, Sara Allain, Ashley Blewer, Santiago Rodríguez Collazo, Miguel Angel Medinilla Luque, José Raddaoui Marín, Cole Maclean, Ross Spencer, Douglas Cerna."
date: 2019-07-22
---

## Context and problem statement

Python 2 will not be supported by the Python development team past January 1,
2020\. Operating system vendors will provide bugfix support for some number of
years, depending on the OS:

* [Ubuntu 16.04 through 2021](https://wiki.ubuntu.com/Releases)
* [Ubuntu 18.04 through 2023](https://wiki.ubuntu.com/Releases)
* [RHEL/CentOS 7 through 2024](https://wiki.centos.org/About/Product)

Archivematica is not fully compatible with Python 3 yet. Archivematica and all
of its required components will eventually need to run in a Python 3
environment, especially as downstream dependencies begin to drop support for
Python 2 (i.e.
[Django](https://docs.djangoproject.com/en/2.2/faq/install/#what-python-version-should-i-use-with-django)).

Components:

* [am/compose](https://github.com/artefactual-labs/am)
* [archivematica-storage-service](https://github.com/artefactual/archivematica-storage-service)
* [MCPServer](https://github.com/artefactual/archivematica/tree/a889605d8c97e114f8c0bc707d6a371030fb5c0b/src/MCPServer)
* [MCPClient](https://github.com/artefactual/archivematica/tree/a889605d8c97e114f8c0bc707d6a371030fb5c0b/src/MCPClient)
* [archivematica-common](https://github.com/artefactual/archivematica/tree/a889605d8c97e114f8c0bc707d6a371030fb5c0b/src/archivematicaCommon)
* [Dashboard](https://github.com/artefactual/archivematica/tree/a889605d8c97e114f8c0bc707d6a371030fb5c0b/src/dashboard)
* [mets-reader-writer](https://github.com/artefactual-labs/mets-reader-writer)
* [ammcpc](https://github.com/artefactual-labs/ammcpc)
* [agentarchives](https://github.com/artefactual-labs/agentarchives)
* [fixity](https://github.com/artefactual/fixity)
* [automation-tools](https://github.com/artefactual/automation-tools)
* [archivematica-acceptance-tests](https://github.com/artefactual-labs/archivematica-acceptance-tests)
* [amclient](https://github.com/artefactual-labs/amclient)

## Decision drivers

* Archivematica is built on Python 2
* Python 2 will no longer be supported after January 1, 2020
* Archivematica should be refactored to use Python 3 (3.5 at minimum)

## Considered options

1. Refactor to Python 3 (3.5 at minimum)

## Decision outcome

Chosen option: 1, because refactoring Archivematica and all required components
to Python 3 is the only option to ensure that Archivematica continues to be a
safe, stable environment.

Python 3.5 has been set as the minimum version for the following reasons:

* [Python 3.4](https://www.python.org/dev/peps/pep-0429/) has already been
  retired
* [Python 3.5](https://www.python.org/dev/peps/pep-0478/) is the oldest version
  this is still supported
* Ubuntu 16.04 ships Python 3.5
* Ubuntu 18.04 ships Python 3.6
* For CentOS 7, The Software Collections Repository provides packages for
  Python 3.5 and up

During the course of the project, a higher version of Python may be selected.

[Epic for Python 3 refactoring](https://github.com/archivematica/Issues/issues/805)

### Positive consequences

* Archivematica will be upgraded to a maintained version of Python.
* Archivematica developers will be able to take advantage of new features in
  Python.
* Python 3 support will be maintained for many years (for example, the latest
  stable release is [3.7, which will be maintained until 2023](https://www.python.org/dev/peps/pep-0537/#release-schedule);
  further releases are expected).

### Negative consequences

* This is a very large task and components need to be tackled in priority order,
  so it will take a considerable amount of time to get everything refactored.
* Releasing the Python 3 work once all components are refactored will take the
  place of a feature release, leaving some development work unreleased for at
  least 4 extra months (note: all code resides in public branches).
* We will need to support Archivematica running Python 2.7 for some time because
  users will need time to upgrade. This results in a dual support burden.
* Development work currently in progress may need to be refactored to Python 3
  before it are releasable, which is unsponsored work.

## Links

* [PEP 373 -- Python 2.7 Release Schedule](https://www.python.org/dev/peps/pep-0373/)

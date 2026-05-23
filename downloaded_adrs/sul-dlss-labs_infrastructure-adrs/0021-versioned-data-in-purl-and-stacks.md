---
layout: default
title: ADR-0021
nav_order: 24
permalink: records/0021
---
# Versioned data in purl and stacks

* Status: Approved
* Decider(s):
  * Chris Beer
  * Aaron Collier
  * Justin Coyne
  * Michael Giarlo
  * Justin Littman
  * Marlo Longley
  * Peter Mangiafico
  * John Martin
  * Niqui O'Neill
  * Steve Taylor
  * Vivian Wong
  * Laura Wrubel
* Date(s):
  * Drafted: 2024-03-15
  * Approved: 2024-06-25

Technical Story: n/a

## Context and Problem Statement <!-- required -->

Open Access (OA) guidelines require that we allow authors to publish each version of a schollarly work as citeable. In order to acchieve this, we will have a unique and stable URL for each version.  Presently we only support a single version in the access (purl/stacks based) systems.

## Decision Drivers <!-- optional -->

* Need to serve multiple versions of data and metadata for each work.
* We don't want to duplicate data that exists in multiple versions
* ... <!-- numbers of drivers can vary -->

## Considered Options

* Use the Oxford Common File Layout (OCFL) <https://ocfl.io/>.  We would merge the existing purl (metadata) and stacks (data) file systems into a single filesystem.  Each object will have a separate metadata and data directory under it.
* A separate directory for each version under the object directory
  * Optionally using a file system that can deduplicate data.
* Custom file layout with content addressable addressable storage using symbolic links to preserve backward compatability
* Create a new SDR item for each version.

## Decision Outcome

Chosen option: "Custom file layout with content addressable addressable storage", because this has the capability of storing multiple versions.  It can deduplicate data it does not require any complex configuration or exotic file system.  It requires fewer lookups than OCFL. Symbolic links will preserve backward compatibility with dissemination services (image server, media server, geoserver, etc.)

### Positive Consequences <!-- optional -->

* Closer association between data and metadata

### Negative Consequences <!-- optional -->

* Converting all the data and applications will take time

## Pros and Cons of the Options

### Oxford Common File Layout (OCFL)

<https://ocfl.io/>

* Good, because data is deduplicated between versions
* Good, because other cultural heritage institutions use OCFL for versioning.
* Good, because it runs on common file systems.
* Good, because it's a relatively simple specification.
* Neutral, not a perfect fit, because OCFL expects stable versions, and we would misuse it by overwriting v1. We may want to use the "mutable head" extension.
* Bad, because data migration is required
* Bad, because application changes are required (e.g. if file paths are not predictable.)
  * If media is never versioned (e.g. always v1), then we can predict its path without reading the OCFL manifest.

### separate directory for each version under the object directory

* Good, because the structure is very simple. No manifest is needed.
* Bad, because data from one version would need to be copied to another version.
* Bad, because mitigating duplicate data may require esoteric file systems.

### Create a new SDR item for each version

* Good, because no migration of data or systems is required
* Bad, because data would be massivly duplicated as new versions were created
* Bad, because multiple versions of each object would show up in discovery and management interfaces.

### Custom file layout with content addressable addressable storage

* Good, because no migration of data or systems is required (using symbolic links)
* Good, because data is deduplicated between versions
* Neutral, we have to build and document this approach. We are not sharing with any other institutions.
* Good, because it runs on common file systems.
* Good, because it's a relatively simple.
* Bad, because links have to be kept in synch with content addressed files. (e.g. two sources of truth)

## Links

* Related to [ADR-0020](0020-purl-fetcher-api.md)

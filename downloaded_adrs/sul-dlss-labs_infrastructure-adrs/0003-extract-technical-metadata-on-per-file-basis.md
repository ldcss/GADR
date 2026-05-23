---
layout: default
title: ADR-0003
nav_order: 6
permalink: records/0003/
---
# Extract Technical Metadata on a Per-File Basis

* Status: drafted
* Decider(s): <!-- required -->
  * Andrew Berger
  * Vivian Wong
  * Infrastructure Team
    * Justin Coyne
    * Mike Giarlo
    * Peter Mangiafico
    * Jeremy Nelson
    * Justin Littman
    * Naomi Dushay
    * John Martin
    * Aaron Collier
* Date(s): <!-- required -->
  * drafted: 2019-10-29
  * ...

## Context and Problem Statement <!-- required -->

Currently, we extract technical metadata per-object and run one extraction job serially per-file. This takes a problematically long time for objects with many files; blocks other objects from accessioning; and complicates restarts which must begin again and process the entire object.

NOTE: Needs discussion: Fedora 3 does not support concurrent writes on the same datastream so we can either split out filesets as a first-class objects in the F3 data model or use temporary caching to generate a consolidated techMD datastream.

## Decision Drivers <!-- optional -->

* Blocker for Google Books project
* Slows down accessioning process

## Considered Options <!-- required -->

* Do nothing
* Extract metadata on a per-file basis rather than on a per-object basis to benefit from parallelism

## Decision Outcome <!-- required -->

TBD!

### Positive Consequences <!-- optional -->

* [e.g., improvement of quality attribute satisfaction, follow-up decisions required, …]
* ...

### Negative Consequences <!-- optional -->

* [e.g., compromising quality attribute, follow-up decisions required, …]
* ...

## Pros and Cons of the Options <!-- optional -->

### [option 1]

[example | description | pointer to more information | …] <!-- optional -->

* Good, because [argument a]
* Good, because [argument b]
* Bad, because [argument c]
* ... <!-- numbers of pros and cons can vary -->

### [option 2]

[example | description | pointer to more information | …] <!-- optional -->

* Good, because [argument a]
* Good, because [argument b]
* Bad, because [argument c]
* ... <!-- numbers of pros and cons can vary -->

### [option 3]

[example | description | pointer to more information | …] <!-- optional -->

* Good, because [argument a]
* Good, because [argument b]
* Bad, because [argument c]
* ... <!-- numbers of pros and cons can vary -->

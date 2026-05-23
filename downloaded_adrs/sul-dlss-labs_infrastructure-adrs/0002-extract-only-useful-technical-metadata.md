---
layout: default
title: ADR-0002
nav_order: 5
permalink: records/0002/
---
# Extract Only Useful Technical Metadata

* Status: drafted
* Decider(s): <!-- required -->
  * Andrew Berger
  * Hannah Frost
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

## Context and Problem Statement <!-- required -->

Currently we are using JHOVE 1.x to generate voluminous technical metadata for every file of every object accessioned in SDR, and we do not use most of this metadata. This is problematic especially for large & many files: we cannot currently accessioning books with many pages because the technical metadata robot consumes all system memory which causes the virtual machine to kill the JHOVE process. We believe that only a small subset of the JHOVE output will ever be useful to SDR consumers.  Note: SMPL content ships with its own metadata typically from MediaInfo rather than JHOVE.

## Decision Drivers <!-- optional -->

* Cannot accession large files (objects > 1GB or so)
* Cannot accession objects with many pages, such as books
* Blocker for Google Books project
* Causes extreme delays accessioning other content

## Open Questions

* What does SMPL do with technical metadata datastream. Should this be cross-walked or added as an attached binary?
* How does this relate to the file identification as part of the contentMetadata? Should we persist the modeled data as a new type of datastream or as part of contentMetadatata?

## Considered Options <!-- required -->

1. Do nothing
1. Identify, and only persist, *needed* technical metadata in a well-defined data model (*.e.g.*, the [one used in Princeton's figgy app](https://github.com/pulibrary/figgy/blob/main/app/resources/nested_resources/file_metadata.rb#L4-L35)), using a tool (or tools) other than JHOVE
1. Stop extracting technical metadata, though this may conflict with being considered a trusted digital repository
1. Add resources to worker machines
1. Run extraction using cloud-based processing

## Decision Outcome <!-- required -->

**Preferred** (by Infrastructure Team) option: option 2, because:

* Option 1 is preventing us from accessioning books and other large objects, which is unacceptable to SDR customers
* Option 3 is an unsound preservation strategy and does not meet SDR user needs
* Option 4 has already been pursued a number of times already, and there's only so much we can toss at the worker machines
* Option 5 has been rejected as a general deployment strategy for now

Thus, option 2 is the only option that currently meets the department's and its customers' needs.

As part of this work, we will move forward with a two-prong strategy in order to resolve the tension between the need to come up with a sound, community-oriented preservation practice and the need to accession large-scale content now.

In the short-term, we will come up with a short list of technical metadata attributes that will be extracted from all files and from all files of certain types. We will convene a “technical metadata strike team” in short order that will review attributes being used in Samvera and make recommendations based thereupon. The aim is for this group to finalize their recommendations in advance of the January 2020 Google Books work cycle.

In parallel, we will pursue a longer-term effort for determining what an ideal, community-oriented strategy is for doing this work building on best practices (which are currently murky/non-emergent). Along with this longer-term work, we will look into how to support on-demand regeneration of technical metadata so that we can iterate on the short-term work in the prior bullet.

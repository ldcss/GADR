---
layout: default
title: Template
nav_order: 27
permalink: records/0024
---

# Transfer Earthworks indexing process to Earthworks codebase and VMs

- Status: proposed
- Decider(s):
  - Access team
- Date(s): <!-- required -->
  - Proposed: 2025-08-14

## Context and Problem Statement <!-- required -->

The focus of this proposal is to move Earthworks-related code and resources from the `searchworks_traject_indexer` stack into Earthworks proper.

The resulting implementation would:

- Remove the traject config for indexing geo records from `searchworks_traject_indexer` and move it to Earthworks
- Halt and remove any Earthworks indexing jobs running on `searchworks_traject_indexer` prod & stage
- Re-implement some indexing jobs as ActiveJob jobs to be run on the Earthworks worker boxes.

## Decision Drivers <!-- optional -->

- It’s a little weird that the codebase called `searchworks_traject_indexer` is actually secretly Earthworks indexing too
- Earthworks already does some of its indexing (see "secondary indexing" below) on its own, separate from `searchworks_traject_indexer`
  - It would be nice not to have indexing happening in 2 places, because this process is manual and basically nobody remembers that it exists
- Earthworks’s stack is already provisioned with worker boxes designed to handle indexing tasks so that the web servers don’t slow down
- Earthworks’s indexer is much simpler than Searchworks’s (nothing from FOLIO, already uses Cocina not MODS, does not need to be particularly fast or parallel)
- Sometimes making changes in `searchworks_traject_indexer` intended to help Earthworks users ends up breaking things for FOLIO indexing

## Considered Options <!-- required -->

There is a choice to be made about the "primary indexing" process (records being released from SDR to be indexed in Earthworks):

1. Run a background process that continuously monitors purl_fetcher's queue, streaming in new records as they are released and indexing them.
1. Periodically invoke a job that asks purl_fetcher for any items updated within the last `<time period>` and reindexes those that were updated.

Option 1 above is more or less the current implementation in `searchworks_traject_indexer`. It's assumed to be fast, but might be overkill for Earthworks.

Option 2 above is more or less the current implementation for DataWorks's indexer (`dataworks-etl`). It may be simpler to implement.

Note that "secondary indexing" (records coming from external sources, like OpenGeoMetadata), which is currently a manual process, would likely be implemented as a scheduled ActiveJob process (similar to Option 2 above) as part of this proposal.

### Positive Consequences <!-- optional -->

- Earthworks-related code becomes centralized in the Earthworks repo instead of spread across repositories
- Indexing jobs for Earthworks are easier for developers who don't often touch Earthworks to understand, debug, and invoke
- It's easier to add or modify indexing jobs for Earthworks without potentially affecting Searchworks indexing

### Negative Consequences <!-- optional -->

- More new code and dependencies will be added to the Earthworks repo, including possibly traject

### Risks

- The existing indexer VMs are powerful, so the indexing process could slow down when not using those machines/becoming less parallel
- Monitoring (e.g. Honeybadger) will need to be carefully set up to ensure the new jobs are running as designed

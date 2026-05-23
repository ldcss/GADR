---
layout: default
title: ADR-0015
nav_order: 18
permalink: records/0015
---
# Replace Openwayback with pywb

* Status: drafted <!-- required -->
* Decider(s): <!-- required -->
  * Andrew Berger
  * Peter Chan
  * Vivian Wong
  * Infrastructure Team
    * Aaron Collier
    * Justin Coyne
    * Naomi Dushay
    * Mike Giarlo
    * Justin Littman
    * Peter Mangiafico
    * John Martin
    * Ed Summers
    * Laura Wrubel

* Date(s): <!-- required -->
  * proposed: 2022-05-17

## Context and Problem Statement <!-- required -->

We currently use a [fork of Openwayback](https://github.com/sul-dlss/openwayback) to provide replay of web archive files (WARCs) in the Stanford Web Archive Portal (SWAP). Openwayback does not successfully replay all WARCs that are replayable elsewhere (e.g. Archive-It's Python Wayback), particularly those with Javascript, videos, and other dynamic content.  Our openwayback repo has been significantly modified and is not possible to update with upstream changes without considerable effort, as explored in [swap](https://github.com/sul-dlss/swap). Our existing CDX files are 10-column indexes (more common is 9 or 11 columns) which lack the compressed length field and do not use SURT-ordered keys, both of which are typical and useful in current index approaches.

The purpose of this ADR is to propose an alternative replay framework and indexing approach. For a previous discussion of some of this issue see the [Indexing](https://github.com/sul-dlss/web-archiving/wiki/Indexing) wiki page.

## Decision Drivers <!-- optional -->

* Support replay of WARCs with dynamic content as well as legacy WARCs, including from the early Web (SLAC)
* Support for indexing WARCs into CDX/CDXJ format
* Can exclude content at the URL level, at a minimum
* Can provide/deny access based on whether the user is on site or not.
* Can delete content at the WARC level
* Infrastructure team can support application
* Operations team can support application
* Use actively developed software with community support
* Is it beneficial for playback to retain the notion of *collections*, or can all the archived content be treated as one big collection?

## Considered Options <!-- required -->

* [pywb](https://github.com/Webrecorder/pywb)
* pywb + [OutbackCDX](https://github.com/nla/outbackcdx)
* Upstream [OpenWayback](https://github.com/iipc/openwayback)

## Pros and Cons of the Options

The following three options all employ open source software. pywb is licensed with the [AGPL](https://en.wikipedia.org/wiki/GNU_Affero_General_Public_License), which would prevent closed source reuse or alternative licensing of pywb. OpenWayback and OutbackCDX both use the liberal Apache license.

### pywb

* Pro
  * [pywb](https://github.com/webrecorder/pywb) is replacing Openwayback as wayback machine of choice among institutions running a replay system.
  * Does not require customization to provide access to crawl dates pre-1996.
  * Can continue to leverage the filesystem as a way to communicate between the workflow and the playback application.
  * Active development is occurring on the software.
  * Supports embargos and exclusions at a URL level.
  * Increasingly used by community, [recommended by IIPC](https://netpreserveblog.wordpress.com/2020/12/16/openwayback-to-pywb-transition-guide/) for replay of high-fidelity archiving. [Transition guide](https://pywb.readthedocs.io/en/latest/manual/owb-transition.html) exists.
* Con
  * As a Python application, is less familiar to developers and operations team
  * pywb development is currently done in large part by one developer
  * adding new WARC data to a collection involves merging the existing index with the new index, which can involve unknown amounts of time as collections get bigger, athough approaches like the current `level[0-3].cdx` approach could provide a way to mitigate this cost.
  * without the creation of new tooling, *deleting* WARC content would require immediate reindexing of the entire collection that the content is a part of
  * moving WARC data from one collection to another would require immediate reindexing of both collections, but would be unnecessary if there is only one big collection
* Additional context
  * It is best practice to reindex WARCs when switching to a new playback system, for consistency. While our existing indexes can be converted with a pywb utility, reindexing would be preferable.

### pywb + OutbackCDX

* Pro
  * All pros from above, including increasing use by community for indexing.
  * Eliminates need to merge index levels as collections grow; new indexes would be POSTed to [OutbackCDX](https://github.com/nla/outbackcdx) as created.
  * OutbackCDX makes it easy to remove WARC content from an index, by issuing a HTTP DELETE request containing the CDXJ data to be deleted.
  * Moving content between collections (if needed) would amount to deleting the CDXJ data from the existing collection and adding it to the new collection, which should be quick operations.
  * Searching indexes should be faster since OutbackCDX uses RocksDB to do the lookups rather than the binary search implementation that is built into pywb. We would need to do testing to compare how much of a difference this is.
  * pywb migration documentation [recommends using OutbackCDX with pywb](https://pywb.readthedocs.io/en/latest/manual/owb-transition.html?highlight=outbackcdx#openwayback-transition-guide). This is presumably because pywb and OutbackCDX are being used together by large national libraries.

* Con
  * Outback CDX does not support querying all or multiple indexes at once. They must be queried one by one. Pywb does not yet provide ability to automatically query all OutbackCDX indexes.
  * OutbackCDX development is led by small number of developers.
  * OutbackCDX is another Java application to support.
  * "fuzzy" matching allows looking up URLs which may have timestamps and other boilerplate in them, which is sometimes needed for replay of video and social media content. It is unclear how pywb and OutbackCDX fuzzy matching implementations are kept in sync. If there are lots of people using OutbackCDX this may be more of a Pro than a Con since improvements that are made there may not get reflected in pywb's implementation.

* Additional context
  * It is best practice to reindex WARCs when switching to a new playback systems for consistency. While our current indexes can be converted with a pywb utility, reindexing would be preferable.

### Upstream Openwayback

* Pro
  * Exploratory work occurred and can be basis of new work.
  * Relatively familiar application, although requires Java which is less widely used by team.
* Con
  * Playback is not up to date with contemporary websites.
  * OpenWayback is no longer under active development.
  * Many other institution moving away from Openwayback for replay.
  * Exploratory work did not lead to implementation.
  * Will still require customization to support WARC collections
  * Adding new content involves indexing and merging, which can be costly in terms of time and resource utilization.

## Decision Outcome <!-- required -->

The infrastructure team, combined with Andrew Berger and Peter Chan, convened a meeting on May 19 to discuss the three presented options. The consensus was to proceed with the first option (using pywb without OutbackCDX) pending performance testing of indexing and searching of multi-TB subset of the web archive content. The decision was largely motivated by an interest in simplifying service maintenance (less moving pieces to keep up to date) and reflecting on the relatively narrow developer and install bases there for these applications. The decision can also be revisited in the future as we learn more about using pywb over time.

## Unknowns

* Any needed changes to sul-embed to support display of crawl dates (uses TimeMapAPI)

## Links <!-- optional -->

* [Link type] [Link to ADR] <!-- example: Refined by [ADR-0005](0005-example.md) -->
* ... <!-- numbers of links can vary -->

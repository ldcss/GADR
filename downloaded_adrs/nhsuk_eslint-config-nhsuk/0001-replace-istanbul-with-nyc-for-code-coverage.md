# 1. Replace istanbul with nyc for code coverage

Date: 2019-09-23

## Status

Accepted

## Context

Istanbul version <1.x.x has been deprecated and is no longer receiving updates.
nyc is one of the suggested replacements. Additional information is available
on [npm](https://www.npmjs.com/package/istanbul). This leaves the package open
to security flaws that will not be patched. Features available in the latest
versions of node will not be supported.

## Decision

The decision is to migrate from istanbul to nyc.

## Consequences

Consequences include:
* Latest releases will be available
* Security patches will be available
* The new industry standard code coverage tool will be getting used by the
  project

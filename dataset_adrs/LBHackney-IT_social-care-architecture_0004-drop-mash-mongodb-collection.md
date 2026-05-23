---
id: drop-mash-mongodb-collection
title: 4. Drop MASH MongoDB Collection
---

Date: 2022-01-24

## Status

Accepted

## Context

Early in the MASH development, a MongoDB collection was set up for storing the form data from MASH referrals form data. This was only set up in Staging. However this collection was never used and is no longer needed.

## Decision

The MongoDB collection for MASH referrals will be dropped.

Information on the changes and the details of implementation can be found in this [PR](https://github.com/LBHackney-IT/social-care-case-viewer-api/pull/577).

## Consequences

Number of MongoDB collections to manage will be reduced.

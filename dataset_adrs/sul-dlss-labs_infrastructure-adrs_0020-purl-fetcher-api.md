---
layout: default
title: ADR-0020
nav_order: 23
permalink: records/0020
---

# Create a publish/shelve API that support versions for access systems

- Status: Approved
- Decider(s): <!-- required -->
  - Access Team
  - Infrastructure Team
  - Andrew (Repository Admin)
  - ...
- Date(s):
  - Drafted: 2024-03-14
  - Approved: 2024-04-28

Technical Story: n/a

## Context and Problem Statement <!-- required -->

Currently dor-services-app (DSA) and the SDR workflow system work together to orchestrate the three steps required for shelving and publishing an object to the access system. DSA needs to share knowedge with the access systems for how the files in both `/stacks` and `/purl` are to be structured.

1. Put content files on `/stacks` NFS mount (<https://github.com/sul-dlss/dor-services-app/blob/main/app/services/shelving_service.rb#L4>)
1. Put metadata on `/purl` NFS mount (<https://github.com/sul-dlss/dor-services-app/blob/main/app/services/publish/metadata_transfer_service.rb#L5>)
1. Call the "purl-fetcher" API to transfer control of these objecs to the access system (mainly for indexing.)

Ideally, this would be a single API where the files are uploaded and metadata is posted (similar to the SDR deposit API). This would allow us to decouple DSA, from needing to mount the `/stacks` and `/purl` filesystems.

## Decision Drivers <!-- optional -->

- We need to add support for versions of objects. An API allows the access team to fully control the implementation of the filesystem required for versions, without having to share that knowledge with DSA.

## Considered Options <!-- required -->

- Use a deposit API similar to sdr-api
- Continue to use 3-step deposit

## Decision Outcome <!-- required -->

Chosen option: "Use a deposit API for purl-fetcher", because this allows for decoupling dor-services-app from the file structure of `/purl` and `/stacks`. This will allow the access projects to move to versioned object storage, without having to make changes in dor-services-app.

### Positive Consequences <!-- optional -->

- [e.g., improvement of quality attribute satisfaction, follow-up decisions required, …]
- ...

### Negative Consequences <!-- optional -->

- [e.g., compromising quality attribute, follow-up decisions required, …]
- ...

## Pros and Cons of the Options <!-- optional -->

### Use a deposit API similar to sdr-api

This will allow us to leverage the activestorage API for transfering the files. We've already implemented this in SDR-API, so it won't be a big challenge to adopt it here. See <https://github.com/sul-dlss/sdr-api/?tab=readme-ov-file#sequence-of-operations>

- Good, because all files and metadata can be verified when we do the final post.
- Good, because all files and metadata go through a single API
- Good, because it abstracts away the implementation of /purl and /stacks filesystems.
- Bad, because we will need to account for orphaned files, that is files that are posted, but metadata is never sent.
- ... <!-- numbers of pros and cons can vary -->

### Continue to use 3-step deposit

Put files on /stacks mount, put metadata on /purl mount. Then call dor-fetcher.

- Good, because proven setups
- Good, because it's simple
- Bad, because it will make it hard to change to versioned access system. We will have to rewrite it all anyway, and this will require both the sender and receving systems to coordinate that migration.
- Bad, because boundaries between systems should have APIs.
- Bad, because no validation of completeness happens.

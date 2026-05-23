# 4. use a version tag to make updating wordpress easier

Date: 2021-02-25

## Status

Accepted

## Context

As we move client sites to dalmatian we want an easy way to keep WordPress up
to date. We currently use whippet-racetrack but that doesn't understand github
and is still quite a manual process. We are likely to have 80 sites running on
dalmatian so we also need a scalable way to update these sites to the latest
version of WordPress.

We want to automatically update minor and patch versions but not major
versions. We have created a `v5` tag in our snapshot repo that will point to the
latest released version of version 5.

When a new major version is released we will want to test it before updating
therefore we are not going to just point at master branch on our snapshot
repo.

## Decision

Set the revision of WordPress in `config/application.json` to be `v5`

## Consequences

We will be able to update WordPress within a major version easily but upgrading
to a new major version will still be quite manual.

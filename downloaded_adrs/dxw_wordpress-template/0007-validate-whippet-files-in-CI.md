# 7. Validate Whippet files in CI

Date: 2021-10-01

## Status

Accepted

## Context

Whippet.lock and whippet.json files can sometimes become out of sync, or malformed. For instance, this can happen when attempting to remove a plugin. When this happens, we often are unaware until the deploy fails.

Whippet now has a `whippet deps validate` command that will check if the two files are properly aligned, and well-formed, that we could use to spot such errors earlier.

## Decision

We'll run `whippet deps validate` in CI via a re-usable workflow.

## Consequences

We'll need to maintain the [GovPress-workflows repo](https://github.com/dxw/govpress-workflows) which will centrally control this workflow.

# 4. Allow easily publishing of commands and repositories

**Date**: 2020-05-28
**Status**: Accepted

## Context

Now that the [repository story is a bit
clearer](0003-remote-repositories-management.md), `macondo build` command should
be enhanced to also generating repository YAML files.

## Decision

Add a new flag to the `macondo build` command that also generates a YAML file
with all the commands generated.

## Consequences

This makes it easier to automate building/publishing commands to HTTP repos like
artifactory.

# 5. Remove unnecessary commands

**Date**: 2020-05-29
**Status**: Accepted

## Context

Now that the repo subcommand is able to add, remove, update and list
repositories... maybe the barebones `list` command should be removed in favor of
`repo list`. That may make things simpler.

Also the `--with-manifest` command is less useful now that the repository
management is easier.

## Decision

- Remove the explicit `list` command
- Remove the `--with-manifest` argument
- Simplify listing the commands when none is provided (removing versions)
- List commands when listing repositories

## Consequences

- New users might find it more difficult to list the commands
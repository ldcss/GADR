# 3. Remote repositories management

**Date**: 2020-05-27
**Status**: Accepted

## Context

Right now this cli tool comes with a builtin set of commands that is hardcoded
to a gist I own somewhere. This is not ideal.

We want this tool to easily access "repositories of commands" that are either
remote or local; as well as a way to easily add/remove repositories.

Some ideas of repositories:

- HTTP urls pointing to yaml manifests with commands definitions
- Github repositories
- Local files or directories

## Decision

- We won't have built-in commands or repositories
- We will support three types of repositories:
  - Remote http resources pointing to yaml files
  - Local manifest yaml files
  - Local directories containing .mcd files

Because http resources are now supported, we could make it so that the
repositories with commands has CI/CD via Jenkins, which generates a repo and
publishes it to artifactory.

The macondo file will be simplified to only include, for now, a top-level
`repositories` array, which would point to the repositories.

A macondo update command will be added that refreshes the list of commands
provided by the repositories. This is only done for http repos, whose
contents could change anytime.

A new set of commands to be implemented:

- `macondo repo add` to add repositories
- `macondo repo remove` to remove them
- `macondo repo update` to update them
- `macondo repo list` to list them

## Consequences

It makes us implement proper repository management, adding more complexity to
the application.

It adds complexity to the tool making it harder to understand.

Makes it easier to keep track of the changes of the commands, allowing rolling
back if needed (by reverting to use a different http repo, for instance).

# 2. No commands are built in by default

Date: 2020-05-25

## Status

Proposed

## Context

As of now, the `macondo` tool includes a basic manifest pointing to a personal
gist. This is useful because it means `macondo` is pretty much useful after
installing, without configuring anything.

This is however no ideal:

- It makes it hard to generalize/open source.
- It points to a hardcoded gist to which only I have access to

Instead, I propose not to include any command by default. Instead, provide ways
for people to easily add commands/manifests/repositories by using something like
`macondo config`.

This could be added to the installation documentation, making it a bit more
explicit while still not being too painful.

## Decision

Remove the hardcoded bootstrap repository.

## Consequences

`macondo` requires extra configuration post-installation before it is useful.

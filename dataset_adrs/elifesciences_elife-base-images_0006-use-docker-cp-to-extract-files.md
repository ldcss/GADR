# 6. Use docker cp to extract files from containers

Date: 2018-02-15

## Status

Accepted

## Context

Test suites and other tools may produce output files while running inside a container.

Due to environmental differences, container users and groups often do not match the host's users and groups, blocking one side from deleting the files of the other; often with corner cases such as files being deleted but not subdirectories.

Automated infrastructure usually runs as the `elife` or `jenkins` user, not as `root`. The docker daemon runs as root and is capable of bridging differences.

## Decision

Use `docker cp` to exchange files between containers, especially from inside a container to the outside.

## Consequences

It should never be necessary to mount a volume on `/srv/project/build/`.

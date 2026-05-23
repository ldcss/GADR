# 7. Automatic aligning of user host user for better interoperability

**Date**: 2020-06-03
**Status**: Proposed

## Context

A well constructed macondo command should be easy to run directly (without
macondo) by just executing it. This is hard to achieve unless the user in the
container resembles as much as possible the host running it.

One case where this is important is modifying files in the host. This is
achieved by mounting a volume into the running container. However, the files
written from the docker container are owned by the docker user, i.e. the user id
and group id of the file is that of whatever docker user happened to write it.

So if the container runs with the root user, which is unfortunately common, then
the files written to the host also are owned by root, making them innacessible
to the host user.

Potential ideas:

- A flag that enables user alignment and mounts HOME into docker's HOME.
- Customize home when running in OSX to be /Users/bla instead of /home/ble
- Even if mounting the whole home, it should be easy to mount current PWD into
  something else /mnt/blablabla and use tha as working directory

## Decision

Add a mechanism to align the user/group of the host system with that of the docker container.

## Consequences



# 5. Provide a standard bin/ folder

Date: 2018-02-05

## Status

Accepted

## Context

Applications often need to drop in binaries or scripts, either downloaded or picked up from other images such as `proofreader-php`.

The binaries needed do not need `root` permissions or system-wide installation.

The binaries may need to modify the application files.

A container image may be an alien environment, as it makes it difficult to find out which of the files were provided by the Dockerfile build process.

## Decision

Every image should provide a standard `/srv/bin` folder, on the PATH, containing utilities owned by `elife`.

## Consequences

Using tools from inside a container image or on a `run` command should be as simple as `command arg1 arg2` (calling `/srv/bin/command`).

Multi-stage builds should be minimal, just copying a file from another image to `/srv/bin`.

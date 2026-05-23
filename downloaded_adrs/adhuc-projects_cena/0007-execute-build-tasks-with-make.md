# 7. Execute build tasks with Make

Date: 2018-12-29

## Status

Accepted

## Context

We don't want the development tools or Continuous Integration pipeline to be strongly bound to [Gradle](0006-manage-build-with-gradle.md).

[Make](https://linux.die.net/man/1/make) is an utility agnostic of any language or build management tools.

## Decision

Make will be used to execute build tasks, abstracting Gradle and potential other tools used during build execution.

## Consequences

Gradle tasks won't be executed directly, but rather encapsulated in Make targets. Using Make will help abstract the
different tools used during the build execution and provide a cohesive way to run any build task.

Make may help integrating with multiple tools used during the build even if Gradle has no plugin to manage those tools
directly. It will also simplify the commands to use during development lifecycle, using well known `clean`, `build`, `run`
targets.

A `help` target will list the available options.

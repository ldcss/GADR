# 2. Isolate components into submodules

Date: 03/06/2018

## Status

Accepted

## Context

I want to be able to mix and match different implementations
of the ddd sample application, without needing to pull in
a large collection of unnecessary dependencies.

I want all of the code to be together in one place; which
is to say, I want to treat the entire project as a mono-repo.

I can't be bothered to maven install/maven deploy each
little piece to propagate the necessary changes between
isolated libraries.

## Decision

Use a maven reactor project to track the dependencies between
different libraries within the project

## Consequences

Because the existing citerus implementation already has
its own repository, and project hierarchy, I'll need to
manage that piece separately from the rest.



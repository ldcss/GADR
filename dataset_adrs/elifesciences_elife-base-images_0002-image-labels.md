# 2. Use image labels to store metadata on an image

Date: 2018-02-05

## Status

Accepted

## Context

An image is a powerful mechanism for deployment, as it is portable across environments.

Some images need to specify the version of their dependencies (such as other images) that should be run as sidecars.

## Decision

Use image labels of the form `org.elifesciences.dependencies.api-dummy` to store the version of a dependency. 

## Consequences

Developers and nodes will be able to retrieve the corresponding version of a dependency through the inspection of an image.


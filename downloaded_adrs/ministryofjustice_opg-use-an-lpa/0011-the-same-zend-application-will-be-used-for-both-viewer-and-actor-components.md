# 11. The same Zend application will be used for both Viewer and Actor components

Date: 2019-05-01

## Status

Accepted

## Context

Use an LPA will be made up of two components - those for use by LPA _actors_, and those used by third 
party groups who are the _viewers_ of the LPA.

At present it is expected that these two components will be hosted on two different domains.

## Decision

That both `Viewer` and `Actor` will both be separate modules of the same Zend application.

Note: it is still expected that they will be deployed separately into two containers.

## Consequences

* The two services will be able to share code much more easily.
* There will only be a single Zend codebase to manage.
* The application will be slightly larger overall as the dependencies for both modules will be included.

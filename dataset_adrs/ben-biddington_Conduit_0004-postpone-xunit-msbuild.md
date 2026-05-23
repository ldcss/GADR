# 4. Postpone Xunit MSBuild

Date: 24/02/2016

## Status

Accepted

## Context

The xunit msbuild target does not work under xbuild and also we would like to be able to select files by glob pattern. The xunit target requires you know the name up front. In a CI environment these may differ, for example you may be unpacking an artifact archive.

## Decision

Try implementing our own one that allows globbing but uses the internal from the xunit version

## Consequences


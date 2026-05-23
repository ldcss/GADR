# 4. Depend on linux

Date: 2020-11-02

## Status

Recommended

## Context

Should we depend on running in an unix environment with support for e.g. `sh` commands.

## Decision

We depend on linux and therefore reduce the overhead of maintaining linux and windows support.

## Consequences

* The shared library cannot be completely used in windows environments. 
* Windows slaves for UI testing etc may not be fully supported
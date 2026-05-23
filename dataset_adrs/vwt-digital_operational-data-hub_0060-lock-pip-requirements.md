# 60. Lock pip requirements

Date: 2021-06-08

## Status

Accepted

Implements [4. Create software defined everything](0004-create-software-defined-everything.md)

## Context

Code Injection is a specific type of injection attack where an executable program statement is constructed involving user input at an attack surface that becomes vulnerable when it can be manipulated in an unanticipated way to invoke functionality that can be used to cause harm.

## Decision

To prevent dependency injection attacks we decided to have both a requirements.in file and a [pip-tools/pip-compile](https://github.com/jazzband/pip-tools) generated requirements.txt

## Consequences

Please check the 'Way of Working' document on [Confluence](https://recognize.atlassian.net/wiki/spaces/DAT/pages)

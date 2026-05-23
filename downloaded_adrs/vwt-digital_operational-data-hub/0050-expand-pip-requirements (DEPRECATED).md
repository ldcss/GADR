# 50. Expand pip requirements

Date: 2020-11-18

## Status

DEPRECATED

Implements [4. Create software defined everything](0004-create-software-defined-everything.md)

Deprecated by [60. lock-pip-requirements](0060-lock-pip-requirements.md)

## Context

Code Injection is a specific type of injection attack where an executable program statement is constructed involving user input at an attack surface that becomes vulnerable when it can be manipulated in an unanticipated way to invoke functionality that can be used to cause harm.

## Decision

To prevent dependency injection attacks we decide to have both an requirements.unexpanded.txt and an (development time / pip freeze) generated requirements.txt

## Consequences

Please check the 'Way of Working' document on [Confluence](https://recognize.atlassian.net/wiki/spaces/DAT/pages)

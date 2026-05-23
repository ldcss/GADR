# 45. Code / config separation

Date: 2020-09-21

## Status

Accepted

Implements [4. Create software defined everything](0004-create-software-defined-everything.md)

Implements [5. Build Open Source solutions](0005-build-open-source-solutions.md)

## Context

Both Code and Configuration reside in source code control (Github in our case). This makes it very easy to mix-up code and configuration. However, these 2 should be clearly separated. Where possible code can be reused, but configuration is most of the times instance specific.

## Decision

Code and Configuration is clearly separated. At deployment time the CI/CD tools are responsible for bringin code and config together and deploy the code together with the correct configuration.

## Consequences

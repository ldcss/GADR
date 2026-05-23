# 6. Homogeneous build across environments

Date: 2020-11-20

## Status

In progress

## Context

* In order to develop and test their build and deployment pipeline the teams need be able to run the same build tools as the CI server offline on their machines.
* In order to be able to trace user acceptance down to code and to enable efficient and fast pipelines we must not build the same code multiple times for different environments / configurations.

## Decision

* We make a **pipeline development environment** available to teams. See #34
* The CI server only **build once** per pipeline run, so that the commit hash of the system can be used as reliable reference.

## Consequences

* We keep environment specific configuration outside of the binaries.
* We accept to use feature toggle.
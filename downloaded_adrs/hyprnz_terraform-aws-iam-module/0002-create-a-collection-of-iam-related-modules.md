# 2. Create a collection of IAM related modules

Date: 2020-03-10

## Status

Accepted

## Context

There are many IAM resources of which most, if not all, are relatively small in size & complexity. In order to minimise repo churn, the module will contain a collection of modules which can be invoked as required.

## Decision

The module will be a mono repo of specific IAM resources.

## Consequences

Over time, the size of the repo may cause issues when using singular resources. Given that IAM resources have a relatively small size footprint, it is unlikely to cause any impacts.

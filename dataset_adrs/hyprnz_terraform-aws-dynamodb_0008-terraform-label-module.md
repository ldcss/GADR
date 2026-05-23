# 8. Terraform Label Module

Date: 2019-05-21

## Status

Accepted

## Context

It can sometimes be hard to name resources in AWS so that you can identify them.
The clever guys from [CloudPosse](https://github.com/cloudposse) have created a
[terraform-terraform-label](https://github.com/cloudposse/terraform-terraform-label)
module aimed at helping to generate consistent label names and tags for
resources.

## Decision

This module will utilise the
[terraform-terraform-label](https://github.com/cloudposse/terraform-terraform-label)
module.

## Consequences

You should use this module for every unique resource of a given resource type.

Labels follow the convention of: `{namespace}-{stage}-{name}-{attributes}`

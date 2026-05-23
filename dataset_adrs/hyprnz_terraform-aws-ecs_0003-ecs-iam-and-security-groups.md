# 3. ECS IAM and Security Groups

Date: 2019-03-21

## Status

Accepted

## Context

The ECS IAM roles are currently in the global IAM module and the security groups
are in the VPC modules. These made sense when first developed and based on the
existing multi environment in one account set up. They don't make sense when
doing a new single environment account - which is the way we are transitioning
to.

## Decision

Refactor the IAM roles and security groups into the ECS Cluster in a way that
maintains backward compatability and supports the future approach of single
environment accounts.

Toggles can be used to support the backwards compatability and future
approaches.

## Consequences

IAM roles currently duplicated in the global IAM modules.

Additional complexity to the ECS Cluster module but this trades off against
additional use flexibility.

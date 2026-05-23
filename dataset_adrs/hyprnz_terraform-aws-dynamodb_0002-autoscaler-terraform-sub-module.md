# 2. Autoscaler Terraform Sub Module

Date: 2019-05-14

## Status

Accepted

## Context

DynamoDB can utilise the [AWS Application Auto
Scaling](https://docs.aws.amazon.com/autoscaling/application/APIReference/Welcome.html)
to dynamically adjust provisioned throughput capacity on your behalf. Not all
uses of DynamoDB will use this autoscaling service.

There is a plan to create a Terraform `Data Storage Module` which will include
the DynamoDB module.

## Decision

To support autoscaling a Terraform sub module will be utilised.

This sub module will be included in the DynamoDB module using Terraform `module`
syntax. An `enabled` toggle will be used to determine whether or not the
autoscaling resources will be created.

## Consequences

The autoscaling module will not be versioned independently. Changes to the
DynamoDB version will be associated with the local version of the autoscaling
sub module.

There is a single place to update DynamoDB Terraform modules.

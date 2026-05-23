# 3. Provisoning Service Link Role is outside the scope of this module

Date: 2021-01-06

## Status

Accepted

## Context

An Elastic Search Service Linked Role is required when provisioning an ES Domain in a VPC. It allows the ES Domain to bind and configure ENI's on the VPC.

## Decision

There can be only 1 ES Service Linked Role per account, and so this module will not create the Service Linked Role. The ES Service Linked Role resource must already be provisioned in the AWS account when using this module.

## Consequences

Given this ES Service Linked Role is shared across all ES Domainsin an AWS Account, the consequences of a Terraform Destroy removing the Service Linked Role would impact any remaining ES module instances still provisioned.

Having no side effects of the module upon a Destroy command is preferred over the convenience of creating the ES Service Linked role when provisioning this module. This module has a dependency on having the ES Service Link Role provisioned before running the Apply command.


# 2. Do not specify maximum-version constraints for required providers

Date: 2020-12-21

## Status

Accepted

## Context

Terraform allows to pin the spcific versions of providers required for this module.

## Decision

This module will not enforce maximum versions contraints for all required providers

## Consequences

Terraform recommend to only provide minimum provider version constraints as per the [best practices](https://www.terraform.io/docs/configuration/provider-requirements.html#best-practices-for-provider-versions) page.

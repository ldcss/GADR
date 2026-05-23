# 2. use terraform workspaces for environments

Date: 2019-11-12

## Status

Accepted

## Context

There are two primary patterns of use when managing multiple environments (staging, prod, etc) in Terraform. The first is to use multiple directories--one for each environment. This has the advantage of being explicit, with an associated cost of repeated TF configuration. The second alternative uses TF workspaces to switch between environments. This option appears to be [recommended](https://www.terraform.io/docs/enterprise/guides/recommended-practices/part1.html#one-workspace-per-environment-per-terraform-configuration) by Terraform. The latter which we will use here allows a DRY approach across the environment.

## Decision

Use workspaces to manage multiple environments.

## Consequences

Users will have to remember to switch workspaces that aren't clearly labeled

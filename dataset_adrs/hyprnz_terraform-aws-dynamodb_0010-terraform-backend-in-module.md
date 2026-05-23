# 10. Terraform Backend in Module

Date: 2019-05-28

## Status

Accepted

Updates [3. No Terraform Backend in Module](0003-no-terraform-backend-in-module.md)

## Context

When LIC teams begun using this module it became apparent that the current
implementation pattern does not meet their needs. Without a backend in the
module teams would need to add a Terraform `backend` configuration into there
local implementation for it to be picked up.

## Decision

Restored the `backend` into the module for the time being.

We still feel this should be removed at some time and teams become familiar with
how to use Terragrunt/Terraform configuring there own `backend`.

## Consequences

The examples that were envisioned to use a local `backend` now have the
Terraform `backend` set in a `terraform.tf` (Terragrunt) or in the `main.tf`
(Terraform).

Teams don't need to set a `backend` during implementation time. This matches
current expectation.

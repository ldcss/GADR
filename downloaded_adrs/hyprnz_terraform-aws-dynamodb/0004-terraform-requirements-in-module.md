# 4. Terraform Requirements in Module

Date: 2019-05-14

## Status

Accepted

## Context

Terraform enables you to constrain the version of Terraform able to run a
modules, as well as the minimium allowed versions of providers. Many of LIC
existing modules do not leverage these configurations.

## Decision

The Terraform version able to run this module will be set in `main.tf`.

The miniumum allowed versions of providers will be set in `main.tf`

## Consequences

There is a minimum version of Terraform able to run this module.

* Terraform `~> 0.11`

The minimum allowed versions for providers used by this module.

* aws  `>= 2.6.0`
* null `>= 2.1.1`

Terraform/Terragrunt will flag uses outside these parameters as issues.

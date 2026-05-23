# 5. Feature Toggles

Date: 2019-05-21

## Status

Accepted

## Context

Toggles are a useful aspect of Terraform modules that provide the ability to
turn on/off functionality.

Capital One have written about
[Building Feature Toggles into
Terraform](https://medium.com/capital-one-tech/building-feature-toggles-into-terraform-d75806217647)
. This build on top of the use of the count and ternary to provide a more robust
feature toggle.

As this module is envisioned to be part of a larger Data Storage Module there is
a concept where no DynamoDB table may need to be provisioned. In addition, when
using DynamoDB Autoscaling can be a useful feature. Providing the capabilities
to turn this on and off based on requirements is also a useful requirement.

## Decision

Feature toggles will be leveraged to determine:

* If any resources should be created
* If a DynamoDB resource should be created
* If the Autoscaler should be enabled

## Consequences

When using Terragrunt consumers can utilise a `toggles.auto.tfvars` file to make
it clear what feature toggles exist.

When using Terraform alone with the module these flags are just properties on
the module being called.

Using the toggles in the module enables more flexibility and reduces complexity
in implmentation detail.

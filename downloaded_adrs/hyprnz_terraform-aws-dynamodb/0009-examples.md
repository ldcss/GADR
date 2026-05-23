# 9. Examples

Date: 2019-05-21

## Status

Accepted

Relies On [3. No Terraform Backend in Module](0003-no-terraform-backend-in-module.md)

## Context

Consumers need to know how to use the Terraform Module. This module has a number
of configurable options.

## Decision

The module will have several examples of how to use the module. Initially 2
examples named `base` and `complete` will be created. These should show how to
provide a minimal and a complete configuration.

This module may be used inside another module or in isolation, so these two
aspects should also be part of the example implementation.

## Consequences

The examples rely on a `local` backend which requires the ability for consumers
to configure the `backend`. This decision has been made in the `No Terraform
Backend in Module` ADR.

Consumers will be able to refer to these examples to see how to initially set up
and use the module.

Consumers can run the examples out of the box using the `local` backend.

# 3. No Terraform Backend in Module

Date: 2019-05-14

## Status

Accepted

Enables [9. Examples](0009-examples.md)

Amended by [10. Terraform Backend in Module](0010-terraform-backend-in-module.md)

## Context

Terraform requires a `backend` for state file storage. Most existing Terraform
modules within LIC have this `backend` set in the Terrform configuration in
`main.tf`.

Having the `backend` configured in the module means that consumers can't
overwrite the configuration. When building and testing modules it is useful to
be able to use a "local" `backend`.

## Decision

We have not set the `backend` configuration in the `main.tf`.

## Consequences

When running locally, such as when using the examples, the consumer can set the
`backend`. This enables the `backend` to be decided by the consumer rather than
the module.

When running in labelled environments the configuration will need to be set up
to use the appropriate backend. In most cases this will be the `s3` backend.

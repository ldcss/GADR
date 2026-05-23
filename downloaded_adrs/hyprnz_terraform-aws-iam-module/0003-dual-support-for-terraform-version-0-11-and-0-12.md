# 3. Dual support for terraform version 0-11 and 0-12

Date: 2020-03-17

## Status

Accepted

## Context

Terraform version 0.12 release was a major change with the API. Given the worked required to upgrade, it is envisaged that Terraform 0.11 will remain for quite some time.

## Decision

This module will support both version 0.11 and 0.12 of Terraform. Version 0.11 support will be managed from the 0.11 branch and tagged with a version pattern 0.minor.patch. Version 0.12 support will be managed from the master branch and tagged with a version pattern 1.minor.patch.

## Consequences

We predict that Terraform 0.11 usage will eventually decline and at some time a decision will be made as when to end support of Terraform 0.11. Supporting two versions of Terraform may introduce additional complexity with future implementations, and as such may accelerate any decision to end Terraform 0.11 support. There maybe scenarios where changes made to the 0.12 branch may not be ported immediately to the 0.11 branch. This may result in a batch of changes being applied to the 0.11, to maintain feature parity.


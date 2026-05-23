# 1. Open Source Shared Jenkins Library

Date: 2020-11-05

## Status

Recommended

## Context

1) We are [open by default](https://github.com/baloise/baloise.github.io/blob/master/design/OpenByDefault.adoc)
1) The myCloud API spec [is not confidential](https://github.com/baloise/CICD-pipeline/issues/15)
1) Openness is a driver for clean, secure design and good documentation
1) There are currently no obvious drivers for confidentiality

## Decision

We release the Shared Jenkins Library under Apache 2.0.

## Consequences

1) We follow the [Baloise Open Source Guidelines](https://baloise.github.io/open-source/docs/arc42/#_include_the_required_assets)
1) We need a second platform to exchange confidential information, like IP addresses or confidential documents. We initially use https://github.com/baloise/CICD-pipeline-private


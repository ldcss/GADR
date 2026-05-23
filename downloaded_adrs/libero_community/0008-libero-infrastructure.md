# 8. Limit scope of Libero infrastructure

Date: 2020-01-10

## Status

Proposed

## Context

Libero infrastructure (servers, Kubernetes, buckets) supports Libero development by providing demo environments.

Service providers need documentation to learn to run Libero products.

Service providers cater for the disparate, very specific needs of publishers.

Service providers may consolidate their infrastructure with the rest of the platforms.

## Decision

Libero infrastructure should serve two purposes:

- provide *demo* environments to showcase Libero products in certain configurations
- provide realistic *reference* environments that do not serve real users but can be forked and adapted by service providers to kick start their Libero offering

## Consequences

Demo environments for Libero products are run on Libero infrastructure.

Operational aspects that can be added to an environment without changing its architecture (e.g. backups, log aggregation) are considered out of scope for Libero infrastructure.

Libero Infrastructure As Code is not directly runnable by a third party.

Libero Helm charts are not directly installable by a third party.

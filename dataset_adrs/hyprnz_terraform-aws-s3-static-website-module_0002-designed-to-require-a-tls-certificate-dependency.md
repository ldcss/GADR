# 2. Designed to require a TLS certificate dependency

Date: 2020-01-20

## Status

Accepted

## Context

As https connections have become the standard for web connections this module needed to implement a TLS connection. An abstraction of how certificates and DNS is managed be users of this module needed to be abstracted away.

## Decision

While this module may have created a certificate resource, it was decided the use cases of any DNS management and certificate providers was too vast and that this module will take a certificate arn as a dependency.

## Consequences

This module does not provide an option to run without `https`. A certificate must be installed (created or imported) in the same AWS Account (AWS Certificates do not support cross account sharing) as where the module resource are being provisioned. Cloudfront certificates must reside in `us-east-1` region, a current constraint of the Cloudfront resources.

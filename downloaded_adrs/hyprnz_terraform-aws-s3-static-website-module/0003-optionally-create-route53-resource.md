# 3. Optionally create Route53 resource

Date: 2020-01-20

## Status

Accepted

## Context

It cannot be assumed that users of this module would manage DNS in AWS or that users may have a cross account design that prevents access to the hosted zone.

## Decision

Provide a means to create the custom Route53 resource as an option

## Consequences

The module will require additional testing to test implementations of the option turned off and on. Given there's is only one resource in question, the impact is negligible.

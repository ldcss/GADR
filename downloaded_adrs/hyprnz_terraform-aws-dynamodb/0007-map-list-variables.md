# 7. Map/List Variables

Date: 2019-05-21

## Status

Accepted

## Context

DynamoDB provides the ability to supply additional attributes, a local
secondary index and a global secondary index. These additional attributes
consumed by the DynamoDB AWS Provider as maps/lists.

In addtion to the consumption as maps/lists there are additional requirements
that the range/hash keys be added to the additional attributes if declared. They
are not added if undeclared.

## Decision

The module will use a `null_resource` to manage the secondary indexes. Creating
them from the existences of appropriate maps/lists.

Properties related to these resources will consume a list of maps as input.
These will them be mapped to the appropriate resource within in the module.

The range/hash key will be added automatically to the additional attributes by
the module, reducing the load on the consumer with implementation detail.

## Consequences

This provides a huge amount of flexibility for the module. Enabling secondary
indexes to be fully configured by consumers and additional attributes to be
added. In addition the consumer does not have to add the range/hash keys to
attributes as this is done automatically.

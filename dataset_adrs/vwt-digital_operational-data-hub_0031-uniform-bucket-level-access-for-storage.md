# 31. Uniform bucket-level access for storage

Date: 2020-09-30

## Status

Accepted

Implements [6. Implement Security by Design](0006-implement-security-by-design.md)

Related to [14. Single confidentiality level per data component](0014-single-confidentiality-level-per-data-component.md)

## Context

As motivated in [14. Single confidentiality level per data component](0014-single-confidentiality-level-per-data-component.md), access level granularity is kept at data component level. For buckets, this means uniform bucket-level access will be used, the more fine grained object-level ACLs will not be used.

## Decision

We will use uniform bucket-level access for storage.

## Consequences

Clear and transparent access to data. However, additional buckets are sometimes needed to store data with another accesslevel.

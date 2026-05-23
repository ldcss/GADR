# 14. Single confidentiality level per data component

Date: 2020-09-21

## Status

Accepted

Related to [31. Uniform bucket-level access for storage](0031-uniform-bucket-level-access-for-storage.md)

## Context

Granularity of access determines the boundaries of control regarding protection of confidential information. For example, a bucket has [uniform bucket level access](0031-uniform-bucket-level-access-for-storage.md). Therefore, all information in the bucket should have the same confidentiality level to make sure the right access permissions are applied.

## Decision

We will only store data of a single confidentiality level on a data component.

## Consequences

### Advantages

Management of access to confidential data is bound to explicit platform components. This prevents unintented disclosure of confidential information.

### Disadvantages

When handling information of different access levels, additional storage components must be created and used, coming with additional overhead.

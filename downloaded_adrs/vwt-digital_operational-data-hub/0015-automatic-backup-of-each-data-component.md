# 15. Automatic backup of each data component

Date: 2020-09-21

## Status

Accepted

Related to [12. Data catalog specifies all data components](0012-data-catalog-specifies-all-data-components.md)

## Context

To protect against data loss, a backup of all storage components should be implemented. As all data components are specified in the [data catalog](0012-data-catalog-specifies-all-data-components.md), automated backup can be implemented from this specification.

## Decision

We will implemented automated backup based on the [data catalog](0012-data-catalog-specifies-all-data-components.md) for each component that stores data.

## Consequences

### Advantages

Any component storing data on the platform will be included in the backup, protecting it for loss in case of any error or disaster occurring.


### Disadvantages

Backup has to be implemented for every component storing data that is used on the platform.

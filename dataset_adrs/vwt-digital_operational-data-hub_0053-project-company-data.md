# 53. Project company data

Date: 2020-09-21

## Status

Accepted

Implements [4. Create software defined everything](0004-create-software-defined-everything.md)

Implements [12. Data catalog specifies all data components](0012-data-catalog-specifies-all-data-components.md)

Implements [13. Data retention defined on each data component](0013-data-retention-defined-on-each-data-component.md)

Implements [52. ODRL policy](0052-odrl-policy.md)

## Context

Specifying the [data catalog](0012-data-catalog-specifies-all-data-components.md) requires a clear and specific way of documenting that is also suitable for automated processing.

A data catalog enables a publisher to describe datasets and data services in a catalog using a standard model and vocabulary that facilitates the consumption and aggregation of metadata from multiple catalogs. The challenge is to define and name standard metadata fields so that a data consumer has sufficient information to process and understand the described data. The more information that can be conveyed in a standardized regular format, the more valuable data becomes.

[Project company data](https://vwt-digital.github.io/project-company-data.github.io/) specifies a metadata format for data catalogs in a machine readable JSON format, covering the commonly required metadata attributes.

## Decision

We will use the [Project company data](https://vwt-digital.github.io/project-company-data.github.io/) to describe the data catalog.

## Consequences

### Advantages

* The formal specification allows automated processing for automation of data storage deployment.
* Easy gathering and management of metadata.
* Possibility to service the data catalog information in a portal.

### Disadvantages

* The machine readable JSON format can be hard to read and write for humans.

## References

* https://vwt-digital.github.io/project-company-data.github.io/, retrieved 9 October 2020
* https://www.w3.org/TR/vocab-dcat/, retrieved 9 October 2020

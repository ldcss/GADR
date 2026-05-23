# 12. Data catalog specifies all data components

Date: 2020-09-21

## Status

Accepted

Implements [4. Create software defined everything](0004-create-software-defined-everything.md)

Implemented by [53. Project company data](0053-project-company-data.md)

Related to [15. Automatic backup of each data component](0015-automatic-backup-of-each-data-component.md)

Implemented by [52. ODRL policy](0052-odrl-policy.md)

## Context

Metadata is structured information that describes, explains, locates, or otherwise makes it easier to retrieve, use, or manage an information resource (NISO 2004, ISBN: 1-880124-62-9). A Data Catalog is a collection of metadata, combined with data management and search tools, that helps analysts and other data users to find the data that they need, serves as an inventory of available data, and provides information to evaluate fitness data for intended uses.

By specifying the data catalog as part of the application code in a schema defined by [Project Company Data](0053-project-company-data.md), deployment of the data storage can also be done from the this metadata. By only creating storage from the data catalog, it is assured that all storage on the platform is defined in the data catalog. 
The data catalogs can be used to populate a Data Portal Platform (data catalog viewer). This makes the metadata in the data catalog accessible for users.

Together this leads to the implementation of Enterprise Metadata Management, the business discipline for managing the metadata about the information assets of the organization.
Developers specify the metadata with the storage declaration in the data catalog, which is part of the application programming code. On deployment the storage specified in the data catalog is created and the data catalog is published to the Data Portal Platform. Data governance employees, data analysts and business analysts use the Data Portal Platform to access the metadata.

## Decision

We will specify and deploy all storage on the ODH platform using a data catalog in the schema of [Project Company Data](0053-project-company-data.md).

## Consequences

### Advantages

Up-to-date Data Portal Platform. Populating the Data Portal Platform is completely automated, which ensures its completeness and correctness.

Support goverenance and control. A total overview of the data is a key requirement for the controls of data governance.

Support data analytics and business intelligence. The data catalog provides data scientists and business ananlists with information on available data.

### Disadvantages

Cost. Keeping a data catalog up-to-date requires tools and procedures to be maintained.

Additional developers work. Developers have to gather metadata on every storage component they need on the platform. Not all of this information is technically required, so it is important developers take the responsibility to specify also additional metadata at the right quality.

## References

* https://www.alation.com/blog/what-is-a-data-catalog/, retrieved 30 September 2020
* https://www.gartner.com/en/information-technology/glossary/enterprise-metadata-management-emm, retrieved 30 September 2020

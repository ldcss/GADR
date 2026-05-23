# DECISION 001 - Creation and use of the MetaData schema

## WHEN 
11- April-2020
## WHAT?
All data dictionary helpers will be kept within a schema called MetaData.

This schema will be deployed to the Data Catalog database in order to allow descriptive comments to be attached to Data Catalog artefacts

## WHY?
The Data Catalog product uses the dbo schema.

These helper objects are not part of the product so by choosing to create a new schema we provide a clear and visible boundary between our artefacts and those of the product.

A product upgrade is unlikely to suffer unexpected failure caused by choosing an object name that later turns out to be part of the product.

## See Also
* [Light Weight Decision Register](README.md)

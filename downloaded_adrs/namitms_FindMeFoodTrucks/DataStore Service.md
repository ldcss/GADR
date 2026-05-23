# :bulb: Datastore service selection

:calendar: Date: 2/10/2020

## :heavy_check_mark: Status : Accepted

## :dart: Context

Select the service to be used for the non-relational data store given the following application considerations:
1. The type of data is non-relational
1. Data is de-normalized
1. The total number of records is less than 1000
1. The total number of columns is less than 30
1. Data to be stored is less than 1 GB
1. Data store will not require geo-redundancy
1. Data store will not require to scale automatically

## Considerations
The following datastore technologies were considered:
1. Azure SQL Database : Not ideal because the data is non-relational
1. SQL Database Instances : Not ideal because the data is non-relational
1. Azure Table storage : Not ideal because of the limited support on Geo-spatial data types and SQL querying
1. Azure Database for MySQL : Not ideal because there are no portability requirements
1. Azure Cosmos DB : Ideal as it is schema agnostic, battle tested and supports SQL like queries.

The recommended service for Datastore is Azure Cosmos DB.

The decision is based on the guidance provided by Microsoft here: https://docs.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-store-considerations

## :trophy: Consequences

Choosing Azure Cosmos DB will help developers use their existing SQL skills in querying the data store. The technology also saves effort on index management and can be optimized for cost by using the right hosting model.  
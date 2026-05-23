# :bulb: Datastore - Relational or Non-relational

:calendar: Date: 2/10/2020

## :heavy_check_mark: Status : Accepted

## :dart: Context

Given the following application requirements, a data store technology needs to be chosen to persist the data from the sfgov api.
1. The type of data is non-relational
1. Data is de-normalized
1. The total number of records is less than 1000
1. The total number of columns is less than 30

## Considerations
1. Normalize the data (schema on write) and store it in a relational data store
1. Keep the data de-normalized and use a non-relational data store

Considering the nature of the requirements to query the information only on location coordinates, normalization will not add much value. It is preferred to use non-relational data store for this application

Reference : https://docs.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-store-decision-tree

## :trophy: Consequences

Choosing a non-relational data store will help preserve the data in the raw format and support applying schema on read. This will also save the over head of normalizing the data while storing it.
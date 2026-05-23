# ADR 015: EVA REST search

## TL;DR
EVA are strongly discouraging the direct use of the MongoDB instance, and have requested we use the REST API instead, which requires a new implementation

## Context
EVA discourage direct use of the Mongo instance on the grounds:
1. The schema is not stable
2. The schema is complex e.g. mapping samples to genotypes
Given this, a new Search implementation is needed that uses the following endpoints:
https://www.ebi.ac.uk/eva/webservices/rest/swagger-ui.html#!/variants/getVariantsByRegionUsingPOST
https://www.ebi.ac.uk/eva/webservices/rest/swagger-ui.html#!/variants/getVariantByIdUsingGET

## Decision
A new `Search` implementation has been developed, `EVARestSearch`. 

This search needs to take care of the following tasks

### Querying
Query fields need to be split up into the following classes:
1. Mandatory - ID or sequence region plus species_assembly
2. Optional server filters 
3. Optional client filters
These need to be applied in the correct way to the correct endpoint.

The species_assembly string will be looked up from an Ensembl style genome name, as to support joining better.

### Filtering
The server only excludes a subset of fields, so most exclusion must take place on the server

### Faceting
Cannot be supported

### Sorting
Cannot be supported

## Status
Under development

## Consequences
Querying severely limited
Sorting is not supported
Faceting is not supported

## Tags

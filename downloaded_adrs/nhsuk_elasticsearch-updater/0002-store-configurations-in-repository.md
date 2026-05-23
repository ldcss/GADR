# 2. Store configurations in repository

Date: 2017-07-03

## Status

Accepted

## Context

The application loads data from a JSON file into an Elasticsearch instance. Along with the raw data the import 
also needs to create mappings and transform data to improve search rankings or provide geolocation searches. 
These are rich complex JSON objects or functions that cannot be passed in as environment variables. 

## Decision

Given the small number of databases (currently only GP Profiles data is held in Elasticsearch) it is pragmatic to co-locate the Elasticsearch configuration alongside the `elasticsearch-updater` code, rather than creating a new repository and file hosting for each mappings and transform.

## Consequences

Elasticsearch configurations can be reliably duplicated across environments with minimal enviroment variables.

Elasticsearch configurations are tracked in source control.

Configuration settings for an Elasticsearch index must exist within the `elasticsearch-updater` repository, i.e. it is not possible to load data into a bespoke Elasticsearch index from environment variables alone.

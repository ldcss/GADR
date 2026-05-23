# 2. Store Common Database Configuration in the Repository

Date: 2017-06-19

## Status

Accepted

## Context

The application loads data from a JSON file into a mongodb database. Along with the raw data the mongo database
may also need to create indexes to improve search performance or provide geolocation searches.

The configuration of a database such as database name, collection name, indexes and ID key remain the same
across environments.

## Decision

As the index may be fundamental to the operation of the consuming application, such as the geolocation search in the pharmacy database,
these configurations should be stored in version control.

Given the small number of databases (currently only Pharmacy, and GP Profiles data are held in mongodb) it is pragmatic to co-locate the configuration files
alongside the `mongodb-updater` code, rather than creating a new repository and file hosting for each database configuration files.

## Consequences

Database configurations can be reliably duplicated across environments with minimal enviroment variables.

Database configurations are tracked in source control.

A database index may not be set by an environment variable. A database which requires an index will need a suitable configuration added
to the `mongodb-updater` repository.

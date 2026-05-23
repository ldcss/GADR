# Uploaders ADR


## Status

Accepted

## Context

Monolith and a few deployed jars handling delivery of data feed files into S3 for the existing parsing processes powering the monolith client data hub system, this increases cost on the monolith's systems which require more vertical scaling of resources to manage, more so, due to the monolith lock, any fix or update is locked to the monolith release SDLC.

Considering these functions serve to move files from source to destination we need to migrate them as external services to both CDH and the monolith, these are then bundled into a single service responsible for the delivery of new data feed files into the S3 Archives and CDH feed data stores.

## Decision

Migration of all monolith related uploading logic into external service which is responsible for the timely retreival, delivery and storage of data feed files from their respective sources. The service is responsible for ensuring the ETL service database is always up to date, by deliverying events on file additions into the archive storage regardless of what storage is being used by event delivery.

![Data Feed Delivery](../assets/images/workflows/image8.png)

## Consequences

A new service must be deployed along side the ETL service which will be responsible for the delivery of all new data feed files into our cloud storage (regardless of vendor) and will deliver events to the ETL service to update it's database records on new files within those filestores.
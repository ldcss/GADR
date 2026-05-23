# XML Freshness

## Context

* Our application works by indexing an XML file given by WikiMedia
* WikiMedia manually create a new XML file twice a month on average
* We have not been given an indication on how fresh the data our service provides needs to be
* We want the software to be deployable without relying on a shared file system

## Decision

* We store the XML dump in this git repo and update it when we need to
* The file will be accessed over http to allow us to move to a different storage solution in the future

## Alternatives Considered

* As per [ADR-001](adr-001-search_and_indexing) we could store the file in a database and update it using an async process
* Downloading the file straight from WikiMedia. This would use an excessive amount of their bandwidth, and our service would need to have a connection to the internet.
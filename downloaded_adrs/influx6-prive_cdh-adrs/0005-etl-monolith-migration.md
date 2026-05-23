# ETL Monolith Migration


## Status

Accepted

## Context

Currently, the parsing process for datafeeds is still part of the existing monolith codebase, which brings it's own share of problems with scaling and feed parsing managemnent. Monolith also has a hard dependency on AWS S3 which must be broken out to allow us specfically move these dependencies outside as they are not relatively core to the ETL processing architecture but are generally how we organize and move input into desired place for access and delivery. 

A hard requirement for the ETL service is the ability to ensure processed datafeed consistently have relational information with their tenants as specific feeds
have specific constraints on how they are accessed and stored.

Another hard requirements is to organize how data feed files are accessed and retrieved from S3, this currently has issues due to the need to directly access S3, and move files and directories into the bulkupload directories for processing by the monolith. Whilst the alternative of storing both file, metadata and file binary into the database simplifies these access issues, we create more problems in the management of the database files (without using FileStream optimization in SQLServer), increasing cost of backup and replication. 

## Decision

ETL will be moved into an external service of it's own with the following responsibilities:

- Embodiment of all parser logic.
- Delivery of agreed parser format (currently PriveXML) into message queues.
- Standardized library for parsing delivery and logic.
- Standardized database tables for data feed file delivery and access.
- Standardized database tables for tenant data (Company, Client, Accounts).
- Creates tenant specific events for delivery for tenant specific datafeed.

As regards data feed file access problem

- Manage synchronization of uploaded files events into database from uploader service.


## Links

- https://habiletechnologies.com/blog/better-saving-files-database-file-system/
- https://dzone.com/articles/which-is-better-saving-files-in-database-or-in-fil
- https://codingsans.com/blog/nosql-vs-relational-database
- https://systemswemake.com/2012/12/22/to-blob-or-not-to-blob/
- https://www.codeproject.com/Articles/28416/Best-Practice-in-File-Storage-while-Building-Appli



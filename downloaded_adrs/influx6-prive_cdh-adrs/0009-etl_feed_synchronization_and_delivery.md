# ETL Feed Synchronization And Delivery


## Status

Accepted

## Context

Currently, we move files around in S3 from Archive folders into bulkupload folders which is cumbersome and error prone, 
more so this is being done to allow us trigger data feed processing from the dev admin. 
We need a means of reducing the flow steps to go from files to processing and reduce surface level access for the ETL team.

## Decision

- ETL will have a dedicated database tables which will serve the need to both register and retrieve data feed files in the 
most optimized manner necessary on a per feed basis. This database tables will be appropriately updated by the ETL service 
based on update events from either the uploader service, or the windows-specific uploader jars.

The following operations then becomes possible:

1. Ability to query for specific files based on upload date (the date it was uploaded to S3).
2. Ability to query for a specific batch of files related to specific data feeds.
3. Ability to get data files specific to a given owner and/or provider.
4. Ability to get data files specific to a given provider.


- Due to we creating a database to optimize a query to retrieve and manage data feed files, then we require a way to keep 
the ETL database tables up to date with new files from uploader service. Therefore, the ETL system will listen for events coming 
from both a lambda function which will be called by S3 when new files are added to the specific bucket, and the new uploader
service which will house necessary logic for retrieving such data feed files from their sources. Once all uploading logic 
have being migrated to the uploader, we will de-commission the lambda function and directly have the uploader service inform the 
ETL service as regards new files.

See
![Data Feed Delivery](../assets/images/workflows/image8.png)


## Consequences

We need to create a set of database for the 3 major parts of the database ETL system:

These requirements require four major MySQL tables:

1. Data Feed Source Table

ID | Name | ShortName | URL  | CREATED DATE
-- | ---- | --------- | ---- | -------------
1211 | VARCHAR | VARCHAR | VARCHAR | UTC

Data feeds table will contain a list of registered data feed sources (think CreditSuisse, etc) which provides consistent unique IDs specific to each data feed.


2. Data Feed EAM Table (DataFeedEAMS)

ID | Name | Owner Key [Legacy EAM KEY] | Short Name | DataFeed ID [Foreign Key] | CREATED DATE
-- | ---- | -------------------------- | ---------- | ------------------------- | -------------
INT | VARCHAR | VARCHAR | VARCHAR | INT | UTC

This table exists to house specific details for each EAM with a unique identifier which should be separate from whatever concepts ETL identifies an EAM has. 
What we want is to enrich categorization of which entity the files belong to.

This table has a Many to One relationship with the EAM tables in 1. This means you can have multiple rows with the same `Name` field but for different `DataFeed ID` for EAMs providing different feeds from specific data feed sources.

The Owner Key column is a user defined key which we can use to create consistency between existing EAM representation in monolith and the new EAM structure in our ETL, which will allow monolith the possibility of utilizing the ETL database directly for file retrieval.

3. Data Feed Data Table (DataFeedData)

ID | EAM ID | Name | Type | MetaData | Data URL | Uploaded Date | Created date | Marked as Deleted | Marked as Disabled
-- | ------ | ---- | ---- | -------- | -------- | ------------- | ------------ | ----------------- | --------------------
INT | VARCHAR | VARCHAR | XML | JSON | VARCHAR | LOCALIZED DATE | UTC | BOOLEAN | BOOLEAN

This table will contain rows of binary blobs stored with associated EAM identifiers from DataFeedEAM tables and will exist specifically to identify a given data to a specific EAM, which will allow exploratory options for reaching directly into the tables to pull out specific data blobs for data research.
The `MetaJSON` will contain associated meta information desirable to be attached to such files, which may serve to enrich exploratory processes and processing operations.

Trade off: We could suffer from very large database files with every increasing cost of backup. Generally it’s advised to use object stores like S3 for the file contents and simply use paths to indicate in the database where these are stored. This means we need to ensure db is synchronized with s3 though which is a problem itself, hence this may suffice for now.

4. Data Error Data Table 

ID | Message | EAM ID | DataFeed ID | ErrorType | TraceData | CREATED DATE
-- | ------- | ------ | ----------- | --------- | --------- | -------------
INT | VARCHAR | INT | INT | VARCHAR | INT | TEXT | UTC

This table contains different errors found within the parsing process for giving data feed which is considered non-critical and allowable during the flow of parsing a given data feed source. It’s expected only errors that are critical that will affect correctness should cause a total stop of parsing for a source or set of sources, or the whole operation (this will need explicit definitions)

There are 3 levels of errors: 

1. Non critical that allows continued processing of file (with alerting done to inform)
2. Middle Level critical that stops just the processing of that file (with alerting, and ending of that particular file’s process)
3. High Critical Level where the whole parsing process halts with adequate error detail as to why.



# 4. Build Image with GP Data

Date: 2017-06-15

## Status

Accepted

## Context

Other work within the same domain has created a JSON file containing all GP practices that need to be searched and exposed via ES. This datafile was originally created to be loaded into MongoDB. Whilst Elastic Search (ES) can import the JSON document in the existing format it takes considerable time. Re-shaping the data to that required by the bulk import API of ES means the import can happen in a matter of seconds rather than many minutes otherwise.

## Decision

We will use the existing data file but reshape the data specifically to suit the needs of ES.

## Consequences

- The updating of the source GP data file in this repo is a manual process with no set schedule. This will likely be superseded by the GP data ETL processors in the near future.

- As well as reshaping the GP JSON document for bulk insert some manipulation of the properties was necessary to optimise for particular search requirements. The reshaping was carried out using `jq` (a JSON processing CLI tool) as a lightweight way of doing this but did mean that there are no tests around the reshaping.

- Since the data is loaded during `docker build` then the Docker image contains ES loaded with the GP data making it easy for applications to use. 

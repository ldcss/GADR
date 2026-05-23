# 3. Store Host output file in ETL container

Date: 2017-06-07

## Status

Accepted

## Context

The ETL process takes a long time to run, approximately 6 hours.
Running the ETL process makes close to 30,000 requests to the Syndication API.
Several applications need access to the JSON file created by the ETL.

## Decision

Rather than each application running its own copy of the ETL to obtain the Syndication data in JSON format,
a single instance of the ETL will run and provide access to the resultant file via an nginx web server
running in the ETL container.

The output JSON is hosted in the container to remove reliance on external solutions, such as Azure.

## Consequences

A single ETL runs every night to gather the data, reducing load on the Syndication API.

There is a single point of failure - if the ETL has not run, or the site is not available then consuming
applications have no access to the latest Syndication data.

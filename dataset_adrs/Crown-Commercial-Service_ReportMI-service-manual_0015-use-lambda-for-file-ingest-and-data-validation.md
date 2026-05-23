# 15. Use Lambda for file ingest and data validation

Date: 2018-07-19

## Status

Accepted

## Context

In [ADR-0002][adr-0002] we outlined the overall technical approach for the Data
Submission Service, and highlighted the components which we expect will be
developed.

This ADR focusses on the technology choice for building a portion of the
features. In particular:

1. File transformation service - a small service for extracting data from an
uploaded file, transforming it into a useful format and storing it via the API
(a process we're currently calling 'ingest').
1. Data validation service - a service for validating the data provided by
suppliers and calculating the appropriate management fee.

### Features of these services

These services have to handle large peaks in traffic, but will be rarely used
for a large part of the month.

The file transformation service will need to handle multiple files, of different
formats, at the same time, some with well over 100,000 rows of data.

The data validation service will need to perform validation and calculations on
each row within the data.

To provide a good user-experience, we want these services to operate quickly and
provide feedback to users.

These services will need to apply custom rules based on the framework the report
applies to. For example the fields of data provided for G-Cloud 9 are different
from General Legal Services, and the process for calculating the management fee
is different for Rail Legal Services and Courier Services.

### Serverless

Serverless technologies are designed to run code without the need to manage
infrastructure, which allows it to scale easily. Generally, you are only billed
for the time it takes to run the code - usually charged in fractions of a
second.

Developing these services to be hosted as a serverless function would allow us,
in theory, to infinitely scale the file ingest and validation parts of the
service and only pay for what is actually needed.

Each of the main cloud providers has their own implementation of a serverless
hosting option including Azure Functions, Google Cloud Functions and AWS Lambda.

## Decision

We will use AWS Lambda for the ingest and data validation processes.

We can deploy a different Lambda function for each file type we expect to
ingest, and split the data validation scripts into easy-to-maintain functions.

## Consequences

We will need to use Terraform to deploy the Lambda functions to the AWS
environment, and we will need to design an appropriate way of orchestrating
calls to the Lambda functions.

[adr-0002]: 0002-overall-technical-approach.md

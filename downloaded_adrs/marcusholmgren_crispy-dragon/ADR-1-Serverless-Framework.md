# ADR1: Use Serverless Framework
Date: 2021-02-03

## Status
Accepted

## Context
The resources, database, storage and API endpoints needs to be managed as a unit. 
When build our application with the Serverless framework we get CloudFormation templates that manages our infrastructure in AWS.

## Decision
To help package the individual AWS resource into a serverless application we will use [Serverless](https://www.serverless.com/) framework.

We also considered the following alternative solutions:
* Manual creation of resource in AWS throurgh the AWS Console.
* AWS Serverless Application Model (AWS SAM)

## Consequences
* We need to learn Serverless patterns and usage style

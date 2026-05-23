# 5. Serverless framework - Chalice

Date: 2017-11-22

## Status

Accepted

## Context

My first instinct for the tool was to use the 
NPM [Serverless](https://serverless.com/) framework.

The main advantage of serverless is that it is cloud 
agnostic. However JavaScript is not widely used at GDS.

AWS [Chalice](https://chalice.readthedocs.io) is a similar 
framework which has a multi-stage deploy process to 
automate provisioning Lambda and Api Gateway but written 
in Python. 

Both languages have frameworks for accessing the AWS API: 
* The [SDK](https://docs.aws.amazon.com/sdk-for-javascript) 
for JavasSript and 
* [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) 
for Python.  

## Decision

Given that we had already made the decision that cloud 
agnostic was not important for this service and that 
Python was more in keeping with GDS common practice we
decided to use Chalice.  

## Consequences

Chalice is AWS specific and written by AWS. 

If we do build other tools which we do want to be cloud 
agnostic we may not be able to re-use components as 
readily. 

We have additionally made the decision to code in Python.

 




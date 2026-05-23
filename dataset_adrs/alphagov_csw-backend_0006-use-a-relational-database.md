# 6. Record architecture decisions

Date: 2017-11-22

## Status

Accepted

## Context

We needed some persistent storage of audit results. 

We considered: 
### Schemaless - DynamoDb 
This would be the most obvious choice for a lambda based 
service. 

The dynamo data model is tables of key value pairs.

The main problem with Dynamo is the limit of I think 4K 
per value. 

One of the things we wanted to do was briefly cache API 
responses which could easily breach that 4K limit.

With Dynamo the access control is via IAM which would be 
relatively easy to manage and encryption at rest can 
be easily configured.  
 
### Schemaless - MongoDb

Mongo was a better fit for our service, saving JSON 
representations of API responses and resources. 

The problem with Mongo is it's not AWS native so we'd 
have to provision a server, manage the access controls, 
maintenance and availability. 

### Relational - RDS MySQL / PostgreSQL 

RDS gives us the benefit of running a managed service so 
AWS are responsible for backups and patching minor 
version. 

Relational databases give us the ability to do on-the-fly 
analysis more easily. 

We can store JSON as blob data although not ideal. 

If we want to re-use the database instance as a shared 
resource across multiple services RDS is more capable. 

It's not unlikely that a future development may require 
django. 

PostgreSQL seems to be the general direction of travel 
in GDS and is much more capable for a wider range of 
use-cases where we don't know what we're building in the 
future. 

## Decision

Whilst none of the options were perfect we decided that 
a PostgreSQL RDS was the best option given the 
information available to give us an infrastructure to 
support multiple tools and services.  

## Consequences

The decision to implement a VPC [ADR 7](0007-implement-a-vpc.md) was 
partly a consequence of the decision to implement RDS.


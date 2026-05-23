# 2. Persistent Storage uses DynamoDB

Date: 2019-02-21

## Status

Accepted

## Context

* The application will require persistent storage for storing LPA ownership, granted access, and possibly user credentials
* Current MoJ strategy is to use managed services where possible

## Decision

Use DynamoDB for persistent storage

## Consequences

Reduced cost, Faster build and destroy times, and easier to run local versions for development (compared to AWS RDS Aurora or Postgresql)

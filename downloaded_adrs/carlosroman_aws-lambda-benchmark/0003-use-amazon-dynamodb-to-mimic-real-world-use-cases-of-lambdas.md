# 3. Use Amazon DynamoDB to mimic real world use cases of Lambdas

Date: 2018-08-24

## Status

Accepted

## Context

To make the benchmark more meaningful we will want to make them to be more like real world Lambdas. A typical pattern we see with lambdas is fetching data from Amazon DynamoDB.

## Decision

With the deployment of the Lambdas and API gateway we will also deploy a DynamoDB table.

## Consequences

The Lambdas will mimic more realist real world user cases by accessing data from DynamoDB.


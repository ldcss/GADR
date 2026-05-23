# 2. Store incoming payloads to S3

Date: 2021-10-01

## Status

Accepted

## Context

We have a requirement to store the JSON messages that arrive in the request bodies to the EventController endpoints and this is done to an S3 bucket where they can be retained securely for 28 days. This could have been done by adding a service call in the EventController itself.   

However, the EventController is a spring-managed endpoint and receives the payload already transformed into the required ```Hearing``` instance. If there was a problem parsing the payload, it would never arrive in the endpoint and the opportunity to store would have been lost. 

Alternatively, a Filter could be implemented which intercepts the request before it arrives at the endpoint. This requires more code and a little more development effort.

## Decision

Decision taken to implement Filter so that no request body is lost.

## Consequences



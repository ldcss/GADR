# 1. Increase pod memory limit for OOM error

Date: 2020-01-05

## Status

Accepted

## Context

We have received a couple of Out of Memory errors in relation to large pdfs which cause a problem themselves or when they are combined through the `count` parameter.

## Decision

Given the low number of occurances it has been decided to simply increase the memory available to the JVM in the pod.

Should this problem continue to occur we will need to look at options such as:
* Streaming the zip file data to the SFTP server directly
* Storing binary data in Blob Storage instead of Postgresql and potentially shifting processing to a tmpfs volume

## Consequences

Increased memory consumption for the send-letter-service pods

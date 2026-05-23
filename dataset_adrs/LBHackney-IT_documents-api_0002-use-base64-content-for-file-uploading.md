# 2. Use base 64 content for file uploading

Date: 2021-06-24

## Status

Accepted

## Context

There are a number of ways an API could allow clients to upload files to S3, the popular ones:
- Allow the API to accept Base 64 encoded files in a JSON POST request and subsequently send this blob to S3
- Allow the API to accept multipart form uploads, compile the parts on the server then send the file to S3
- Use the S3 Presigned URL functionality, which allows the client to act as the IAM which created the URL for a single operation, and upload the file directly to S3 themselves

## Decision

We decided to use the first option (base 64 encoded uploads), for the following reason:
- We do not want to expose any AWS links to outside parties. This ensures that all access to AWS resources is controlled by Hackney authentication mechanisms.

## Consequences

It is a slightly slower option compared with presigned URL so the user's experience will suffer a bit.

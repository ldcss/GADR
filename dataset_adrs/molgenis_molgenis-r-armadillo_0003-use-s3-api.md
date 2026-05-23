# 3. Use S3 API

Date: 2020-06-02

## Status

Accepted

## Context

* Minio already has a UI and an S3 API that allow administration of files and buckets.
* There are existing client libraries for the S3 API.
* It is nontrivial to proxy large file uploads through the armadillo server.

## Decision

The Armadillo client will be written as a high-level library on top of an existing S3 API.

## Consequences

### Open minio to the local data manager
The Minio instance will need to be accessible to the local data manager.
+ Armadillo server, which is exposed to a larger audience, does not expose access to the file system
- Minio API is exposed to the local data managers

### Federate ID from minio to ID Provider
Local data manager logs in with Minio so Minio has to federate to the ID Provider.
ID Provider needs to specify the access policy as claim in the ID token. 

### Free UI
Local data manager can use the Minio UI.
+ free UI, less work
- General purpose UI that does not know about cohorts and versions and metadata

### Access policies
Access policies are configured in Minio.
+ Configuration instead of code
- The s3 config is pretty verbose if you need more than the precanned ones

### Armadillo client uses (parts of) S3 api
+ Free library, less work
+ Multi-part upload works out of the box
- Becomes harder to switch file storage to non-s3 implementation

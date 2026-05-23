# 9. Use AWS KMS to manage session encryption keys

Date: 2019-05-01

## Status

Accepted

## Context

Following on from [8. Session storage using an encrypted cookie](0008-session-storage-using-an-encrypted-cookie.md)

* The encrypted cookie will need to be encrypted using a key.
* Keys should be able to be rotated easily and often.
* Key rotations should have no effect on active users.

## Decision

* We will use AWS' KMS to manage our encryption keys.
* Keys will be cached at the contained level in volatile memory.

## Consequences

* Responsibility for the generation of keys will be solely on AWS.
* Responsibility for the storage of long lived keys will be solely on AWS.
* The size of the cookie value will be larger
    * This is seen as outweighed by the above benefits.
* Caching the keys on the container will:
    * Ensure we don't hit KMS' hard limits on requests; and
    * Improve performance.

# 36. SSL certificates are always verified

Date: 2020-09-21

## Status

Accepted

Implements [6. Implement Security by Design](0006-implement-security-by-design.md)

## Context

When using SSL, certificate verification ensures the identity of the other party we're communicating with. Using unverified certificates makes the communication more vulnerable to man-in-the-middle attacks. Certificate verification can be done using a trusted Certificate Authority (CA) or by pinning the certificate (importing a host's certificate in your trust store).

## Decision

We will only use verified SSL certificates.

## Consequences

Using verified certificates greatly reduces the risk of man-in-the-middle attacks, preventing information ending up at unintented places. Many components on the platform facilitate managed certificates, resulting in CA trusted certificates. Configuring certificate pinning is somewhat more complicated, but will only be needed in a limited amount of specific situations.

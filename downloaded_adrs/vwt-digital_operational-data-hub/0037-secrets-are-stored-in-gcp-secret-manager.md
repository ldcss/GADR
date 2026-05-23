# 37. Secrets are stored in GCP Secret Manager

Date: 2020-09-21

## Status

Accepted

Implements [6. Implement Security by Design](0006-implement-security-by-design.md)

## Context

Secrets must be protected according to the least-privilege principle. To reduce the trusted computing base, preferrably a 3rd party secret management tool is used to manage and use secrets. Google Secret Mananager is a managed service on GCP, integrated into the platform. This makes it a suitable tool to manage our secrets.

## Decision

We will use GCP Secret Manager to manage, store and use secrets.

## Consequences

Secret Manager provides a secure and reliable way to handle secrets. It is integrated in the platform, which simplifies using it. Outside the platform (e.g. external services) can use it through the API. However, authenticating to Secret Manager requires special attention in that case.

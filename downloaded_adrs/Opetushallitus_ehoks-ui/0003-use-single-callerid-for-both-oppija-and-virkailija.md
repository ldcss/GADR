# 3. Use a single Caller-Id for both oppija and virkailija frontend requests

Date: 27.03.2020

## Status

Accepted

## Context

Every service is required to pass a Caller-Id header with its requests and previously eHOKS frontend had separate
ids for oppija and virkailija. While the codebase is largely shared between oppija and virkailija the services themselves
are separate and hence the separate ids were created. While the headers were simple to add to requests made by
components only used by either oppija or virkailija, dynamically figuring out which id should be used in the shared
components at any given time proved harder.

## Decision

The separate ids will be replaced by a single frontend Caller-Id. Since all the requests made by both oppija and
virkailija frontends go through the eHOKS backend service and don't call any external services directly this
should be sufficient. The requests from oppija and virkailija can be distinquished from each other via other means,
eg. they use different backend APIs altogether.

## Consequences

All requests made by the frontends can now easily include the Caller-Id header. If the need arises to filter which
frontend is responsible for a particular request it cannot be done by just checking the Caller-Id header.

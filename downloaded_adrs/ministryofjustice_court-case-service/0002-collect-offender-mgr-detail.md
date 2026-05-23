# 2. Collect offender manager detail from new Community API endpoint

Date: 2020-12-10

## Status

Under review

## Context

The "probation-record" endpoint in court-case-service gathers information about an offender, including offender managers from the community API, using the endpoint at `/secure/offenders/crn/{crn}/all`. 

The ticket https://dsdmoj.atlassian.net/browse/PIC-1016 requires us to gather information for telephone number and email for the offender managers. This is available in community API but via an LDAP repository which is not currently used to gather any other part of the detail for the offender manager.

## Decision

Addition of the extra fields to the existing endpoint is likely to add a significant performance overhead for no benefit to any other consumers of the endpoint. 

We will not alter the existing endpoint (`/secure/offenders/crn/{crn}/all`).

We will add a new endpoint to Community API to get offender managers (community and prison), at `/offenders/crn/{crn}/allOffenderManagers`. This will follow the example of the existing endpoint which does the same at `/offenders/nomsNumber/{nomsNumber}/allOffenderManagers`. This returns Prison and Community Offender Managers in two separate lists. The phone and email fields for Prison Offender Managers are already set. We will ensure that it is set for Community Offender Managers, via the LdapRespository, where it is available.

We will alter court case service to use this new endpoint for offender managers. Court case service will filter the prison offender managers from the probation record.

## Consequences

Prepare a case will have the extra contact details available.

We should monitor performance during development and deployment to determine any effect on the overall retrieval of the probation-record.

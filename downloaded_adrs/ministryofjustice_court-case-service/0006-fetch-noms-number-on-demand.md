# 6. Fetch nomsNumber on demand on calls to custody endpoint

Date: 2021-07-21

## Status

Accepted

## Context

The call to the prison-api to get custody data requires a nomsNumber as the identifier. This is a new identifier for the court-case-service and two options were identified as ways we could get this: 
1. Incorporate nomsNumber into the case model, retrieve it as part of the matching process and have prepare-a-case pass it in the request to the custody endpoint
2. Use CRN to retrieve this data on demand from the community-api

## Decision

Option 2 chosen - Use CRN to retrieve this data on demand from the community-api.

## Consequences

- Implementation is simpler and constrained to one endpoint in court-case-service
- CRN is consistently used as the primary identifier for an offender within court-case-service
- An additional api call must be made by court-case-service to community-api on every call to custody endpoint
- nomsNumber will always reflect the current state in Delius. This is beneficial as nomsNumbers are known to be frequently duplicated/deduplicated/updated in Delius

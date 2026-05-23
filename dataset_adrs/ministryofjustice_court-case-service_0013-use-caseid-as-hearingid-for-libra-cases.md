# 13. For Libra cases, use the caseId as the hearingId

Date: 2022-05-18

## Status

Accepted

## Context

`court-case-service` was originally built solely to handle cases from Libra. Later, we made significant changes to support Common Platform data as well. Relatively late in the day we discovered that we were handling Common Platform data incorrectly, and to resolve this we would have to introduce the concept of a `hearing` which does not exist as a separate entity to a case in Libra. This work started with ticket [PIC-2023](https://dsdmoj.atlassian.net/browse/PIC-2023). At this point the Common Platform integration had been substantially completed and we did not want to break existing functionality whilst these further changes took place. This meant that in the interim both Libra and Common Platform cases had all of their `hearingId` set to the same value as their `caseId`. For Common Platform, this was always intended as a temporary measure and these id's are now completely independent values. However, as there is no separate concept of a `hearingId` for Libra cases we continue using the `caseId` for both ids. 

There is a related phenomenon which affects Libra cases from the pre Common Platform era, where the `caseId` and therefore `hearingId` of these cases is not a UUID but a long integer similar to `caseNo`. This is because Libra payloads have their own `caseId` which for a time in the early days of the service we used as the primary business identifier for a case. We later learned that this was not reliable so we switched to using a compound key of `caseNo` and `courtCode` to uniquely identify a case, so this field fell out of use. When we did the Common Platform integration the decision was made to repurpose this field as it was no longer used, rather than create a new field with a different name as it seemed that in the long run this would create less confusion. For this reason we're unable to use the UUID data type in Postgres and must treat it a simple string until such a point as the long tail of these cases has been cleared down and archived or deleted.

Note - Libra cases also don't have a separate concept of `defendantId` but this relationship was well understood from the outset so we took the decision to generate a unique uuid as `defendantId` for Libra cases. The only reason we have not taken this approach again was to allow the application to continue operating whilst we made the above changes, so we have knowingly introduced inconsistency, hence this ADR.


## Decision

Use `caseId` for Libra case `hearingId`.

## Consequences

- There is inconsistency between how we treat `hearingId` and `defendantId` relative to `caseId` for Libra cases
- At some point we may want to resolve this by either using unique UUIDs for both, or by using the same id for all 3 ids

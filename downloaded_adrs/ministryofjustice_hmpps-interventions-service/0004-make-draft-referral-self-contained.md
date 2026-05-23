# 1. Make draft referrals self contained

Date: 2023-01-26

## Status

Accepted

## Context

We store data in the service database about draft referrals in a table which contains some sensitive personal data and are 
looking to add new fields relating to drafts.
It would be difficult at the moment to delete this when no longer used due to referential constraints, which means we store
unnecessary data and causes concerns relating to GDPR.

## Decision

We decided to add no further referential constraints on the DRAFT_REFERRALS table, and 
move to a point where existing constraints are dropped and a job/task added to remove records more than a month old. 

## Consequences

1. DRAFT_REFERRALS table should ideally store all fields needed to store a draft.
2. The draft data should be considered temporary
3. Previous referential constraints which link to production data tables are targets for removal
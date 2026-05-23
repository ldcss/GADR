# 2. CDH ETL Logic Boundaries

Date: 2020-10-29

## Status

Accepted

## Context

To ensure a clear separation as regards what logic resides within CDH and ETL related services where there exists feed specific 
requirements during onboarding and processing of feed files, the following issues where considered:

- Will such logic require specialized implementation across feeds?
- Are such logic generic and require one time implementation or will require continous change/update?
- What are the benefits of moving such logic into ETL instead of CDH.

## Decision

The most important point agreed on was that CDH will remain focused on defined object and data models as possible and CDH will 
run with the expectation that all inputs received are completed. This means CDH should not have domain specific knowledge in regards
specific intricacies about how specific feeds are reconcilied into complete Positions, Transactions and Ticker data.

Such specificity will reside within the ETL service and be housed based on each feed parsing logic within the ETL service.

The benefits of such a system is that only ETL needs to change to accomodate new and changing requirements of old and new feeds
ensuring the final result is always consistent to march what the CDH service requires.


## Consequences

We must never implement custom, specific feed logic in the CDH service, such must always reside in ETL.

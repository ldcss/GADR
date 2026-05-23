# 508 Systems List as View of `system_intakes`

**User Story:** *[ES-255](https://jiraent.cms.gov/browse/ES-255)*

For the 508 workflows, individual testing engagements need to
refer to an existing "system" which will be the subject of the
testing. Within the EASi application the best source of data
outlining what these systems are live in the `system_intakes`
database table. The question to answer is how to expose data
that originally lives in the `system_intakes` table to the
508 workflow.

## Considered Alternatives

* Filtered View of `system_intakes` Table
* ETL (Extract/Transform/Load) Process to Stand-Alone Table

## Decision Outcome

Chosen Alternative: *Filtered View of `system_intakes` Table*

* Keeps the Systems List up-to-date with the latest
  information in the `system_intakes` table

Consequences:

* Slight maintenance overhead if the structure or contents
  of the `system_intakes` table changes over time
* Minimal to non-existent performance impact between the
  two strategies: both read a collection of items from the
  database; the `system_intakes` uses a slightly richer
  set of SQL filters for choosing the subset of data

## Pros and Cons of the Alternatives

### *ETL Process to Stand-Alone Table*

* `+` Mapping Systems List types to a stand-alone table would
  not change unless the backing table changed; this would mean
  the Systems List would be isolated from any changes to the
  `system_intakes` table
* `-` ETL process would mean the backing table was current
  only at point-in-time after an ETL run
* `-` Keeping ETL table up-to-date would require one of two
  approaches: human intervention to re-run ETL on some
  cadence; having the `SystemIntake` system push data to the
  Systems List, which is an inversion of the data dependency
  flow

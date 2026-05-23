# 8. Split out offender values to new table

Date: 2021-11-18

## Status

Accepted

## Context

Since the first version of the service, fields which are associated with a matched offender have been stored with the defendant record. This includes fields such as ```probationStatus```, ``CRN`` and ```suspendedSentenceOrder```.

It has become apparent that this has had several negative effects
* since we often have the same defendant appearing in multiple cases, there is a challenge to keep those offender-based fields consistent
* mixing of concepts around defendant and offender is confusing, a more natural model to adopt would be to have a separate ```Offender``` and have that as an optional relation to the ```Defendant```
* performance impacts 

## Decision

It has been decided to move the offender based fields from the Defendant to a new Offender entity at the level of the repository. This includes the following fields

* crn
* previouslyKnownTerminationDate
* suspendedSentenceOrder
* breach
* preSentenceActivity
* awaitingPsr
* probationStatus 

CRN will be unique in the Offender table. Ultimately, all of these fields will be removed from the Defendant, except for CRN which will remain to operate as the foreign key field.

Note that whilst PNC is related to an Offender, we will keep it in Defendant because it is sent in the LIBRA and Common Platform feeds and we need to keep the original value as it was supplied.

REST-based interfaces will not be altered to ensure that clients will not need to change. 

## Consequences

There is a risk that fetching of the optional Offender record might slow down the retrieval.

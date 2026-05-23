# Include Implementation Log as part of Decision Records

* Status: accepted
* Deciders: roleyfoley, rossMurr4y
* Date: 2021-01-19
* Implementation Log: https://github.com/hamlet-io/architectural-decision-log/issues/3

## Context and Problem Statement

When reviewing outstanding ADR records which haven't been accepted we noticed that there isn't anything in the record which allows you to see the implementation of a given decision. This makes it hard show progress towards in implementing a decision once it has been reached.

## Considered Options

* Use the status of the record and review records regularly
* Include a implementation log which needs to be created for each ADR

## Decision Outcome

Chosen option: "Include a implementation log which needs to be created for each ADR", because this allows for recorded ongoing progress of the the decision and maintains conversations around the decision through their implementation


### Positive Consequences

* We can clearly define an epic level work item to ensure that the decision is implemented
* It shows the reality of the records outcomes which is useful during reviews of the process
* We can reference the decision as part of other pieces of work

### Negative Consequences

* Additional work overhead when creating records
* Risk of losing the concrete nature of the records where the implementation log starts new conversations that are note reflected in the record or new records

## Pros and Cons of the Options

### Use the status of the record and review records regularly

This option is to essentially use the records as they are now but with a new status of `Implemented` which would be after the `Accepted` status. This would require someone to update the ADR with the status once they have implemented the record

* Good, because it doesn't require additional work in following a new log
* Good, because it aligns with the ADR process
* Bad, because it requires ongoing reviews and requires people to be aware of the records more deeply

### Include a implementation log which needs to be created for each ADR

In this option we would create an implementation log as a Github Ticket and reference this as part of the ADR. The Log would be created when the record reaches the `Accepted` status. The log would be assigned to a maintainer and any work which implements the record would be recorded in the log, using links from other issues or PR's. Once the log has been closed the record is considered implemented

* Good, because it assigns responsibility to a maintainer for the record
* Good, because it provides an easy to demonstrate tracking record of the work required to implement the record
* Good, because it will show real world usage of the record
* Bad, because it requires additional maintenance and adds a new step to the process
* Bad, because it may create augmentations to the record which aren't reflected in the record

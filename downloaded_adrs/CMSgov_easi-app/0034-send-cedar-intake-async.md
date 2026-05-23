# CEDAR Intake Asynchronous Approach

The current (at time of writing) approach for sending data to the CEDAR Intake API is to [call the CEDAR Intake client as a part of an action that a user takes](https://github.com/cms-enterprise/easi-app/blob/5df7edb258addd2e974d797523318b09a4b2e21b/pkg/server/routes.go#L267-L270). This works, but raises a few questions:

- Should a failed call to CEDAR result in an error being returned to the user? (It does at the time of writing)
- How do we handle if one of these calls to CEDAR fails?
- What actions should we modify to also send to CEDAR?

Some of these questions are not too hard to answer, while others (like error handling and retries) are a bit more difficult.

As part of regular discussions about CEDAR's Intake API, it was brought up that an "asynchronous"/"scheduled" approach to sending data to CEDAR (rather than one that's triggered by user action) might help solve a good number of these problems.

## Considered Alternatives

* Continue modifying user actions to send data to the CEDAR Intake API.
* Use an asynchronous "scheduled" approach to sending data to the CEDAR Intake API.

## Decision Outcome

* Chosen Alternative: Use an asynchronous "scheduled" approach to sending data to the CEDAR Intake API.

There's probably a few approaches that could be taken here, but the most generic approach would be to use the action scheduling mechanism outlined in [this ADR](./0033-technical-action-scheduling.md), to define a job that will either
* Scan our DB for entities that need to be sent to CEDAR, or to send a specific entity to CEDAR.
* Pull items off a "queue" that we populate with entities that need to be sent to CEDAR.

## Follow Up Decisions
* Should our scheduled job scan our DB, or pull of a "queue" that we populate? Which of these is easier to implement? Are there specific upsides to either approach?

## Pros and Cons of the Alternatives

#### Continue modifying user actions to send data to the CEDAR Intake API.
* `+` Don't have to introduce any new logic, just add a new step to the action we want to modify.
* `-` Still would have to build out some sort of (likely asynchronous) mechanism for handling errors anyways.

#### Use an asynchronous "scheduled" approach to sending data to the CEDAR Intake API.
* `+` Don't have to write separate error handling logic, as the nature of a scheduled job means that retries will happen automatically.
* `+` Don't have to modify any specific actions to send to CEDAR as part of that action, which would complicate testing of those actions. (This makes the actions have a "single responsibility" of saving data to EASi's DB)
* `-` Is reliant on the existence of an action scheduling mechanism, which (as of writing) doesn't exist yet.

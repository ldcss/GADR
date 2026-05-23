# DynamoDB update strategy

*   Status: accepted
*   Proposers: trestini
*   Deciders: trestini
*   Date: 2018-04-28

## Context and Problem Statement

In order to maintain the serverless nature of the project, a DynamoDB table was
chosen as main persistence mechanism, which means that a schedule is primarily
stored in DynamoDB and then distributed to other components, which in turn
goes back to DynamoDB to update state. So, DynamoDB holds both state and
historical data.

The problem here is that both ~~warmer~~ `task-1minute-enqueuer` and ~~poller~~ `task-1minute-sqs2sns` will concur by Dynamo resources and probably will be throttled (it's easy to reproduce this behavior only by setting Dynamo's read and write capacity to 1 and trying to send some hundreds of schedules while some other are ~~moving from *WARM* state~~ being enqueued in delayer queue).

## Decision Drivers

*   Solution must kept as simple as possible
*   Even it could delay the problem, increase read and write capacity of
DynamoDB is not an architectural solution

## Considered Options

*   Use an event driven approach for updates
*   Use separated persistence stores for state and historical data
*   Don't use state as a field in database

## Decision Outcome

Take the decision for the use of the DynamoDB introduced a new concept for the entire architecture: the layered concern.

The `delayer-aws` solution aims to provide a way to schedule future operations reliably. It's not part of this system store or ingest or even present information about these schedules. In this sense, the use of DynamoDB is needed only because there's a need of store schedules that could not be posted in delayer queue, and there's only 2 options for those records: or they are in the delayer queue, or they're not. That's why the "state" field is needed, but it will not hold the *entire* lifecycle of a schedule.

With this in mind, we realize that all 3 options will be considered, but in different contexts:

-   Present data of scheduler is not `delayer-aws`'s concern, but it will be needed. So all the data events should be published by `delayer-aws` to be consumed by another "view" platform - this is a kind of *event driven approach*.
-   In this sense, if another system will ingest all of this published data, state and historical data will be stored in different persistent stores;


### How it should work

When a schedule is inserted, if their timeframe was greater then the timeframe of the delayer queue, the schedule is stored in DynamoDB with a *currentStatus* marked as `NEW` and a TTL of 1 hour after schedule time.
When `task-1minute-enqueuer` runs and finds this scheduler, it will be updated to `PROCESSED`. After that, no more updates are made in DynamoDB.

For each event that occurs with this schedule, a message should be posted in the correspondent topic. 

### Don't use state as a field in database

The state of a schedule is noted by currentStatus/currentState attribute in
DynamoDB. The proposal of this optional is to treat state as part of the
general flow of application:

1.  When scheduled, it's COLD
1.  When *warmer* puts it on SQS, it's WARM
1.  When *poller* publishes it on SNS is DOING
1.  When *actions* execute

*   Good, simplified update policy
*   Good, reduced DynamoDB costs
*   Bad, no information about past events

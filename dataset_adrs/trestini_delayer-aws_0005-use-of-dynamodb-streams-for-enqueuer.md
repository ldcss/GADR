# Use of DynamoDB streams for *enqueuer*

*   Status: accepted - partially superseeds [ADR-0003]
*   Proposers: trestini
*   Deciders: trestini
*   Date: 2018-05-16

## Context and Problem Statement

The [ADR-0003] states that the main purpose of DynamoDB is not hold historical data and must only be used as state holder while the particular schedule is not ready to be in the delayer queue. However, the state will be changed from *NEW* to *PROCESSED* exactly when this schedule is posted in the delayer queue. This proposal aims change this behavior, removing the records that are already in delayer queue instead change it to *PROCESSED*.

## Decision Drivers

*   Cost: to be able to deal with thousands of schedules, the only way is to increase provisioned capacity of DynamoDB. Do it of hundreds of thousands, or even millions of records is acceptable, but not for few thousands.

## Considered Options

*   Move for a solution based on TTL and Dynamo Streams

## Pros and Cons of the Options

### Move for a solution based on TTL and Dynamo Streams

*   Good, increases performance and reduces cost
*   Bad, adds complexity and some not-so-obvious solutions

## Decision Outcome

Chosen option was to move to a solution based on Dynamo Streams. The proposed solution doesn't use TTL, since according [AWS docs](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/howitworks-ttl.html), the deletion of a expired record should occurs within 48 hours - which, for this case, is not acceptable.

The solution is based in the fact that records generates events in DynamoDB that can be consumed by lambda functions. In this sense, when a new schedule is deleted, a DELETE event is raised, and the function will schedule it for the proper pointInTime. In other hand, when a schedule is placed within the delayer period (the timeframe that events are waiting in the delayer queue), this function deletes this record which generates another DELETE that will be handled. If the schedule is not in the delayer period, it will be stored until the *task-1minute-enqueuer* finds it and then deletes the record.

Hey, but why *api-schedule-post* don't simply put this in que delayer queue directly?

The short answer is: because each lambda should do 0, 1 or tops 2 data transformation. 

Each lambda should be very restrict on what it does. *api-schedule-post* is the function responsible to handle the POST request from API Gateway. Handle and transform the data and store it somewhere is the "reason to exists" of this function. How this information is processed later, is not it's concern.

Have in mind that in this stage of development, keep the integrity of the design is more important that this fine performance tunning.

Below, the new roles of the involved lambdas:

*   *task-1minute-enqueuer* - this function still be triggered by the cloudwatch events and simply deletes the records that entered in the delayer period.
*   *stream-dynamodb-fasttrack_enqueuer* - send the records that are raised in DELETE event to the SQS queue. If the event is an INSERT and it will be in the delayer period, it deletes the record.

Positive Consequences:
*   Keeps the entire architecture design more *push based*, which is very important for a serverless architecture style.
*   Keeps the integrity of the flow: only 1 lambda sends records do sqs, only 1 lambda inserts records in the dynamodb, the event the pushes records to sqs is always the same.

Negative consequences:
*   Still keeps the increased writes in DynamoDB (each delete in Dynamo counts as a write operation)

## Links

*   Refers to [ADR-0003](0003-dymamodb-update-strategy.md)

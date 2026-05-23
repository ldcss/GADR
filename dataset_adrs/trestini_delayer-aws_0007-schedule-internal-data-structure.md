# Schedule internal data structure

*   Status: accepted
*   Proposers: trestini
*   Deciders: trestini
*   Date: 2018-06-10

## Context and Problem Statement

Define a default data structure for the schedule information within interal structures of delayer-aws. The outside schedule model was already defined.

## Decision Drivers

*   Structure is an internal representation, and format should be concerned with it's interal functionalityes
*   Could be used in future event dispatchers

## Decision Outcome

The json structure of the schedule will be:

```javascript
{
  scheduleId: "484a127d-6ce3-11e8-8fdd-fb8b5aab61ea",
  pointInTime: 1528662600,
  apiKey: "nVMIr6J5Do1qutXsZt1dhaaJfjyq4YgzThPQWkQ1",
  topicArn: "arn:aws:sns:us-east-1:472249637553:http-request_action-topic",
  actionConfig: '{ "method" : "GET", "url" : "https://google.com/" }',
  context: '{ "headers" : [], "payload": "" }'
}
```

Where:

*   `scheduleId`: unique identifier of the schedule - generated
*   `pointInTime`: unix timestamp created in UTC basis to the exact time of the execution of the schedule - informed by the client in request body
*   `apiKey`: if informed, the client's api key - informed by the client in headers
*   `topicArn`: the Amazon Resource identifier of the action topic on where the schedule will be published. If only the topic name was provided, the current account and the region of the *api-schedule-post* currently in execution will be used to build the arn.
*   `actionConfig`: config object provided by the user based on the type of the action
*   `context`: the data that will be used as context in the actions

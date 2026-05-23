# Recursive lambda or CloudWatch-triggered lambda

*   Status: accepted
*   Proposers: trestini
*   Deciders: trestini
*   Date: 2018-04-28

## Context and Problem Statement

~~In the WARM stage~~ When a schedule is in the delayer queue, messages become visible after delayed period. However, those messages must be published in corresponding *action topic*, and it cannot be done automatically, being needed to use a lambda function to do this publishing.

## Decision Drivers

*   This project is a scheduler, so the latency is an important concern
*   Flexibility: ability to be good enough in high or low concurrent executions

## Considered Options

*   Recursive lambdas
*   Cloudwatch-triggered lambda

## Decision Outcome

Chosen option was to "Cloudwatch-triggered lambda".

Chaining lambda functions is a good solution when the volume of messages is flat or well known. In a scenario of a variable/high-volume of messages, the function would introduce some latency, due to the lack of paralelism of execution. To achieve paralelism, the solution would become much more complicated.

The chosen solution introduces the folowing concepts:
-   lambda function timeout: configured time on when a function will be forcibly stopped by it's container
-   lambda execution baseline: amount of time that a lambda function should be ideally working
-   cloudwatch event timer: amount of time on cloudwatch event will call lambda function

The execution baseline and the event timer should have the same values, and timeout should be greater. Function starts executing and during the execution baseline, it waits for messages. If no messages arrives when this time finishes, the function stops itself. However, if there's more messages waiting in the queue, the function keeps consuming messages until 1. there's no more messages, 2. reach the function timeout. Whilst, the function will keep running and as new function are spawned by CW events, those function will run in parallel.

```
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----| <- CW events

|-----------------------------| <- function timeout

|-----| <- function baseline
```

**Example of how it would work**

```
|-----| <- function - instance 1
      |-----| <- function - instance 2
            |-----| <- function - instance 3

************************ received a bunch of messages - parallel

|-----------------------------| <- function - instance 4
      |-----------------------------| <- function - instance 5
            |-----------------------------| <- function - instance 6
                  |-----------------------------| <- function - instance 7
```

Positive Consequences:
*   Enable parallelism and, for instance, reduces latency. This is very important for a scheduler

Negative consequences:
*   More effort in develop and maintain this lambda function

## Pros and Cons of the Options

### Recursive lambdas

In this case, lambdas do their jobs and at the end, they call recursivelly the
same function.

*   Good, by the simplicity
*   Bad, an error could stop the chain of calls
*   Bad, can introduce latency

### CloudWatch-triggered lambdas

In this case, each lambda keep doing their jobs until some time before their
configured timeouts while CloudWatch triggers new executions in some intervals.

*   Good, provide reduced latency due to concurrency capability of lambdas
*   Bad, complicated.

## Links

*   https://github.com/serverless/examples/blob/master/aws-node-recursive-function/handler.js
*   https://theburningmonk.com/2017/08/write-recursive-aws-lambda-functions-the-right-way/

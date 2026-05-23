# 3. Data will be stored and treated independent from triggers

Date: 2020-05-17

## Status

Accepted

## Context

There are a number of independent microservices as part of the Mercury Platform and each one of them needs to operate with our data in one way or another.

## Decision

In order to maximize reusability of the data and to make triggers as generic and lightweight as possible, data will be stored completely separately from other services and will not act as a data flow trigger in any way.

## Consequences

By not using the data itself as part of a trigger, it opens the system to reference issues.

If service A references data that for whatever reason service B cannot find, we will run into runtime errors.

The alternative of using the data itself as part of the trigger gives us more certainty that each successive service will have what it needs, but reduces the ability to cache and reuse data effectively as well as spiking storage utilization.


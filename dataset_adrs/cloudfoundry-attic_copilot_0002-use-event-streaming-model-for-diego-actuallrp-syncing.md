# 2. Use event streaming model for diego ActualLRP syncing

Date: 2018-07-25

## Status

Accepted

## Context

The diego ActualLRP syncing model as currently implemented will fetch all LRPs
across all diego cells at a specified time interval (at the time of writing 10
seconds). As the ActualLRP count grows on a cloudfoundry deployment this could
impact the performance of the BBS (large response sets coming back).

## Decision

We want to use the [Event package](https://github.com/cloudfoundry/bbs/blob/master/doc/events.md)
to get the event stream for each ActualLRP. We will also use a bulk sync every
60 seconds to catch any events that were missed.

## Consequences

- There should be an immediate reduction in the amount of ActualLRP data coming
  from diego in each sync event.
- Functionally, there should be no difference in the amount of time it takes for
  diego ActualLRP data to make its way into copilot.
- This means we need to store our diegoProcessGUID to BackendSet mapping
  in memory so that we can update it each time an event comes in.


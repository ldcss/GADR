# 4. event contracts

Date: 2018-05-26

## Status

Accepted

## Context

When returning to development after a break and needing to create events in integration tests it was difficult to identify and construct events.

Also, producers that only produce one event type were still able to set an event type so the event contract was very weak.

## Decision

All events will be in a file with a name formatted `eventType.event.js` where the event type is in past tense and is duplicated in a property of the event with key `type`.

The JS module exported by that file will be one or more functions that return the event

E.g. `decisionMade.event.js` would export a function that takes a decision and returns

```
{
  type: "decisionMade",
  decision: "the provided decision"
}
```

## Consequences

This makes event creation less flexible but more discoverable.

Further development might lead to a decision that supercedes this one as it has been made in the context of fewer than five events in the domain.

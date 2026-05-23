# Post launched active missile status updates directly from MGCC via SignalR

* Status: [accepted]
* Deciders: [[@kakarotto67](https://github.com/kakarotto67)]
* Date: [2019-09-17]

Technical Story: [Create Missile Guidance Controller Chip](https://github.com/kakarotto67/mlmc/issues/15)

## Context and Problem Statement

There is a need to send real time SignalR-based notifications about current missile position to the map.

## Decision Drivers

* Need easy way to post missile status updates
* Need easy way to get those updates using SignalR on client side

## Considered Options

* Use MGCC->Message Bus->Handler->CosmosDB->Function trigger->SignalR flow
* Use MGCC->SignalR flow

## Decision Outcome

Decided to simply push SignalR messages directly from MGCC module.

### Positive Consequences

* Initially I planned to post current missile status to Message Bus, then process it to CosmosDB, then have Azure Function to send SignalR messages. But that seemed too complicated. With direct SignalR messages from MGCC module the implementation will be much easier and faster.

### Negative Consequences

* n/a

## Links

* n/a

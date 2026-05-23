# [ADR-002] Implementation of Client-Side Prediction and Server Reconciliation

**Date:** 2026-05-22

## Status
Accepted

## Context
We are developing a 10v10 competitive online FPS. Network latency (ping) and packet loss inherently delay the transmission of player inputs to the server and the resulting game state back to the client. Relying on a purely synchronous model where the client waits for server confirmation before rendering actions causes visible input lag, degrading the player experience. 

Simultaneously, the game requires strict server authority to prevent cheating and reliably resolve interactions between players. The game engine must handle asynchronous communication rapidly while ensuring all clients eventually share a synchronized, valid state. 

## Considered Options
* **Strict Server Authority (No Prediction):** The client sends inputs and waits for server confirmation before updating the local simulation. *Rejected:* Causes intolerable input delay proportional to the player's latency, making fast-paced FPS gameplay impossible.
* **Peer-to-Peer Lockstep:** Clients share inputs and wait for all peers before advancing the simulation tick. *Rejected:* Does not scale well for 20 players, exposes IP addresses, and allows the slowest connection to lag the entire match.

## Decision
The game will implement **client-side prediction** paired with **server reconciliation**. 

* **Client-Side Prediction:** The client will immediately process local inputs and render the predicted game state without waiting for server confirmation. Inputs will be simultaneously dispatched to the server via UDP.
* **Server Authority:** The server remains the single source of truth, executing the same inputs and calculating the authoritative state.
* **Reconciliation:** The client will maintain a buffer of historical states and unprocessed inputs (tracked via incrementing tick IDs). When the client receives the authoritative state from the server, it will compare it against the historical local state. If they diverge, the client will roll back to the server's state and rapidly replay any pending local inputs to correct the present state.
* **Shared Logic:** Game simulation logic must be highly deterministic and shared identically between the client and server codebases to minimize prediction errors.

## Consequences

**Positive:**
* Eliminates perceived input lag for local movement and actions.
* Retains absolute server authority, effectively preventing movement hacks and unauthorized state manipulation.
* Masks minor packet loss and network jitter via smooth local simulation.

**Negative:**
* Significantly increases architectural complexity; requires strict determinism and shared simulation code between client and server.
* Higher memory usage on the client due to the necessity of storing circular buffers for historical inputs and states.
* Players experiencing extreme latency or severe packet loss will experience "rubber-banding" (visual snapping) when the client is forced to execute large state rollbacks.
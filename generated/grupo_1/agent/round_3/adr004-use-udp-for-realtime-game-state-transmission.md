# [ADR-004] Use UDP for Real-Time Game State Transmission

**Date:** 2026-05-22

## Status
Accepted

## Context
We are developing a competitive 10v10 online FPS requiring high-frequency, real-time game state synchronization. The architecture relies heavily on asynchronous communication patterns, client-side prediction, server reconciliation, and lag compensation. Maintaining ultra-low latency is critical to prevent visible stuttering or character freezing. We must choose a transport protocol for sending data packets that prioritizes immediate state updates over strict delivery guarantees. 

## Decision
We will use UDP (User Datagram Protocol) as the transport protocol for transmitting real-time game data packets to prioritize transmission speed over guaranteed delivery.

## Considered Options
* **UDP (User Datagram Protocol):** Selected. Connectionless protocol that avoids sequence tracking and handshakes, resulting in the lowest possible latency for time-sensitive state updates.
* **TCP (Transmission Control Protocol):** Rejected. While it guarantees ordered delivery, the connection-oriented handshake and mandatory round-trip acknowledgments introduce severe latency bottlenecks (head-of-line blocking) during packet loss, rendering it unacceptable for fast-paced FPS mechanics.

## Consequences

**Positive:**
* **Low Latency:** Removes connection overhead and round-trip confirmations, maximizing throughput.
* **No Blocking:** Packet loss does not halt the processing of newer, incoming game state packets.
* **Optimal for FPS:** Perfectly supports our use of client-side prediction and server reconciliation by ensuring the client always has the most recent data available as fast as possible.

**Negative:**
* **No Guaranteed Delivery:** Dropped packets are permanently lost without automatic retransmission mechanisms.
* **Unordered Arrival:** Packets may arrive out of sequence. 
* **Increased Application Complexity:** The game engine must be explicitly programmed to handle packet loss, interpolate missing data, and discard outdated, out-of-order packets.
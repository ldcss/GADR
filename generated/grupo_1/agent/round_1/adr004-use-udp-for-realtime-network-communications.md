# [ADR-004] Use UDP for Real-Time Network Communications

**Date:** 2026-05-11

## Status
Accepted

## Context
We are developing an online competitive 10v10 First-Person Shooter (FPS) game. In this environment, low latency and high responsiveness are critical for features like client-side prediction, lag compensation, and server reconciliation. The game state changes rapidly (e.g., hitscan tracking, projectile simulation, and player movement). Relying on a protocol with connection management overhead, guaranteed delivery, and packet ordering would introduce head-of-line blocking and visible lag during packet loss, severely degrading the player experience. Additionally, the network architecture must scale efficiently to support at least 500 concurrent connections and 5000+ Daily Active Users (DAU). 

## Decision
We will use the User Datagram Protocol (UDP) implemented via socket-based connections for all real-time, time-sensitive in-game network communications. 

## Considered Options
*   **TCP (Transmission Control Protocol):** Rejected. While it guarantees delivery and ordering, the connection overhead, handshakes, and automatic packet retries cause unacceptable latency spikes and head-of-line blocking, rendering it unviable for a fast-paced competitive FPS.
*   **WebSockets (over TCP):** Rejected. Offers persistent bidirectional communication but inherits TCP's reliable delivery drawbacks, resulting in the same latency issues when packets are dropped.

## Consequences

**Pros:**
*   **Maximum Performance:** Connectionless, datagram-oriented transmission omits handshake and retry overhead, delivering optimal speed for time-sensitive data.
*   **High Scalability:** Foregoing reliable messaging allows the system to easily support high capacity limits (500+ concurrent connections and 5000+ DAU).
*   **No Head-of-Line Blocking:** Dropped packets will not delay the processing of subsequent, more recent state updates.

**Cons:**
*   **No Delivery Guarantees:** UDP inherently lacks delivery and ordering guarantees. Packet loss will occur.
*   **Increased Application Complexity:** The game engine/application layer must handle missing or out-of-order data using techniques like entity interpolation, client-side prediction, and server snapshots.
*   **Unsuitable for Reliable Actions:** Critical data, such as marketplace transactions or persistent account updates, cannot use this UDP channel and will require a separate, reliable HTTP/TCP service.
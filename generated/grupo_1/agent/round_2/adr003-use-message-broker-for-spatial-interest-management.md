# [ADR-003] Use Message Broker for Spatial Interest Management

**Date:** 2026-05-22

## Status
Accepted

## Context
In our 10v10 competitive FPS architecture, broadcasting all game state and event data to every client causes unnecessary network traffic and degrades performance. For example, a client does not need network updates regarding a confrontation happening 2km away on the map. To optimize bandwidth and client-side processing, the system requires an "Interest Management" mechanism to filter and route spatial updates so clients only receive data relevant to their immediate field of view or proximity. 

## Decision
We will implement an external message broker to handle interest management and asynchronous event routing. The broker will filter data streams based on spatial parameters, restricting network updates so clients only receive positional data, events, and entity actions occurring within their immediate proximity (e.g., a 1km radius).

## Considered Options
*   **External Message Broker (Chosen):** Provides robust built-in routing, topic configurations, and asynchronous consumption necessary for filtering spatial proximity updates across distributed nodes. 
*   **In-Memory Pub/Sub (Rejected):** While possessing lower latency, it lacks advanced routing and filtering configurations. Using this would require custom-building complex spatial filtering middleware that external brokers already provide.
*   **Direct Synchronous MVC/HTTP (Rejected):** Synchronous, blocking calls would severely bottleneck the game loop. Unfit for the high-frequency asynchronous streaming (UDP-based) required in an FPS environment.

## Consequences

**Pros:**
*   **Bandwidth Optimization:** Eliminates the transmission of large payloads (e.g., 70kb event logs) for distant, irrelevant actions, significantly reducing network saturation.
*   **Non-Blocking Performance:** Broker libraries offer asynchronous, non-blocking consumption, allowing spatial proximity events to be dispatched without interrupting the main game loop.
*   **Advanced Routing & Reliability:** Provides built-in capabilities for complex message routing, prevents duplicate messages (reducing unnecessary I/O operations), and maintains plausible message ordering.
*   **Scalability:** Acts as a reliable cornerstone for scaling the distributed architecture across multiple geographic server nodes.

**Cons:**
*   **Network Overhead:** Introduces a new network hop and communication overhead between the game servers and the external broker.
*   **Complexity:** Increases architectural complexity and infrastructure deployment effort compared to a centralized, in-memory state manager.
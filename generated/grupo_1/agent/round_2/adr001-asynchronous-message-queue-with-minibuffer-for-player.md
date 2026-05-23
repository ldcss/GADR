# [ADR-001] Asynchronous Message Queue with Mini-Buffer for Player State Synchronization

**Date:** 2026-05-22

## Status
Accepted

## Context
We are developing a 10v10 online competitive FPS game. Handling high-frequency player inputs and state updates across 20 distributed nodes requires a highly performant and fault-tolerant network architecture. True synchronous network calls block the client and are highly susceptible to network latency, packet loss, or server crashes, making them unviable for real-time multiplayer gaming. However, players require an experience that *feels* synchronous and instantaneous. We must establish a centralized server authority (Observer) to validate match data while masking network latency from the client.

## Decision
The server architecture will utilize an asynchronous UDP data stream routed through a message queue, paired with a mini-buffer to collect and sequence player data. 

The message queue will act as an asynchronous broker to handle incoming player inputs without blocking clients. The mini-buffer will allow the server to reconstruct messages in chronological order before processing game state. To simulate a synchronous experience, the architecture will rely on client-side prediction (simulating actions locally immediately) and server reconciliation (correcting the client state based on the asynchronous queue's processed result). 

## Considered Options
* **Pure Synchronous Architecture (Direct RPC/TCP):** Rejected. Blocking the client to wait for a server response introduces noticeable lag and freezes the game during network spikes or packet drops.
* **Pure Asynchronous without a Buffer:** Rejected. Relying on raw UDP streams without a sequencing buffer leads to out-of-order execution, causing state desynchronization and inaccurate hit registration.
* **Asynchronous Message Queue with Mini-Buffer (Chosen):** Provides the non-blocking benefits of async communication while the mini-buffer guarantees ordered reconstruction of data for accurate server-side simulation.

## Consequences

**Pros:**
* **Unblocked Clients:** Asynchronous brokering allows clients to process inputs immediately using client-side prediction, hiding actual network latency.
* **Optimized Server Performance:** Message queues optimize server I/O by batching events, preventing duplicate handler calls, and decoupling payload access.
* **Accurate State Reconstruction:** The mini-buffer enables the chronological ordering of asynchronous inputs, which is critical for lag compensation and hit validation.

**Cons:**
* **Increased Architectural Complexity:** Implementing event queues, server reconciliation, and lag compensation (rewinding state) significantly increases the codebase complexity compared to a standard request-response model.
* **New Points of Failure:** The message broker introduces a new potential failure point. Clear data flow diagrams and robust tracing mechanisms will be required to debug delayed or dropped messages.
* **Visual Artifacts:** High latency will result in visible "rubber-banding" when the server ultimately rejects and corrects a client's predicted local state.
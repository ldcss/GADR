# [ADR-001] Implementation of Event Broker for Asynchronous Server Messaging

**Date:** 2026-05-11

## Status
Accepted

## Context
We are developing a 10v10 competitive online FPS game requiring high-frequency state updates and low latency. The server must process continuous data streams from players, calculate game states, and broadcast updates. Synchronous server-side communication causes structural tight coupling and blocks operations, increasing perceived lag. Furthermore, broadcasting all state changes to all players wastes bandwidth and processing power; we need "interest management" (e.g., occlusion culling or proximity-based routing) to send data only to relevant, nearby players. Simple in-memory pub/sub mechanisms lack the advanced routing, durability, and integration capabilities required for this scale.

## Decision
We will implement an external Event Broker and Messaging Architecture on the server-side to handle asynchronous event streaming and message queuing. 

We will expose an event-publishing abstraction over a dedicated third-party pub/sub framework (e.g., RabbitMQ or Kafka) to route game events. The broker will utilize specific routing patterns (such as topic or direct exchanges) to manage interest management, ensuring players only receive data updates relevant to their in-game proximity.

## Considered Options
*   **Pure Synchronous APIs (Pure MVC via HTTP/RPC):** Rejected. Direct synchronous calls create brittle inter-modular coupling, block server threads, and are inadequate for real-time, continuous data streams in an FPS environment.
*   **In-Memory Publish/Subscribe:** Rejected. While simpler to deploy, it lacks message durability, guaranteed delivery, and out-of-the-box advanced routing capabilities necessary for proximity-based interest management.

## Consequences

**Positive:**
*   **Interest Management:** Leveraging broker routing patterns natively supports distributing relevant state data based on player proximity, reducing client/server payload.
*   **Decoupling:** Asynchronous message passing effectively replaces direct synchronous calls, improving server-side modularity and resilience.
*   **Durability and Fault Tolerance:** External brokers provide message persistence (e.g., Kafka retaining messages for days) and advanced failure handling, enabling recovery without data loss if a microservice crashes.
*   **Flexibility:** Abstracting the broker allows iterative adoption of advanced streaming features without refactoring core game logic.

**Negative:**
*   **Increased Complexity:** Introduces infrastructure overhead, requiring external dependency deployment, orchestration, and maintenance.
*   **Ordering Constraints:** Message queuing introduces technical difficulties regarding strict message ordering, especially when dealing with processing failures and re-queued messages. 
*   **Debugging:** Tracing asynchronous events across multiple decoupled services is fundamentally harder than tracing synchronous call stacks.
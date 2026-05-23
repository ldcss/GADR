# [ADR-003] Message Broker for Game State Interest Management

**Date:** 2026-05-22

## Status
Accepted

## Context
We are developing a 10v10 competitive online FPS. Broadcasting the global game state to all 20 clients generates excessive network overhead and forces clients to process irrelevant data (e.g., combat events occurring 2km away on the map). To optimize bandwidth and client-side performance, we require an "interest management" mechanism that restricts data broadcast based on in-game proximity. Additionally, the fast-paced asynchronous architecture requires robust message ordering, concurrency control, and connection management to ensure accurate state synchronization (e.g., lag compensation, client-side prediction).

## Decision
We will implement an external Message Broker for interest management to filter and route game state data. The broker will restrict the broadcast of state updates to clients strictly based on in-game spatial proximity and relevance.

## Considered Options
* **External Message Broker (Selected):** Provides advanced integration, rich configuration for complex proximity filtering (topic/routing-key based), and built-in connection management (heartbeats). It abstracts the routing layer and supports non-blocking message consumption.
* **In-Memory Publish/Subscribe (Rejected):** Eliminates inter-process network latency and is simpler to stand up initially. However, it lacks out-of-the-box advanced routing features, meaning complex interest management, concurrency controls, and reliable message ordering would require heavy custom implementation.

## Consequences

**Positive:**
* **Bandwidth Optimization:** Players only receive state data relevant to their immediate vicinity, drastically reducing payload sizes and network congestion.
* **System Decoupling:** Abstracts the routing layer; new game events or job types can be added without altering the core server architecture or underlying storage.
* **Reliability & Synchronization:** Prevents duplicate message dispatching and guarantees plausible message ordering, which is critical for accurate asynchronous game state reconciliation.
* **Concurrency:** Dedicated broker libraries allow for non-blocking message consumption and efficient signal dispatching to parallel workers.

**Negative:**
* **Architectural Complexity:** Introduces a new infrastructural dependency that requires configuration, hosting, and monitoring.
* **Latency Overhead:** Adds internal network communication latency (server-to-broker) compared to a pure single-process in-memory solution.
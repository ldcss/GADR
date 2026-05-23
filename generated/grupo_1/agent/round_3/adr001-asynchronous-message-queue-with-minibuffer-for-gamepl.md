# [ADR-001] Asynchronous Message Queue with Mini-Buffer for Gameplay Input Processing

**Date:** 2026-05-22

## Status
Accepted

## Context
We are developing a 10v10 competitive online FPS. Real-time multiplayer architecture requires a balance between authoritative server state and low-latency client responsiveness. A purely synchronous architecture introduces blocking operations that cause visible lag and state locks during network instability. To support client-side prediction, lag compensation, and UDP-based data streaming, we must process high-frequency input events without stalling the game loop.

## Decision
The server architecture will utilize an asynchronous message queue combined with a mini-buffer to collect and process player inputs. 

The message queue will act as an asynchronous broker to receive the data stream from all connected client nodes. The mini-buffer will then collect these messages over a brief window (tick) to reconstruct the plausible sequential order of events, effectively simulating a synchronous gameplay execution step.

## Considered Options
1. **Strict Synchronous Execution (RPC):** Rejected. Mandating a synchronous call for every input creates blocking bottlenecks. Network latency or dropped packets would halt the server simulation, causing unplayable client freezing.
2. **Direct State Mutation (No Queue):** Rejected. Processing events the exact millisecond they arrive via multiple threads introduces severe race conditions and prevents reliable lag compensation or deterministic rollback. 

## Consequences

**Positive:**
* **Non-Blocking Performance Gains:** Asynchronous processing ensures clients do not wait on HTTP/RPC request resolutions. The queue acts as a broker, preventing blocking and keeping response times instantaneous.
* **Reconstruction of Execution Order:** Emptying the asynchronous queue into the mini-buffer allows the engine to sort and reconstruct player inputs into a plausible, sequential order required for simulating synchronous gameplay.
* **Decoupling and Extensibility:** Abstracting the communication layer reduces duplicate messages (optimizing I/O) and enables the seamless addition of new input/job types without modifying the underlying storage mechanics.

**Negative:**
* **Concurrency Management Overhead:** Safely managing read/write access to the event queues and mini-buffer across multiple threads introduces significant complexity. Strict locking or lock-free concurrent data structures are required to avoid race conditions.
* **Increased Points of Failure:** Routing data through an initial queue and then into a secondary mini-buffer creates intermediary failure points. This necessitates advanced debugging telemetry, distinct message IDs, and precise data flow mapping to trace dropped inputs.
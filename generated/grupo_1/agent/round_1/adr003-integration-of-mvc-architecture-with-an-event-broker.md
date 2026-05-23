# [ADR-003] Integration of MVC Architecture with an Event Broker

**Date:** 2026-05-11

## Status
Accepted

## Context
We are developing a 10v10 competitive online FPS game. The system must process high-frequency player inputs, manage complex game states (hitscan, simulated projectiles), and handle network volatility using client-side prediction, server reconciliation, and lag compensation. To support fast, non-blocking asynchronous communication (via UDP and server message queues) while maintaining code maintainability, we require a foundational architecture that enforces strict component boundaries but can efficiently distribute rapid state changes (e.g., interest management/culling) across the application. 

## Decision
The Model-View-Controller (MVC) architectural pattern will be utilized as the core project structure, integrated with an Event Broker (Publish/Subscribe pattern). The MVC structure will isolate the shared models and state-changing services from the UI and controllers. The embedded Event Broker will manage asynchronous internal communication, utilizing defined interfaces, callbacks, and dispatch queues to orchestrate events across the decoupled MVC components.

## Considered Options
* **Standard MVC (pure HTTP/direct calls without Broker):** Rejected. Cannot reliably handle the high-throughput, asynchronous messaging required for a multiplayer FPS. Direct coupling would lead to blocking calls and potential loss of rapid player inputs during network latency or service dips.
* **Pure Event-Driven Architecture (without MVC):** Rejected. While highly decoupled, lacking the strict structural boundaries of MVC makes user interface and state management complex, hindering parallel development of client-side components.

## Consequences

**Pros:**
* **Separation of Concerns:** Enforces strict architectural boundaries between data management (Model), user interface (View), and business logic/routing (Controller).
* **Parallel Development:** Structural decoupling natively supports rapid, concurrent development across UI, core mechanics, and networking teams.
* **Component Isolation & Autonomy:** Application layers remain isolated. The Event Broker allows modules to react to state changes without direct dependencies.
* **Robust Async Processing:** The Broker's message queue efficiently buffers rapid inputs, masking latency and supporting pseudo-synchronous gameplay features (e.g., buffering inputs for server reconciliation).

**Cons:**
* **Middleware Coupling:** The system becomes heavily reliant on the Event Broker middleware for internal communication.
* **Eventual Consistency:** The asynchronous pub/sub model introduces eventual consistency, requiring careful orchestration for precise game-state synchronization.
* **Strict Contract Requirements:** Demands highly stable and standardized event payload structures to prevent unhandled errors within the dispatch queues.
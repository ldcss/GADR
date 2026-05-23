# [ADR-002] Adopt Event-Driven Architecture with Asynchronous Message Broker

**Date:** 2026-05-22

## Status
Accepted

## Context
The system is an agency architecture focused on real-time logistics optimization and urban mobility. It requires the orchestration of specialized, co-dependent agents (e.g., traffic, cost, weather) to validate route feasibility in real-time and automatically recalculate suggestions upon detecting environmental changes. The system must process simulated high-frequency data asynchronously, demanding an architecture that supports high scalability, independent processing, and decoupled interactions between data producers and consumer agents. 

## Decision
We will adopt an Event-Driven Architecture (EDA) utilizing an asynchronous message queue and a central event broker. The architecture will implement the Publish/Subscribe pattern: 
*   **Producers** (e.g., simulated Python scripts) will publish localized events (traffic updates, weather changes) to the central event bus.
*   **Consumers** (specialized agents) will subscribe only to the data streams relevant to their domain to process the data independently and asynchronously.

## Considered Options
*   **Pipes and Filters:** Initially discussed but rejected. While useful for linear data transformations, it lacks the multi-directional flexibility and asynchronous routing capabilities required for complex, co-dependent agent orchestration.
*   **Synchronous API Facade (Direct REST/RPC):** Rejected. Direct synchronous communication between agents introduces tight coupling, reduces scalability, and makes real-time, resilient recalculations difficult under continuous simulated data streams.

## Consequences

**Positive:**
*   **Scalability & Resilience:** Asynchronous Pub/Sub routing allows agents to process data independently, preventing bottlenecks during high-volume event bursts.
*   **Component Decoupling:** Strict separation between producers, the message broker, and consumers decentralizes responsibilities, enabling high module and team autonomy.

**Negative / Risks:**
*   **Broker Coupling:** The architecture introduces a direct dependency on the specific message broker/middleware chosen.
*   **Eventual Consistency:** The asynchronous nature of the queues necessitates robust handling of eventual consistency across module integrations.
*   **Contract Rigidity:** Events will serve as the "Published Language" between Bounded Contexts, requiring event data structures (contracts) to remain highly stable to avoid breaking consumer agents.
# [ADR-002] Adopt Event-Driven Architecture with Message Broker for Agent Coordination

**Date:** 2026-05-22

## Status
Accepted

## Context
The system must orchestrate co-dependent, specialized agents (e.g., traffic, cost, weather) to perform real-time urban mobility and logistics optimization. The architecture must continuously process dynamic variables (e.g., accidents, weather changes, subway delays) and autonomously calculate optimal routes based on configurable criteria (time, cost, carbon footprint). The solution requires high scalability and the ability to dynamically react to asynchronous external events without stalling the decision-making process. 

## Decision
The system will be built using an asynchronous, event-driven architecture centered around a message broker (message queue). 
*   **Producers:** A service (initially a Python simulation script) will publish environmental state changes (e.g., weather updates, traffic conditions) as discrete events to the broker.
*   **Consumers:** Specialized agents will act as autonomous workers, subscribing only to topics relevant to their domain expertise.
*   **Data Flow:** Agents will process arriving data asynchronously, validate route viability, and publish their intermediate calculations back to the broker for downstream agents to consume.

## Considered Options
1.  **Pipes and Filters Pattern:** Rejected. While initially considered, a sequential pipeline imposes a rigid execution order. This inherently conflicts with the need for dynamic, real-time recalculations where independent agents must react concurrently to unpredictable external variables.
2.  **Synchronous Request-Response (REST/RPC):** Rejected. Point-to-point synchronous communication between agents introduces tight coupling and blocking dependencies, significantly degrading scalability and fault tolerance during system-wide decision making.

## Consequences

**Pros:**
*   **Component Decoupling & Concurrency:** Replaces synchronous chaining with asynchronous communication, granting agents autonomy to operate, scale, and process domain-specific data concurrently.
*   **Scalability & Responsiveness:** Perfectly maps to the dynamic nature of real-time route optimization, allowing the system to handle bursts of environmental events efficiently.

**Cons/Risks:**
*   **Middleware Coupling:** While individual agent modules achieve autonomy, the system introduces a hard dependency and single point of failure/bottleneck on the message broker infrastructure.
*   **Eventual Consistency:** Inter-modular communication via asynchronous message passing means the overall route recommendation state will inherently be eventually consistent.
*   **Strict Published Language:** The event payload schemas become the system's explicit "Published Language." Changes to these event structures will require careful versioning to avoid breaking subscribed agents.
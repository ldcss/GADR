# [ADR-002] Adopt Event-Driven Architecture with Central Message Broker

**Date:** 2026-05-11

## Status
Accepted

## Context
The system is an agency architecture aimed at real-time urban mobility and logistic optimization. It requires orchestrating multiple co-dependent, specialized agents (e.g., traffic, weather, cost) to validate route viability dynamically based on external variables. The environment generates frequent updates (currently simulated via scripts) that dictate autonomous decision-making. Relying on traditional, tightly-coupled request/response patterns would bottleneck performance and hinder the application's ability to react to real-time, concurrent environmental changes.

## Decision
We will adopt an Event-Driven Architecture (EDA) leveraging a central message broker. Specialized agents will act as independent consumers, subscribing to specific data topics (e.g., weather updates, traffic accidents) via a Publish/Subscribe pattern. The central message broker will facilitate all asynchronous communication, routing data from producers to the appropriate specialized agents.

## Considered Options
* **Synchronous Request/Response (REST/RPC):** Rejected. Creates tight coupling between specialized agents and introduces blocking operations, severely limiting real-time scalability.
* **Pipes and Filters:** Rejected. While discussed as a viable pipeline pattern, it is optimized for sequential data transformations rather than the dynamic, decentralized, and asynchronous event reactions required by autonomous agents.

## Consequences

**Pros:**
* **Asynchronous Autonomy:** Shifts away from request/response, granting agents the autonomy to consume and process data independently without blocking system execution.
* **Decoupling:** The central message broker separates event producers from consumers, maintaining independent organizational boundaries.
* **Scalability:** The publish/subscribe pattern inherently supports scaling individual agent types based on specific message load.

**Cons:**
* **Eventual Consistency:** The distributed, asynchronous nature of the architecture introduces eventual consistency across the agent network.
* **Middleware Coupling:** While agents are decoupled from each other, the entire system becomes heavily coupled to the central broker's uptime and performance.
* **Strict Schema Governance:** Events function as the Published Language between bounded contexts. Event data structures must be strictly managed and kept stable to prevent cascading integration failures across specialized agents.
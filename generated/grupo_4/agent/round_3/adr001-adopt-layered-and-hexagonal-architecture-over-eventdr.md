# [ADR-001] Adopt Layered and Hexagonal Architecture over Event-Driven

**Date:** 2026-05-22

## Status
Accepted

## Context
We are developing an AI agent system that requires a logical organization of UI, business APIs, and data access. While conversational and multi-agent systems often benefit from Event-Driven architectures for real-time data provisioning, our primary driver is system simplicity. We need an architecture that suits a straightforward application while ensuring business rules are cleanly isolated from external technical concerns. Traditional layered architectures are well-suited for simpler applications but can suffer from boundary leakage, whereas Hexagonal Architecture provides concrete implementation guidance for structuring and decoupling these layers.

## Decision
We chose to implement a Layered architecture integrated with Hexagonal (Ports and Adapters) patterns. This hybrid structures the system into logical tiers while utilizing Hexagonal boundaries to strictly isolate the core business logic from external systems, databases, user interfaces, and frameworks.

## Considered Options
* **Event-Driven Architecture:** Rejected. While optimal for reactive, real-time conversational workflows, it introduces unnecessary infrastructure and operational complexity (message routing, topics, channels) that exceeds our current requirements. We deliberately chose to forgo this to maintain simplicity.
* **Microservices / Micro Kernel:** Rejected. Deemed too complex for the current scope, risking over-engineering early in the project lifecycle. 

## Consequences

**Pros:**
* **Simplicity:** Aligns with the needs of simpler applications, avoiding the operational overhead of message brokers and asynchronous event tracing.
* **Superior Decoupling:** Hexagonal patterns ensure core business logic remains completely independent from external technologies and infrastructure.
* **High Testability:** Isolating logic into distinct, independent modules without cross-dependencies makes unit testing highly effective.

**Cons:**
* **Loss of Native Reactivity:** Forfeits the built-in real-time, asynchronous communication benefits provided by Event-Driven patterns.
* **Future Refactoring:** May require architectural restructuring if the product evolves to demand highly reactive, concurrent multi-agent data streams.
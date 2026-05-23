# [ADR-001] Adopt Layered Architecture Over Event-Driven for System Simplicity

**Date:** 2026-05-18

## Status
Accepted

## Context
The project involves building an application integrating AI agents (conversational/multi-agent). The system requires a clear structural organization for UI, business logic (API contracts), and data access. While an Event-Driven Architecture (EDA) naturally supports the real-time, reactive requirements of conversational agents, the team currently lacks deep familiarity with event-driven patterns. Adopting EDA introduces a high learning curve, significant asynchronous debugging overhead, and strict coupling restrictions that complicate standard inter-module communication. 

## Decision
We decided to adopt a Layered architecture (with potential Hexagonal organizational principles for logical isolation) and explicitly reject an Event-Driven approach. This prioritizes architectural simplicity, aligns with the team's current knowledge base, and supports both synchronous and asynchronous operations without the overhead of a dedicated messaging routing system.

## Considered Options
*   **Layered Architecture (Selected):** Isolates UI, business logic, and data layers. It offers a familiar request/response model, avoiding unnecessary complexity while still allowing logical separation of concerns (e.g., applying Hexagonal isolation within the layers).
*   **Event-Driven Architecture (Rejected):** While optimal for real-time reactivity and module autonomy, it was rejected due to the high learning curve, tracing/debugging complexity of asynchronous message communication, and the risk of developers accidentally violating architectural rules by bypassing event flows.
*   **Microkernel / Microservices (Rejected):** Acknowledged during discussions but deemed unnecessary for the current system scope and simplicity requirements.

## Consequences

**Pros:**
*   **Lower Learning Curve:** Aligns with the team's existing expertise, ensuring faster development and onboarding.
*   **Easier Debugging:** Relies on straightforward request/response patterns and standard direct method calls, avoiding the tracing overhead inherent in distributed asynchronous messaging.
*   **Architectural Stability:** Reduces the risk of accidental architectural violations and data consistency issues caused by external mutations bypassing event flows.

**Cons:**
*   **Reduced Reactivity:** Forfeits the native real-time, reactive event processing that benefits conversational AI workflows. 
*   **Tighter Coupling:** Modules will be more coupled compared to the strict autonomy achieved by an Event-Driven system, potentially requiring refactoring if system scale or real-time requirements drastically increase.
# [ADR-005] Adoption of MVC Architecture with Encapsulated Message Broker

**Date:** 2026-05-22

## Status
Accepted

## Context
The project is a 10v10 online competitive FPS game that relies heavily on asynchronous networking, client-side prediction, and event-driven state updates. We require a highly modular structural framework that cleanly separates UI, business logic, and application state. Additionally, the system must support complex inter-component communication (e.g., syncing inventory, processing delayed network states) without creating tight coupling or monolithic "god objects." 

## Considered Options
1. **Pure MVC (Direct Synchronous Communication):** Rejected. Traditional direct calls between components tightly couple the system and struggle to manage the delayed, asynchronous nature of competitive multiplayer game events.
2. **Pure Event-Driven Architecture:** Rejected. While excellent for decoupling, lacking the strict structural boundaries of MVC makes standard UI and local state management overly complex and harder to debug. 

## Decision
The project will adopt the **Model-View-Controller (MVC)** design pattern as the core structural framework, enhanced by encapsulating a **Message Broker**. 

* **Broker Encapsulation:** Inter-component communication will route through this message broker (acting as a message bus). It will utilize interfaces and dispatch queues to support an event-driven processing model (callbacks, register/unregister mechanics).
* **Model Modularization:** Instead of a single unified model, we will implement multiple modularized model classes tailored for specific layers (e.g., network state, UI state) to prevent the creation of "god objects."

## Consequences

**Pros:**
* **Separation of Concerns:** Clear delineation between Models, Views, and Controllers scales complexity linearly, making the codebase significantly easier to write, debug, and test.
* **Development Efficiency:** The structured separation inherently supports rapid, parallel development across different functional components.
* **Robust Asynchronous Handling:** The encapsulated broker safely queues and processes asynchronous events (e.g., dropped packets, delayed server reconciliations) without data loss or UI blocking.
* **High Modularity:** Layer-specific models ensure fewer cross-domain dependencies and greater overall flexibility.

**Cons:**
* **Architectural Overhead:** Blending a message broker into a traditional MVC flow increases the initial learning curve and architectural complexity for developers. 
* **Tracing Complexity:** Debugging event-driven message bus communication is inherently more difficult than tracing synchronous, direct method calls.
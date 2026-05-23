# [ADR-001] Adopt Layered and Hexagonal Architecture for Multi-Agent AI System

**Date:** 2026-05-22

## Status
Accepted

## Context
We are developing a multi-agent AI system. In conversational and multi-agent AI contexts, architectures must handle complex workflows and state management. An Event-Driven architecture is commonly utilized in these scenarios to facilitate real-time data feeding and reactive event processing. However, introducing an Event-Driven model requires managing asynchronous inter-modular communication and maintaining a dedicated event bus. The overarching priority for this project is system simplicity and the minimization of infrastructure overhead, necessitating an architecture that strictly avoids over-engineering. 

## Decision
We will structure the multi-agent AI project using a Layered architecture combined with Hexagonal patterns, explicitly rejecting an Event-Driven approach. 

Code and services will be logically organized into distinct layers (UI, Business/API, Data), utilizing Hexagonal mechanics to isolate business rules from external dependencies. Multi-agent orchestration will be handled via a single, agnostic orchestrator that executes a uniform sequence of functions, passing outputs as inputs sequentially, or running agents simultaneously and aggregating their outputs for speed.

## Considered Options
* **Layered combined with Hexagonal Patterns (Selected):** Embeds layered logical separation within a hexagonal framework. This provides concrete mechanics for isolating business logic, keeps control flow simple, and avoids over-engineering.
* **Event-Driven Architecture (Rejected):** While advantageous for real-time responsiveness, it requires an event bus, topics/channels mapping, and asynchronous communication routing. This introduces unnecessary infrastructure complexity that conflicts with our primary goal of system simplicity.

## Consequences

**Positive:**
* **System Simplicity:** Drastically reduces infrastructure complexity by avoiding message brokers and event buses.
* **Isolated Logic:** Hexagonal mechanics ensure clear boundaries between APIs, business schemas, and data access, preventing cross-dependency.
* **Simplified Orchestration:** Multi-agent execution is simplified to synchronous function chaining or parallel execution with output aggregation.

**Negative:**
* **Reduced Real-Time Reactivity:** Rejecting the Event-Driven approach results in a "loss" regarding native real-time responsiveness, making asynchronous analytics feeding and real-time continuous data streams more difficult to implement natively.
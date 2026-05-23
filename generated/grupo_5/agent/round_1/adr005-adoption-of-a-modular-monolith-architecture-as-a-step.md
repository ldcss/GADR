# [ADR-005] Adoption of a Modular Monolith Architecture as a Stepping Stone to Microservices

**Date:** 2026-05-11

## Status
Accepted

## Context
The mareIA platform must support diverse clinical scenarios (telemonitoring, teleconsultation) developed by multiple distributed institutional teams. We are operating under tight deadlines for initial architecture sketches and rapid prototyping. While a microservices architecture is suitable for large-scale systems, establishing it immediately introduces significant infrastructure overhead, integration complexity, and the risk of teams working in isolated silos. Conversely, a traditional monolith risks becoming unmaintainable as functionality grows. We require a structure that simplifies initial mental models for cross-team collaboration, natively leverages Domain-Driven Design (DDD) to establish bounded contexts, and preserves the flexibility to scale independently in the future. 

## Decision
We will adopt a mixed architectural approach, initially designing the system as a modular monolith composed of macro-modules. These macro-modules will act as strict bounded contexts that encapsulate internal components (conceptualized as internal microservices). Communication between these macro-modules will occur via well-defined internal APIs or events, rather than direct database integrations or coupled logic.

## Considered Options
1. **Pure Microservices:** Rejected. High initial complexity in managing network boundaries, distributed data, and infrastructure. Increases the risk of losing control while creating new structures across disparate teams.
2. **Traditional Layered Monolith:** Rejected. Tends to degrade into an anemic CRUD-style application without strict boundaries, hindering future scalability and making concurrent development difficult. 
3. **Modular Monolith (Chosen):** Balances the simplicity of a unified codebase for rapid prototyping with the strict boundaries required for future service extraction. 

## Consequences

**Pros:**
* **Enhanced Collaboration:** A unified codebase simplifies development, testing, and deployment, facilitating easier collaboration among the various institutional teams.
* **Controlled Complexity:** Allows teams to conceptualize the system as a monolithic block, reducing initial cognitive load and infrastructure management.
* **Evolutionary Path:** Acts as a stepping stone. High-level component patterns (DDD bounded contexts) ensure that macro-modules can be seamlessly migrated to independent microservices when required by specific scaling demands.

**Cons:**
* **Requires Strict Discipline:** Developers must rigorously maintain module boundaries. If internal boundaries are violated (e.g., cross-module database queries), the architecture will degrade into a tightly coupled monolith.
* **Deployment Coupling:** In the initial phase, all macro-modules are deployed together. A critical failure or resource exhaustion in one module can potentially impact the entire system footprint.
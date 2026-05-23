# [ADR-003] Adopt Modular Monolith Architecture

**Date:** 2026-05-22

## Status
Accepted

## Context
The system is in the early stages of requirement gathering for various telehealth scenarios (tele-monitoring, clinical protocols, offline/online synchronization). The business domain and user journeys are still being actively explored by multiple collaborating institutions. We need a foundational architecture that supports concurrent development and clear data flows, but we must avoid the immediate distributed-system complexities and operational overhead associated with premature microservice adoption. A pure microservices approach at this stage risks severe fragmentation and loss of domain boundary control. 

## Decision
The system will be structured as a modular monolith. Functionalities and initial services will be grouped within larger, well-defined macro-modules rather than deployed as an ecosystem of pure, independent microservices.

## Considered Options
* **Pure Microservices:** Rejected. Introduces significant upfront infrastructure complexity and creates a highly fragmented environment ("a mess") that is difficult to manage while domain boundaries are still volatile.
* **Traditional (Unstructured) Monolith:** Rejected. Fails to provide the necessary isolation for different functional areas (e.g., clinical follow-ups vs. data collection) and severely hinders future decoupling.
* **Modular Monolith (Chosen):** Provides a blended approach that enforces strict internal boundaries between modules while maintaining the simplicity of a single deployment unit during the domain exploration phase.

## Consequences

**Pros:**
* **Mitigates Fragmentation:** Prevents the loss of control over context boundaries and reduces the cognitive load of managing numerous decentralized repositories.
* **Lowers Upfront Complexity:** Bypasses the immediate operational and infrastructure overhead of distributed systems.
* **Safe Domain Exploration:** Offers the safest environment to develop functionalities while business requirements are still solidifying.
* **Future-Proof Flexibility:** Keeps the architecture sufficiently decoupled to allow extraction of specific modules into standalone microservices later, should scaling or time-to-market demands require it.

**Cons:**
* **Requires Boundary Discipline:** Developers must strictly enforce logical boundaries to prevent the architecture from degrading into a tightly coupled "big ball of mud."
* **Coarse-Grained Scaling:** In the short term, the system must be scaled at the macro-module or monolithic level rather than independently scaling specific, high-load micro-functionalities.
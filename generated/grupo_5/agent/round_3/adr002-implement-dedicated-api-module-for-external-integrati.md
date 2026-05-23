# [ADR-002] Implement Dedicated API Module for External Integrations (RNDS)

**Date:** 2026-05-22

## Status
Accepted

## Context
The platform requires interoperability with external systems, most notably the National Health Data Network (RNDS), to support data exchange across various clinical scenarios. Integrating external dependencies directly into core domain models creates fragile, tightly coupled architectures that are expensive to maintain. Furthermore, health data exchanges demand strict adherence to national data sovereignty, access restrictions, audit logging, and data retention policies. A scalable approach is required to handle real-time data exchange without necessitating modifications to the core systems whenever external requirements evolve.

## Decision
We will architect a dedicated API module to govern all external integrations and data exchanges. This module will act as an abstraction layer, exposing strict contracts with well-defined interfaces to separate core domain logic from specific external business logic (e.g., RNDS communication protocols). The module will explicitly define and centrally enforce all critical technical constraints, including authentication, access control, audit logging, and rate limiting.

## Considered Options
1. **Direct point-to-point integration in core models:** Integrate RNDS and other external communication scripts directly within the primary backend services. 
   * *Rejected:* Leads to high maintenance costs in distributed systems, fragile integrations, and violates the separation of concerns by tangling core domain logic with external communication constraints.
2. **Third-party Integration Platform (iPaaS):** Utilize an off-the-shelf managed integration platform to handle external routing.
   * *Rejected:* Introduces unacceptable risks regarding national data sovereignty and limits our fine-grained control over the strict health data security and audit logging policies mandated by the SUS ecosystem.

## Consequences
**Pros:**
* **Decoupling:** Enables standardized, real-time data exchange without requiring rebuilds of existing core systems.
* **Security & Compliance:** Centralizes the enforcement of critical security constraints (access control, audit logging, data retention) to prevent unauthorized access.
* **Reliability & Scalability:** Ensures robust external connections through strong resource modeling, independent versioning strategies, and standardized error handling.

**Cons:**
* **Initial Overhead:** Requires significant upfront effort to correctly model strict API contracts and define modular architecture boundaries.
* **Operational Complexity:** Adds a distinct architectural component that must be independently monitored, versioned, and maintained.
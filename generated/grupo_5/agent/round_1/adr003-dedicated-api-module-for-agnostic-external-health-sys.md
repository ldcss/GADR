# [ADR-003] Dedicated API Module for Agnostic External Health System Integration

**Date:** 2026-05-11

## Status
Accepted

## Context
The platform must interoperate with various external information systems to manage, collect, and store longitudinal healthcare data. Specifically, it needs to integrate with the National Health Data Network (RNDS) and other SUS-related systems (e.g., CNES, CNS) using the patient's CPF as the primary identifier. Directly coupling external system communications within core application modules creates technical debt, hinders scalability, and complicates maintenance. There is a strict requirement for a standardized data exchange format (HL7 FHIR) to represent clinical services and interventions accurately while ensuring data sovereignty and secure access.

## Decision
Design and implement a dedicated, agnostic API module responsible for all integration with external healthcare systems, including RNDS. 
* The module will expose strict contracts and well-defined interfaces to govern how external systems communicate with the platform.
* The module will encapsulate all data transformation, mapping internal domain models to standardized healthcare formats (specifically HL7 FHIR).
* Core application domains will remain entirely decoupled from external integration logic.
* API governance guidelines will be established to ensure secure, consistent, and standardized integrations.

## Considered Options
* **Option 1: Point-to-Point Integration within Core Modules:** Direct integration from individual microservices/macro-modules to RNDS. 
  * *Rejected:* Breaks separation of concerns, duplicates integration logic across the system, and tightly couples internal domain logic to external third-party API specifications.
* **Option 2: Dedicated Agnostic API Module (Chosen):** Centralized integration layer acting as a facade for external systems.
  * *Accepted:* Centralizes API governance, ensures consistent application of health standards (HL7 FHIR), and shields core systems from changes in external APIs.

## Consequences

**Pros:**
* **Interoperability:** Enables agnostic, standardized data exchange with RNDS and future external dependencies.
* **Separation of Concerns:** Core domain logic is completely isolated from external API complexities and data mapping logic.
* **Governance & Security:** Centralizes authentication, request validation, and auditing for external communications.
* **Maintainability:** Changes in external systems (like RNDS updates) only require modifications within the dedicated API module, minimizing regression risks.

**Cons:**
* **Development Overhead:** Requires upfront effort to design strict API contracts and implement data transformation layers.
* **Complexity:** Introduces an additional architectural component to deploy, monitor, and scale.
* **Standardization Dependency:** Team must acquire and maintain specialized knowledge of HL7 FHIR schemas and standards.
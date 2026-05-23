# [ADR-004] Adopt Care Sessions as Central Entity and HL7 FHIR for Service Summaries

**Date:** 2026-05-11

## Status
Accepted

## Context
The platform (# mareIA - Technology WG, meeting 04/28/2026) requires a foundational data architecture to orchestrate diverse telehealth interventions (e.g., telemonitoring, teleconsultation, educational orientation) across multiple clinical scenarios. Due to tight project deadlines and the requirement to eventually integrate with national systems like RNDS (National Health Data Network), the architecture must be highly interoperable, web-friendly, and capable of functioning as a unified transactional bus for all system modules. Legacy healthcare standards (HL7 V2, HL7 V3, CDA) rely on cumbersome XML structures that do not easily map to modern platform data models.

## Decision
1. **Core Data Entity:** We will adopt `care sessions` (home care) as the central data entity for the platform's transactional bus. All application modules and microservices will be built on top of this raw data skeleton, using it to trigger analyses, notifications, and clinical interventions.
2. **Interoperability Standard:** We will adopt **HL7 FHIR** (Fast Healthcare Interoperability Resources, R4 Normative) as the standard for generating and exchanging summaries of services offered by the platform.

## Considered Options
* **Custom Proprietary Data Model:** Relying entirely on a custom JSON schema for both internal transactions and external summaries. *Rejected* because it restricts longitudinal interoperability with external systems (like RNDS) and complicates future data migrations.
* **Legacy HL7 (V2/V3) or CDA:** Utilizing older healthcare standards. *Rejected* due to rigid, XML-heavy structures that introduce unnecessary overhead in modern, web-mobile ecosystems.

## Consequences

**Pros:**
* **Standardized Interoperability:** FHIR establishes a globally recognized format for longitudinal data exchange, enabling seamless integration with external healthcare information systems.
* **Modern Ecosystem:** FHIR utilizes modern web standards (JSON) and is backed by extensive library support and cloud computing platforms.
* **Unified Business Logic:** Centering the architecture on `care sessions` provides a clear, cohesive transactional flow that accommodates varying clinical protocols (e.g., palliative care, post-surgical follow-up) without fragmenting the core data model.

**Cons:**
* **Mapping Overhead:** The platform must maintain a clear translation layer between the highly-optimized internal `care sessions` schema and the external FHIR resource summaries.
* **Custom Profiling Required:** Because the base FHIR standard is highly flexible and lacks certain universally required operational fields (e.g., default `created_at` timestamps or complex multi-facility associations), the engineering team must design and maintain custom FHIR extensions and profiles to align with internal operational models.
# [ADR-003] Adopt HL7 FHIR for Health Services Data Structuring

**Date:** 2026-05-22

## Status
Accepted

## Context
The platform orchestrates diverse clinical protocols, telemonitoring, and health interventions across multiple institutions. To support these collaborative workflows and future integration with national registries like the Rede Nacional de Dados em Saúde (RNDS), the platform requires a robust, standardized data model. The system must efficiently summarize the health services offered, maintain high interoperability for downstream AI analysis, and allow seamless data exchange with external healthcare ecosystems. 

## Decision
We will utilize the HL7 FHIR (Fast Healthcare Interoperability Resources) standard to structure and summarize the health services data offered by the platform.

## Considered Options
1. **Custom/Proprietary JSON Schema:** 
   * *Rejected.* While initially faster to build, it lacks native interoperability with national health systems (e.g., RNDS) and increases the integration burden for external researchers and downstream applications.
2. **HL7 Version 2, Version 3, or CDA:** 
   * *Rejected.* These legacy standards are less expressive, heavily reliant on complex parsing, and significantly harder to implement within modern, API-driven architectures compared to FHIR.

## Consequences

**Pros:**
* **Industry Standardization:** FHIR is a widely adopted API-focused specification explicitly designed for modern healthcare data representation and exchange.
* **Simplified Implementation:** It is highly flexible and much easier to implement via RESTful APIs than legacy HL7 standards (V2, V3, CDA).
* **High Interoperability:** Structured health data becomes natively accessible to external software systems, researchers, and our internal AI analysis modules.
* **Extensibility:** Provides a foundational set of resources that easily adapt to the platform's diverse clinical scenarios (e.g., post-surgical follow-up, palliative care).

**Cons:**
* **Learning Curve:** Requires the engineering and clinical teams to familiarize themselves with FHIR resource models and standard terminology.
* **Mapping Overhead:** Raw telemetry, IoT data, and custom user journeys will require a transformation layer to map correctly into strict FHIR resources.
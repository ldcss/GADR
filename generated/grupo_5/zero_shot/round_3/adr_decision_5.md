# [ADR-005] Adoption of HL7 FHIR for Clinical Data and API Interoperability
- **Status**: Accepted
- **Context**: The platform will generate clinical summaries, intervention records, and telemonitoring logs that eventually must interact with external national health systems, specifically the RNDS (Rede Nacional de Dados em Saúde).
- **Decision**: Adopt the HL7 FHIR (Fast Healthcare Interoperability Resources) standard for structuring clinical data models and exposing the API module dedicated to external healthcare integrations.
- **Considered Options**:
  - *Custom JSON/XML Data Models*: Rejected. Custom schemas completely lack interoperability and would require heavy translation layers to connect with SUS/RNDS in the future.
  - *OpenEHR*: Rejected. While robust for full electronic health records, FHIR is more lightweight, API-friendly, and is the explicit standard adopted by the Brazilian Ministry of Health (RNDS).
- **Consequences**:
  - **Pros**: Guarantees future-proof interoperability with the national healthcare grid. Standardizes terminology and data exchange contracts across the different academic modules.
  - **Cons**: Introduces a steep learning curve for developers unfamiliar with FHIR resources and complex health informatics standards.
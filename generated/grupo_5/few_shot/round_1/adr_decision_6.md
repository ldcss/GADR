# [ADR-006] Adoption of HL7 FHIR Standard
- **Status**: Accepted
- **Context**: The platform will generate clinical summaries based on the services offered (telemonitoring, interventions, risk classifications). To ensure interoperability with the broader health ecosystem (e.g., RNDS), the data format must comply with health informatics standards.
- **Decision**: Adopt the HL7 FHIR (Fast Healthcare Interoperability Resources) standard for modeling and summarizing clinical data and services within the platform.
- **Considered Options**:
  - *Option 1: Custom JSON/XML data schemas.* Rejected because custom schemas are not interoperable and would require extensive transformation layers to communicate with standard health networks.
- **Consequences**:
  - *Pros:* Guarantees seamless interoperability with modern national and international health data networks.
  - *Cons:* Introduces a steep learning curve for developers and data architects unfamiliar with the strict FHIR resource modeling specifications.
# [ADR-004] External Interoperability Module (RNDS Integration)
- **Status**: Accepted
- **Context**: The application must not operate as an isolated silo. It requires the ability to securely fetch patient registries and push clinical intervention data to external systems, specifically the Brazilian National Health Data Network (RNDS) and other local SUS infrastructure.
- **Decision**: Develop a dedicated export/integration API module implementing the HL7 FHIR (Fast Healthcare Interoperability Resources) standard to handle all external communications.
- **Considered Options**:
  - *Option 1: Direct database integration with external systems.* Rejected as it violates security best practices, creates tight coupling, and is fundamentally incompatible with external government systems.
  - *Option 2: Custom proprietary REST APIs.* Rejected because the Brazilian health ecosystem mandates standardized interoperability protocols for clinical data exchange.
- **Consequences**:
  - *Pros:* Ensures regulatory compliance and seamless interoperability with RNDS and other SUS systems; centralizes all data transformation logic in a single boundary layer.
  - *Cons:* Introduces a steep learning curve for the development team to properly understand and implement the complex HL7 FHIR data models and resources.
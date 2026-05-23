# [ADR-004] External Integration Layer and Interoperability
- **Status**: Proposed
- **Context**: The platform must exchange health data with external systems, specifically the National Health Data Network (RNDS), without hard-coupling internal business logic to external APIs.
- **Decision**: Introduce a dedicated Integration API Gateway Module that abstracts external communications and formats data exchanges using standard healthcare protocols (e.g., HL7 FHIR).
- **Considered Options**:
  - *Point-to-Point Integration inside Application Modules*: Rejected because it tightly couples the core system to external dependencies, making changes to external APIs highly disruptive.
  - *Direct Database Sharing*: Rejected due to severe security risks and the inability to validate or transform data payloads in transit.
- **Consequences**:
  - **Pros**: Prevents vendor lock-in; centralizes authentication and data transformation for external payloads; ensures standard compliance (HL7 FHIR) for interoperability.
  - **Cons**: Adds a layer of architectural complexity; requires up-front effort to design robust API contracts before internal data structures are finalized.
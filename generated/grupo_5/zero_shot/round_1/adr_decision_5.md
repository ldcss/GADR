# [ADR-005] Dedicated API Gateway Module for RNDS Interoperability
- **Status**: Accepted
- **Context**: The system must exchange data with external healthcare systems, specifically the RNDS (National Health Data Network). It must also act as a platform capable of triggering standard tele-health services without hardcoding dependencies to external providers.
- **Decision**: Build an isolated, dedicated API integration module. This layer will handle all inbound/outbound communication with external systems (like RNDS) and translate internal system data into standard healthcare formats (e.g., HL7 FHIR).
- **Considered Options**:
  - *Direct Point-to-Point Integration*: Rejected. Embedding external API calls directly into the core business logic creates high coupling and makes the system brittle to external API changes.
- **Consequences**:
  - **Pros**: Isolates the core system from external network failures. Centralizes data transformation and compliance formatting. Promotes a plug-and-play architecture for future external services.
  - **Cons**: Adds an additional architectural layer that must be developed, tested, and maintained.
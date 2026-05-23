# [ADR-003] Initial Architectural Pattern (Modular Monolith)
- **Status**: Accepted
- **Context**: The platform encompasses diverse domains, including data collection, clinical protocols, risk analysis, and teleconsultation. There is an ongoing debate about structuring the backend as a distributed microservices architecture versus a monolith. Given that the domain boundaries, user journeys, and data flows are not yet fully mapped out, starting with pure microservices introduces high risk.
- **Decision**: Adopt a Modular Monolith architecture for the initial development phase, encapsulating distinct domains (e.g., patient management, risk analysis, telehealth) as strictly separated internal modules.
- **Considered Options**:
  - *Option 1: Pure Microservices Architecture.* Rejected due to the risk of premature optimization. It would introduce massive operational overhead, complex network orchestration, and high maintenance costs before the domain boundaries are fully understood.
  - *Option 2: Tightly Coupled Monolith.* Rejected because it prevents future scalability and makes it nearly impossible to decouple domains once the platform matures and requires independent scaling for specific features (like AI risk analysis).
- **Consequences**:
  - *Pros:* Simplifies deployment and infrastructure setup; allows the distributed teams to understand the complete end-to-end data flow more easily; provides a clear migration path to microservices later by simply extracting isolated modules.
  - *Cons:* Requires strict code-review discipline and architectural enforcement to prevent boundary leakage and tight coupling between the internal modules.
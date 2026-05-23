# [ADR-003] Macro-Modular Architectural Style
- **Status**: Accepted
- **Context**: The system must handle various telehealth protocols, real-time monitoring, and data analytics. Deciding early between a strict monolith and microservices is necessary to align the multi-institutional development teams. A pure microservices architecture poses a high maintenance and orchestration risk for the current team structure.
- **Decision**: Adopt a "macro-modular" architecture (a modular monolith approach). The system will be structured as a unified block composed of encapsulated internal modules/services aligned with specific domains (e.g., Data Collection, Risk Classification, Telehealth Interventions).
- **Considered Options**:
  - *Option 1: Pure Microservices Architecture.* Rejected due to the high initial DevOps overhead, fragmentation, and complex cross-network data flow management it would impose on the current teams.
  - *Option 2: Traditional tight-coupled Monolith.* Rejected because it would hinder the future scaling and addition of new clinical protocols.
- **Consequences**:
  - *Pros:* Simplifies the initial mental model, reduces deployment complexity, and streamlines data sharing between core domains while keeping future extraction into true microservices viable.
  - *Cons:* Requires strict CI/CD and architectural governance to prevent module boundaries from blurring and degrading into a "big ball of mud."
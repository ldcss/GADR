# [ADR-003] Modular Monolith (Macro-Services) as Initial Architectural Style
- **Status**: Accepted
- **Context**: The platform encompasses diverse clinical scenarios (palliative care, post-surgical monitoring, health education) requiring data collection, telemetry, and AI-driven risk classification. The team must define the overarching architectural style to manage data flows without paralyzing initial development.
- **Decision**: Adopt a Modular Monolith (or Macro-services) architecture for the initial phase, grouping related domain functionalities (e.g., patient management, telemonitoring protocols, interventions) into well-defined, encapsulated modules rather than starting with a fragmented microservices architecture.
- **Considered Options**:
  - *Pure Microservices*: Rejected. Premature fragmentation poses a high risk of deployment complexity, data consistency issues, and significant maintenance overhead for the current team structure.
  - *Tightly-Coupled Monolith*: Rejected. Prevents future independent scaling of resource-heavy components (like AI analysis or video streaming).
- **Consequences**:
  - **Pros**: Simplifies mental models, deployment, and tracing of user journeys across the system. Reduces initial operational overhead while maintaining logical boundaries for future decoupling.
  - **Cons**: Requires strict code-level discipline to prevent domain leakage between modules.
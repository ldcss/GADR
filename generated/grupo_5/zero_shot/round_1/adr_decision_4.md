# [ADR-004] Modular Monolith for Initial Backend Topology
- **Status**: Proposed
- **Context**: The project scope involves multiple complex domains (tele-monitoring, clinical protocols, AI interventions). The specific clinical user journeys and domain boundaries are still in the discovery phase. Selecting the wrong service boundaries early on will cause severe integration friction.
- **Decision**: Start backend development using a Modular Monolithic architecture rather than distributed microservices. All core functionalities (data collection, monitoring, tele-health services) will reside in a single deployable unit but must be strictly logically separated into internal modules.
- **Considered Options**:
  - *Distributed Microservices*: Rejected for the initial phase. The operational overhead, deployment complexity, and risk of incorrect boundary definitions are too high while domain requirements are still being mapped.
- **Consequences**:
  - **Pros**: Accelerates initial development. Simplifies deployment, debugging, and data flow tracing across different institutional modules.
  - **Cons**: Can degrade into a "big ball of mud" if module boundaries (interfaces) are not strictly enforced. Will require deliberate refactoring to extract microservices later when independent scaling is required.
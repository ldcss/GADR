# [ADR-001] Architectural Documentation and Decision Tracking
- **Status**: Accepted
- **Context**: The project involves multiple institutions and requires clear communication of architectural boundaries to both technical developers and non-technical clinical stakeholders. Traditional UML is considered too complex and rigid for this audience. Furthermore, the rationale behind critical architectural decisions needs to be preserved to prevent future operational friction.
- **Decision**: Adopt the C4 Model for architecture visualization and the Nygard Markdown template for Architecture Decision Records (ADRs).
- **Considered Options**:
  - *Option 1: UML (Unified Modeling Language).* Rejected because it lacks the intuitive, tiered approach necessary for interdisciplinary stakeholder communication.
  - *Option 2: Ad-hoc documentation via standard text documents.* Rejected due to the risk of inconsistent documentation and loss of historical decision rationale.
- **Consequences**:
  - *Pros:* Provides a highly accessible, zoomable mental model of the system (Context, Container, Component, Code) and ensures architectural governance via lightweight ADRs.
  - *Cons:* Requires the development team to familiarize themselves with C4 notation and maintain discipline in writing ADRs.
# [ADR-001] Architecture Documentation Strategy
- **Status**: Accepted
- **Context**: The project involves multiple universities and stakeholders, including both software engineers and clinical professionals. Documenting the architecture using traditional, verbose methods (like UML or RUP) creates a steep learning curve and hinders communication with non-technical stakeholders. Furthermore, architectural decisions need to be historically tracked to avoid redundant discussions and context loss over time.
- **Decision**: Adopt the C4 Model for visual architecture documentation (Context, Container, Component, and Code levels) and Architecture Decision Records (ADRs) for capturing significant technical choices.
- **Considered Options**:
  - *Option 1: UML (Unified Modeling Language).* Rejected because it is overly rigid, complex, and difficult for clinical stakeholders to interpret.
  - *Option 2: Ad-hoc diagramming and unstructured wikis.* Rejected because it lacks consistency across distributed teams and fails to capture the rationale behind critical, hard-to-reverse decisions.
- **Consequences**:
  - *Pros:* Provides an intuitive, zoomable map of the software architecture that all stakeholders can understand; creates a lightweight, version-controlled history of architectural decisions.
  - *Cons:* Requires discipline from developers to continually update diagrams and write ADRs as the system evolves.
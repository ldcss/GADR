# [ADR-004] Architecture Documentation Standards
- **Status**: Accepted
- **Context**: The project involves distributed teams across four different institutions, comprising stakeholders with varying levels of technical expertise (software engineers, clinical professionals, researchers). There is a high risk of knowledge loss and misalignment regarding system boundaries and irreversible technical decisions.
- **Decision**: Adopt the **C4 Model** for visual architectural documentation (focusing initially on Context and Container levels) and the **ADR (Architecture Decision Record)** standard for tracking technical decisions.
- **Considered Options**:
  - *Option 1: Standard UML diagrams and ad-hoc documentation.* Rejected because UML is often too rigid and difficult for non-technical stakeholders (e.g., clinical leads) to parse quickly, and ad-hoc documents easily become fragmented.
  - *Option 2: Heavy upfront architectural specification (Enterprise Architecture frameworks).* Rejected as it is too slow and verbous for the current agile discovery phase of the project.
- **Consequences**:
  - *Pros:* Provides a highly intuitive, zoomable map of the software architecture accessible to both technical and clinical stakeholders; establishes a lightweight, immutable historical log of "why" specific engineering decisions were made.
  - *Cons:* Requires continuous discipline from the engineering team to update C4 diagrams and write ADRs as the system evolves, introducing a slight overhead to the development process.
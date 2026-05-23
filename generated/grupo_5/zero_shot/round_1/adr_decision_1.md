# [ADR-001] Adoption of C4 Model and ADRs for Architecture Documentation
- **Status**: Accepted
- **Context**: The project involves multiple institutions and stakeholders with varying technical backgrounds (software engineers, healthcare professionals, researchers). There is a need for a standardized, intuitive method to document architectural boundaries and decisions without the heavy overhead and rigidity of traditional UML.
- **Decision**: Adopt the C4 Model for architectural diagramming, starting at the Context (Level 1) and Container (Level 2) levels to map user journeys and system boundaries. Concurrently, adopt Architecture Decision Records (ADRs) stored in version control (Markdown format) to log significant technical choices.
- **Considered Options**:
  - *UML (Unified Modeling Language)*: Rejected due to its complexity and low readability for non-technical clinical stakeholders.
  - *Traditional Heavy Documentation (e.g., RUP)*: Rejected due to high maintenance overhead and lack of agility.
- **Consequences**:
  - **Pros**: Creates an intuitive, zoomable map of the architecture. Facilitates communication with non-technical stakeholders. Ensures architectural history and rationale are preserved in the repository.
  - **Cons**: Requires team discipline to keep diagrams and ADR logs updated alongside code changes.
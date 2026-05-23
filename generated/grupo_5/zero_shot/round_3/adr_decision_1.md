# [ADR-001] Adoption of C4 Model and Markdown ADRs for Architectural Documentation
- **Status**: Accepted
- **Context**: The project involves multiple distributed academic and technical teams building a telehealth platform. There is a need to establish a standardized, lightweight method to document architectural decisions and system boundaries that can be easily understood by both technical developers and non-technical stakeholders (e.g., healthcare professionals).
- **Decision**: We will use the C4 Model for visualizing software architecture (starting at Context and Container levels) and Markdown-based Architecture Decision Records (ADRs) to track historical architectural choices.
- **Considered Options**:
  - *UML (Unified Modeling Language)*: Rejected. Too rigid and complex for non-technical stakeholders (clinical teams) to interpret easily.
  - *Traditional Heavy Documentation (e.g., RUP)*: Rejected. Too verbose, difficult to maintain, and slows down the agile design process.
- **Consequences**: 
  - **Pros**: Provides intuitive, zoomable diagrams (C4) that bridge the communication gap between engineers and clinical stakeholders. ADRs provide a clear, version-controlled history of technical tradeoffs.
  - **Cons**: Requires team discipline to continuously update diagrams and write ADRs alongside codebase changes.
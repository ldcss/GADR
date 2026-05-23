# [ADR-002] Hybrid Authentication Strategy and Offline Support
- **Status**: Accepted
- **Context**: The application requires offline operational capabilities for mobile health agents and caregivers in areas with poor connectivity. However, official authentication must link to national health records via `Gov.br`, which requires internet access. There is also a strict requirement regarding National Data Sovereignty.
- **Decision**: Implement a hybrid authentication architecture requiring an initial online login via `Gov.br`, paired with an internal local database mechanism that uses the CPF (National ID) as the primary key. This allows the mobile application to securely cache session data and operate offline.
- **Considered Options**:
  - *Option 1: Pure Gov.br Authentication.* Rejected because it completely breaks the required offline capabilities of the application.
  - *Option 2: Google Auth / Commercial OAuth providers.* Rejected explicitly due to National Data Sovereignty concerns and the inability to map natively to national health APIs (CNS/CNES).
- **Consequences**:
  - *Pros:* Satisfies both the offline operational requirements and the legal/integration requirements for national health systems. Secures data sovereignty.
  - *Cons:* Increases architectural complexity on the mobile/frontend clients, requiring robust local database synchronization, encrypted caching, and token expiration management.
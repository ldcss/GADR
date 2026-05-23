# [ADR-002] Hybrid Authentication Strategy and Offline Support
- **Status**: Accepted
- **Context**: The mobile and web telehealth applications will be used by patients, health agents, and clinicians in varying connectivity environments. The system requires official identity validation for the Brazilian health ecosystem (SUS), but must also function offline to allow local data caching and offline clinical routines.
- **Decision**: Implement a hybrid authentication and identity strategy. Initial user login and registration will be processed via the federal **GOV.BR** API to retrieve base identity data (e.g., CPF). This identity will then be mapped to an internal, proprietary database and cached locally on mobile devices.
- **Considered Options**:
  - *Strictly GOV.BR Authentication*: Rejected. Depending solely on GOV.BR prevents offline functionality and creates a single point of failure tied to external uptime.
  - *Google / Social OAuth*: Rejected. Unacceptable due to national data sovereignty constraints and compliance requirements for public health applications.
- **Consequences**:
  - **Pros**: Ensures data sovereignty. Validates users officially via CPF while enabling offline capabilities through mobile local caching. Prepares the system for future integrations with CNES and CNS.
  - **Cons**: Increases architectural complexity, requiring data synchronization logic between the local cache, the proprietary database, and state changes from GOV.BR.
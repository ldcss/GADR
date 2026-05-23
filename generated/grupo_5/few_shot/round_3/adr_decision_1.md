# [ADR-001] Authentication and Offline Access Strategy
- **Status**: Accepted
- **Context**: The platform will be used by health agents and patients in mobile environments that may lack reliable internet connectivity. The system requires secure user authentication and access to clinical data offline, while strictly adhering to Brazilian national data sovereignty and public health integration standards.
- **Decision**: Implement a hybrid authentication mechanism utilizing the federal **GOV.BR** system for initial online registration and primary authentication, paired with a local, on-device database utilizing the user's CPF (National ID) as the primary key for offline validation.
- **Considered Options**:
  - *Option 1: Third-party OAuth (e.g., Google/Apple).* Rejected due to strict national data sovereignty concerns and the inability to seamlessly map to internal public health records.
  - *Option 2: Purely online GOV.BR authentication.* Rejected because it completely breaks the core business requirement of allowing health agents to operate in offline/remote environments.
- **Consequences**:
  - *Pros:* Guarantees compliance with national data sovereignty; ensures continuous system availability for mobile users in offline scenarios; facilitates future integration with RNDS (Rede Nacional de Dados em Saúde).
  - *Cons:* Significantly increases mobile application complexity, requiring robust local database management, encrypted offline credential caching, and complex data synchronization logic when network connectivity is restored.
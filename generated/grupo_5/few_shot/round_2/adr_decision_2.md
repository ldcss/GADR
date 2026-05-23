# [ADR-002] Authentication Strategy and Offline Operation
- **Status**: Accepted
- **Context**: The platform will be used in telemonitoring scenarios where internet connectivity may be unreliable or non-existent (e.g., field agents visiting patients). Furthermore, there is a strict requirement to maintain national data sovereignty and integrate eventually with the Brazilian public health system (SUS).
- **Decision**: Implement initial online authentication via GOV.BR using the user's CPF (National ID) as the primary key, coupled with a proprietary local database cache on mobile clients to enable offline functionality.
- **Considered Options**:
  - *Option 1: Third-party OAuth providers (e.g., Google/Apple Auth).* Rejected due to strict national data sovereignty concerns and lack of direct alignment with public health system identities.
  - *Option 2: Purely online GOV.BR authentication.* Rejected because it renders the mobile application unusable in areas without internet access, blocking critical clinical data collection.
- **Consequences**:
  - *Pros:* Guarantees compliance with national data sovereignty laws; allows clinical staff to perform duties offline; perfectly aligns with future integrations into the National Health Data Network (RNDS) via CPF.
  - *Cons:* Significantly increases mobile client complexity, requiring robust local data caching, secure storage of sensitive health information on the device, and conflict-resolution mechanisms for offline-to-online synchronization.
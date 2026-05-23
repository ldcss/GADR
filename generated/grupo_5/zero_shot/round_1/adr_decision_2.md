# [ADR-002] GOV.BR Integration for Authentication and Identity Management
- **Status**: Accepted
- **Context**: The platform requires secure authentication for healthcare professionals, patients, and caregivers. The system must align with national health standards and ensure strict data privacy and national data sovereignty.
- **Decision**: Utilize the Brazilian government's official identity provider (GOV.BR) as the primary online authentication mechanism, using the CPF (National ID) as the primary key. 
- **Considered Options**:
  - *Google OAuth / Big Tech SSO*: Rejected explicitly due to national data sovereignty constraints and compliance risks regarding sensitive healthcare data.
  - *Standalone Custom Authentication*: Rejected as the primary method because it prevents seamless integration with the broader SUS (Unified Health System) ecosystem.
- **Consequences**:
  - **Pros**: Guarantees national data sovereignty. Ensures compliance with government healthcare ecosystem standards. Facilitates future integration with CNES (National Registry of Health Establishments) and CNS (National Health Card).
  - **Cons**: Creates a hard dependency on an external government service for the initial user onboarding and session generation.
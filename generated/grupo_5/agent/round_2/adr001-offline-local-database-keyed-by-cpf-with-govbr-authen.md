# [ADR-001] Offline Local Database Keyed by CPF with Gov.br Authentication

**Date:** 2026-05-22

## Status
Accepted

## Context
The tele-monitoring health application requires offline operational capabilities for field agents and caregivers who may lack reliable internet access. Additionally, as a system operating within the Brazilian public health ecosystem (SUS/RNDS), it must strictly comply with national data sovereignty and data residency requirements. Exposing sensitive health and authentication data to foreign service providers introduces unacceptable jurisdictional risks (e.g., the U.S. CLOUD Act). We must define a secure authentication and local caching strategy that balances offline functionality with strict regulatory compliance.

## Decision
The system will support offline operation using a local database keyed by the user's CPF, facilitated technically by JavaScript Service Workers. Initial registration and authentication must be performed online exclusively via Gov.br. Once the CPF is validated and the local cache is bootstrapped, the user can operate the application offline. We explicitly reject the implementation of Google Authentication (OAuth2) to maintain absolute data sovereignty.

## Considered Options
1. **Local DB with CPF Key + Gov.br Online Bootstrapping:** (Accepted) Satisfies both the offline operational requirement and national data sovereignty constraints while using the CPF to map to future RNDS/CNES integrations.
2. **Google Authentication (OAuth2):** (Rejected) Although utilizing Google's API would significantly accelerate development speed, it fundamentally violates data sovereignty requirements by exposing user access metadata to foreign legal jurisdictions.
3. **Strictly Online Gov.br Authentication:** (Rejected) Fails to meet the core operational requirement of offline access for health professionals and caregivers in the field.

## Consequences

**Pros:**
* **Data Sovereignty:** Strictly adheres to national compliance and data residency requirements by keeping authentication within the state-controlled Gov.br ecosystem.
* **Offline Resilience:** Service Workers and local database caching ensure uninterrupted application usage in disconnected environments.
* **Ecosystem Integration:** Utilizing CPF as the primary key establishes a direct path for future data synchronization with the national health bus (RNDS, CNES, and CNS).

**Cons:**
* **Development Overhead:** Sacrifices the rapid development and out-of-the-box convenience provided by commercial OAuth2 providers like Google.
* **Onboarding Constraint:** Forces a hard requirement that a user's very first interaction (registration/login) must occur in an online environment to validate credentials and populate the offline cache.
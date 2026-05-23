# [ADR-002] Primary Authentication via Gov.br with Local CPF Database for Offline Support

**Date:** 2026-05-11

## Status
Accepted

## Context
The application requires high availability, specifically the ability to operate offline in environments without internet connectivity. Consequently, an authentication mechanism is needed that balances offline access capabilities with strict national data sovereignty requirements. User identities in the Brazilian healthcare ecosystem (SUS) rely on the CPF (Cadastro de Pessoas Físicas) as the primary identifier. While ubiquitous authentication providers like Google are standard on mobile devices, they sync user credentials and data to foreign cloud servers, raising unacceptable national sovereignty and security risks.

## Decision
We will use **Gov.br** as the primary online authentication method, combined with a **local database utilizing CPFs** for offline support. We explicitly reject Google Authentication due to data sovereignty concerns. 

Initial user registration and authentication will require an online connection via Gov.br. Upon successful login, the system will securely cache the user's CPF locally. Subsequent offline access will be validated against this local database, ensuring high availability without relying on continuous external network connections.

## Considered Options
1. **Gov.br + Local CPF Database (Selected):** Meets offline availability requirements by caching the CPF locally. Aligns with national data sovereignty mandates by keeping identity data within government integrations and local devices.
2. **Google Authentication (Rejected):** Highly accessible on Android/iOS devices, but syncs user credentials to external, third-party cloud servers. This violates strict national data sovereignty constraints and unnecessarily exposes the system to vulnerabilities associated with large external credential stores.
3. **Purely Online Gov.br Authentication (Rejected):** Relies entirely on continuous internet connectivity, failing to meet the critical offline accessibility requirement for healthcare agents and patients.

## Consequences

**Pros:**
* **Data Sovereignty Compliance:** Sensitive identity data remains strictly within national systems and the local device environment.
* **High Availability (CIA Triad):** Offline local database ensures system availability and continuous user access even when primary online networks are unreachable.
* **Seamless Ecosystem Integration:** Anchoring on the CPF facilitates future integrations with other national health databases (e.g., CNES for professionals, CNS for patients).

**Cons:**
* **Implementation Complexity:** Introduces the architectural overhead of building, securing, and maintaining a local caching and bidirectional synchronization mechanism for the CPF database.
* **Online Prerequisite:** Users are strictly required to perform their initial registration and login while online before offline capabilities can be activated on their device.
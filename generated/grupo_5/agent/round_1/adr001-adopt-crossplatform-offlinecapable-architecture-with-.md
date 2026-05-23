# [ADR-001] Adopt Cross-Platform Offline-Capable Architecture with Local Caching

**Date:** 2026-05-11

## Status
Accepted

## Context
The system must support clinical and telemonitoring workflows across varied devices (smartphones, tablets, desktops) in environments with intermittent or zero internet connectivity. Tight project deadlines preclude the development of independent native applications for each platform. Furthermore, the system must securely collect and collate complex, mixed-type data (text, videos, photographs) without data loss, adhere to national data sovereignty principles, and allow seamless integration with public health infrastructure such as the RNDS (National Health Data Network). 

## Decision
We will adopt a unified cross-platform (Web/Mobile) architecture that leverages local device caching to ensure full offline capability. 

Specifically, the architecture will enforce:
1. **Local Caching:** The application will download core assets to the local cache upon first use, functioning as a device-agnostic web/mobile app capable of remote data entry.
2. **Hybrid Authentication:** Initial online registration and authentication will be routed through Gov.br. A secure local database will cache the user's CPF (Tax ID) to authorize subsequent offline access.
3. **Integration API:** A dedicated export/integration API module will be implemented to handle asynchronous data synchronization with external systems (including RNDS) once network connectivity is restored.

## Considered Options
* **Separate Native Applications (iOS/Android):** Rejected. Developing and maintaining distinct native applications is unfeasible given current time and resource constraints. A single cross-platform web approach accelerates delivery.
* **Purely Online Web Application:** Rejected. Target deployment environments face intermittent connectivity. An online-only approach risks critical clinical data loss and blocks field operations.
* **Third-Party Identity Providers (e.g., Google OAuth):** Rejected. While technically convenient for caching auth states, relying on foreign identity providers violates strict national data sovereignty requirements for public health data. 

## Consequences
**Pros:**
* **Resilience:** Guarantees uninterrupted functionality and prevents data loss during remote offline operations.
* **Development Efficiency:** A single cross-platform codebase significantly reduces development and maintenance overhead.
* **Compliance & Sovereignty:** utilizing Gov.br and a proprietary local database ensures adherence to public sector security standards.
* **Interoperability:** The abstracted API module future-proofs the system against RNDS dependency changes.

**Cons:**
* **Synchronization Complexity:** Requires robust offline-first state management and conflict resolution logic to securely sync heavy payloads (photos, videos) upon reconnecting.
* **Storage Limitations:** Local caching demands strict storage quota management to support low-end devices without degrading OS performance. 
* **Initial Onboarding Dependency:** Users must have active internet connectivity for their very first session to authenticate via Gov.br and seed the local cache.
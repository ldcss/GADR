# [ADR-001] Initial Authentication via Gov.br with Local CPF Caching for Offline Access

**Date:** 2026-05-22

## Status
Accepted

## Context
The telehealth platform must support mobile usage in environments with poor or no internet connectivity (e.g., home care, telemonitoring). As an e-government health solution integrating with the SUS ecosystem, strict data sovereignty and security contexts are mandatory. The system requires highly reliable identity proofing without relying on commercial third parties, which pose unacceptable data sovereignty risks and architectural dependencies.

## Decision
We will use Gov.br for the initial online user authentication and registration. Upon successful initial login, the user's CPF and essential profile data will be securely cached in a local database on the mobile device. This local CPF cache will serve as the validation key for subsequent offline access and local data operations, with data synchronizing to the central bus once connectivity is restored. 

## Considered Options
* **Google Authentication (OAuth2):** Rejected. While offering rapid development, it introduces severe data sovereignty concerns. It improperly relies on a commercial third-party, forces users to have a Gmail account (requiring redundant login mechanisms for accessibility), and fails to meet the strict security contexts required for government health data.
* **Gov.br with Local CPF Caching (Chosen):** Accepted. Satisfies government-grade security requirements by using official identity proofing. The localized data structure prevents external dependencies, ensures national data sovereignty, and robustly supports offline capabilities.

## Consequences

**Positive:**
* **Data Sovereignty:** Eliminates reliance on foreign commercial identity providers, keeping sensitive user access fully within national/government control.
* **Offline Capability:** The local database and CPF caching allow health professionals and patients to use the system without persistent internet connectivity.
* **Official Validation:** Leverages established official data services (CPF Inquiry) for digital onboarding and risk mitigation.

**Negative:**
* **Implementation Complexity:** Increases engineering overhead to securely manage the local database cache and synchronize offline data.
* **Connectivity Prerequisite:** The user's very first system access and registration strictly require an active internet connection to validate against the Gov.br API.
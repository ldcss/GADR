# [ADR-004] Integrate RNP Web Conference for Video Collaboration

**Date:** 2026-05-22

## Status
Accepted

## Context
The telehealth platform requires robust video collaboration capabilities to support various clinical interventions, including tele-monitoring, tele-consultation, and tele-inter-consultation. The project faces strict delivery deadlines and resource constraints. Developing a custom video conferencing module from scratch is highly complex, expensive, and risks diverting engineering focus away from core clinical data integration. RNP currently provides a market-validated web conference service with the necessary interactive features for telehealth workflows.

## Decision
The platform will integrate the existing RNP web conference service for its video collaboration capabilities rather than building a custom component from scratch.

## Considered Options
*   **Integrate RNP Web Conference (Selected):** Leverages a ready-made, validated solution already native to the RNP ecosystem, providing immediate access to required collaboration features.
*   **Build Custom Video Component (Rejected):** Requires significant engineering effort, delays time-to-market, and introduces unproven reliability risks, acting against cost and resource efficiency.
*   **Integrate Commercial Third-Party API (e.g., Zoom, Google Meet) (Rejected):** Introduces national data sovereignty concerns (as previously noted regarding authentication strategies) and potential external licensing dependencies.

## Consequences

**Pros:**
*   **Resource Efficiency:** Bypasses the high costs and effort associated with developing a real-time video system from the ground up, saving significant development time.
*   **Feature Readiness:** Grants immediate access to built-in interactive features (audio, video, screen sharing) required for effective clinical collaboration.
*   **Proven Reliability:** Adopts a market-validated digital platform, acting as a stable cornerstone for modern communication.

**Cons:**
*   **Platform Dependency:** The technical effectiveness and uptime of the tele-consultation module are strictly dependent on the external RNP service.
*   **Integration Overhead:** Requires engineering effort to securely connect the RNP video collaboration service with the platform's internal clinical record and appointment scheduling services.
*   **Limited Customization:** Core video UI and low-level feature behaviors are constrained by what the existing RNP platform provides.
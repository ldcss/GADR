# [ADR-004] Integrate RNP Web Conference Tool for Video Collaboration

**Date:** 2026-05-22

## Status
Accepted

## Context
The telemonitoring platform requires robust video collaboration capabilities to support various telehealth services, including tele-consultation, tele-interconsultation, and tele-orientation. The project faces strict deadlines for architecture delivery and operates with limited development resources across university teams. Developing a secure, real-time audio/video streaming component from scratch introduces significant technical complexity and regulatory compliance risks, diverting focus from the platform's core clinical care processes. RNP (Rede Nacional de Ensino e Pesquisa) currently provides an established, validated web conference service within our institutional ecosystem.

## Decision
Integrate RNP's existing web conference tool for video collaboration instead of developing a custom video component from scratch. The video collaboration service will be integrated directly with the clinical record service via standard APIs/SDKs to map telehealth sessions to patient protocols.

## Considered Options
* **Custom Video Component Development:** Rejected. Building a secure, compliant AV infrastructure demands massive overhead in time and cost, delaying the project and shifting engineering focus away from core clinical features.
* **Third-Party Commercial Tools (e.g., Zoom, Google Meet):** Rejected. RNP's tool is already available within the academic/health ecosystem, ensuring national data sovereignty, eliminating external licensing costs, and providing a validated environment tailored to our institutional context.

## Consequences

**Pros:**
* **Immediate access to complex features:** Provides a ready-to-use suite of A/V and interactive features without custom development time.
* **Out-of-the-box security and compliance:** Leverages built-in secure infrastructure and data privacy safeguards crucial for health data, bypassing the need to architect these from scratch.
* **Automated data exchange:** Pre-built integrations facilitate syncing session details and documentation directly into the clinical record service.
* **Unified user experience:** Allows seamless workflow connections, enabling users to join scheduled tele-interconsultations with a single click.
* **Leverages standard integration:** Connects easily with existing business logic and clinical protocols using established APIs/SDKs.

**Cons:**
* **External dependency:** System reliability is coupled with the uptime and maintenance schedule of the RNP infrastructure.
* **UI/UX limitations:** Less flexibility to heavily customize the internal interface of the video conferencing room compared to a bespoke solution.
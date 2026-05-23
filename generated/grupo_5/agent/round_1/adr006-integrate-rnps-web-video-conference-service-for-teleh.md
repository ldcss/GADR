# [ADR-006] Integrate RNP's Web Video Conference Service for Telehealth Video Collaboration

**Date:** 2026-05-11

## Status
Accepted

## Context
The telehealth platform requires robust, live, two-way video conferencing to support telemonitoring interventions, tele-interconsultations, and tele-consultancies. Developing a custom video conferencing component from scratch introduces significant development overhead, maintenance risks, and potential compliance issues, especially under current tight project deadlines. Best practices dictate investing in established, reliable platforms that seamlessly integrate with existing clinical records and healthcare infrastructure to ensure accessible, remote care delivery.

## Decision
We will integrate RNP's existing web video conference service for telehealth video collaboration instead of developing a custom video component from scratch.

## Considered Options
1. **Integrate RNP's Web Video Conference Service (Selected):** Leverages an existing, market-validated component within the RNP ecosystem. Provides immediate accessibility and reliability without the technical overhead of custom development.
2. **Develop Custom Video Component (Rejected):** Requires significant engineering effort and long-term maintenance. Reinventing a foundational, market-validated capability introduces unnecessary project risk and delays time-to-market.
3. **Integrate Commercial Third-Party Service (Rejected):** Utilizing external commercial platforms (e.g., Google Meet, Zoom) introduces potential data sovereignty risks and licensing costs, whereas RNP is aligned with the project's national academic and health infrastructure.

## Consequences
* **Pros:**
  * Eliminates the technical overhead and maintenance risks associated with custom video component development.
  * Accelerates development by utilizing an established, market-validated solution.
  * Provides immediate reliability and accessibility for remote healthcare delivery.
  * Aligns with best practices for seamless integration with clinical record services (EHR) for telehealth documentation.
* **Cons:**
  * Introduces a hard dependency on RNP's service uptime, roadmap, and API constraints.
  * Requires dedicated integration effort to map the video collaboration service seamlessly with the clinical care record models and workflows.
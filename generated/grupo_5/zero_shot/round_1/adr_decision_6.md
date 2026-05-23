# [ADR-006] Isolation of AI and Analytics Engine
- **Status**: Proposed
- **Context**: The platform must process collected clinical data to provide risk classification, predictive alerts, and dashboards for care teams. These analytical and machine learning workloads have drastically different compute profiles compared to standard transactional data entry.
- **Decision**: Isolate the AI, risk analysis, and analytics capabilities into a dedicated, standalone module separate from the transactional operational core.
- **Considered Options**:
  - *Embedded Analytics*: Rejected. Running heavy AI inference or complex dashboard queries on the same database/process as the transactional tele-monitoring system risks severe performance degradation.
- **Consequences**:
  - **Pros**: Allows independent scaling of compute-heavy AI tasks. Protects the transactional core's performance. Enables polyglot persistence or specialized databases (e.g., vector DBs or data warehouses) for analytics.
  - **Cons**: Requires building reliable asynchronous communication (e.g., event queues) between the transactional core and the AI module to trigger interventions.
# [ADR-003] Macro-Architecture Strategy (Modular Monolith over Strict Microservices)
- **Status**: Accepted
- **Context**: The system must support diverse tele-health operations (telemonitoring, teleconsultation, patient triage, AI analysis). While a microservices architecture was initially drafted, the exact domain boundaries and user journeys are still being defined by the clinical groups. There is a high risk of maintenance overhead and fragmented data if fine-grained services are defined prematurely.
- **Decision**: Adopt a Modular Monolith (Macro-services) approach for the initial platform architecture. The system will be structured as coarse-grained logical blocks (e.g., Data Collection, Clinical Protocols, Telemonitoring) rather than independently deployed microservices, with internal logic potentially organized as micro-modules.
- **Considered Options**:
  - *Strict Microservices*: Rejected at this stage due to the high orchestration overhead, distributed transaction complexity, and the risk of creating a "distributed monolith" before domain boundaries are fully understood.
  - *Traditional Tightly-Coupled Monolith*: Rejected because it prevents the distinct separation of core clinical capabilities and limits future scalability of specific modules (e.g., AI Analysis).
- **Consequences**:
  - **Pros**: Simplifies initial development, deployment, and data flow tracing; reduces infrastructural management overhead; allows teams to focus on mapping clinical workflows rather than networking concerns.
  - **Cons**: May require strategic refactoring and decoupling later in the lifecycle if specific modules require independent scaling or specialized deployment environments.
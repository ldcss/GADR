# [ADR-002] Architectural Style: Modular Monolith with Macro-Services
- **Status**: Accepted
- **Context**: The platform must integrate multiple distinct domains: tele-monitoring, clinical protocols, risk classification, and AI-based health literacy. While a microservices architecture was proposed to handle these domains, the system's exact bounded contexts and user journeys are still being mapped across four different institutional scenarios, making early distributed decomposition highly risky.
- **Decision**: Adopt a Modular Monolith (Macro-services) approach for the initial platform architecture. The system will be built as a cohesive unit centered around the core transaction (patient attendance/care), with logically encapsulated internal modules (data collection, AI analysis, notifications) that can be orchestrated together.
- **Considered Options**:
  - *Option 1: Pure Microservices Architecture.* Rejected for the initial phase due to the high operational overhead, distributed data management complexity, and the lack of clearly defined domain boundaries at this stage of the project.
  - *Option 2: Traditional tightly-coupled Monolith.* Rejected because it prevents the future scalability, independent deployment, and modular reuse required by the varying clinical scenarios.
- **Consequences**:
  - *Pros:* Simplifies initial development, testing, and deployment; allows the team to understand global data flows and user journeys without the DevOps overhead of managing distributed services; provides a clear migration path to microservices once domain boundaries are solidified.
  - *Cons:* Requires strict engineering discipline to maintain logical separation of modules via interfaces to prevent the codebase from degrading into a tightly coupled monolith.
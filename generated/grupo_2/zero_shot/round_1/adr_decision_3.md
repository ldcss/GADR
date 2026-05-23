# [ADR-003] Domain-Specific Multi-Agent Worker Model
- **Status**: Accepted
- **Context**: The route recommendation engine must evaluate disparate, competing variables such as financial cost, travel time, and carbon footprint. A single, centralized calculation engine would become overwhelmingly complex and difficult to tune. Furthermore, the system must expose its step-by-step logical reasoning to the end user.
- **Decision**: Decompose the core routing logic into autonomous, specialized domain agents (e.g., Traffic Agent, Weather Agent, Cost Agent). Each agent will evaluate specific localized rules against incoming broker messages (e.g., the Weather Agent invalidating motorcycle routes during heavy rain) and append its rationale to the event payload before passing it along.
- **Considered Options**:
  - *Monolithic Rules Engine*: Rejected because centralizing all decision-making violates separation of concerns, complicates dynamic tuning of specific modal parameters, and makes it harder to extract individual logical steps for the user feedback interface.
- **Consequences**:
  - **Pros**: Exceptional modularity; aligns perfectly with the requirement to display transparent, step-by-step system reasoning to users; agents can be scaled independently based on their specific workload.
  - **Cons**: Increases the risk of complex inter-agent choreography; mandates strict, versioned data contracts to ensure payloads remain compatible as they traverse multiple distinct agents.
# [ADR-001] Event-Driven Architecture for Agent Communication
- **Status**: Accepted
- **Context**: The system requires real-time multimodal transport analysis and dynamic route recalculation. Multiple co-dependent agents (e.g., traffic, weather, cost) must exchange data and react to sudden environmental changes without blocking system execution.
- **Decision**: Adopt an Event-Driven Architecture (EDA) utilizing a central Message Broker. Agents will operate as asynchronous consumers (workers), subscribing to specific domain topics (e.g., weather updates) and publishing their processed decisions back to the broker for downstream consumption.
- **Considered Options**:
  - *Synchronous REST/RPC Calls*: Rejected due to the risk of cascading failures, tight coupling between agents, and inadequate scalability for continuous real-time data processing.
- **Consequences**:
  - **Pros**: Highly scalable; enables truly asynchronous processing; agent decoupling allows for independent deployment and isolated failure domains.
  - **Cons**: Introduces architectural overhead (broker provisioning and maintenance); requires complex tracing for debugging message flows across multiple agents.
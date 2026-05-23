# [ADR-002] Adopt Event-Driven Architecture for Inter-Agent Orchestration
- **Status**: Accepted
- **Context**: The system must orchestrate multiple co-dependent, specialized agents (e.g., traffic agent, weather agent, cost agent) that perform real-time multimodal route analysis. These agents must react dynamically to changing variables, requiring an orchestration model that supports asynchronous processing and high scalability. 
- **Decision**: We will adopt an Event-Driven Architecture (EDA) centered around a Message Broker. The simulated environment will publish data to the broker, and agents will act as consumers/workers, subscribing exclusively to topics relevant to their domain of expertise.
- **Considered Options**:
  - *Event-Driven Architecture (Pub/Sub Message Broker)*: Accepted. Agents subscribe to specific data streams (e.g., the weather agent listens only to weather events). Upon processing, agents can publish their constraints or decisions back to the queue for subsequent downstream processing.
  - *Synchronous Request-Response (REST/gRPC)*: Rejected. Direct synchronous communication between agents would create tight coupling, blocking bottlenecks, and complicate the dynamic recalibration of routes.
- **Consequences**:
  - **Pros**: Complete decoupling of specialized agents; high scalability; natively supports the asynchronous nature of real-time environmental monitoring and dynamic route recalculation.
  - **Cons**: Introduces architectural overhead (deployment and maintenance of a message broker); increases the complexity of end-to-end tracing, making the requirement to "exhibit the logical reasoning used by agents" harder to implement in the UI.
```
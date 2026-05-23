# [ADR-002] Event-Driven Architecture for Agent Orchestration
- **Status**: Accepted
- **Context**: The system relies on multiple specialized, co-dependent agents (e.g., traffic agent, weather agent, cost agent) to continuously evaluate multimodal route viability. These agents must react instantly to dynamic environmental changes (such as accidents or subway delays) to autonomously recalculate routes.
- **Decision**: Adopt an Event-Driven Architecture (EDA) utilizing a Message Broker to handle asynchronous communication and data distribution among the specialized agents.
- **Considered Options**:
  - *Option 1: Synchronous REST/gRPC communication.* Rejected because it creates tight coupling between agents, inherently limits scalability, and is ill-suited for reacting to continuous, unpredictable environmental updates.
  - *Option 2: Event-Driven Architecture with a central Message Broker.* Accepted because it allows agents to act as independent consumers (workers) that subscribe exclusively to relevant data topics (e.g., a weather agent only listens to weather events).
- **Consequences**:
  - *Pros:* Maximizes decoupling of agent business logic; highly scalable; natively supports real-time asynchronous data streams; simplifies the addition of new specialized agents in the future without modifying existing infrastructure.
  - *Cons:* Increases infrastructure complexity due to the deployment and management of a message broker; debugging and tracing the lifecycle of a specific route decision across multiple decoupled agents will require robust distributed tracing and observability tools.
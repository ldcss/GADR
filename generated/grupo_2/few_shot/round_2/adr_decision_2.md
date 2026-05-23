# [ADR-002] Event-Driven Architecture for Agent Orchestration
- **Status**: Accepted
- **Context**: The system requires multiple co-dependent, specialized agents (Traffic Agent, Cost Agent, Weather Agent, etc.) to process data, detect critical environmental changes, and exchange information to determine route viability. These agents must operate autonomously, react dynamically to external inputs, and scale efficiently.
- **Decision**: Adopt an Event-Driven Architecture (EDA) utilizing a central Message Broker (message queue). The environmental simulation script will act as a publisher, sending specific data types to designated topics, while specialized agents will act as consumers (workers) subscribed only to their domain-relevant topics.
- **Considered Options**:
  - *Option 1: Synchronous HTTP/REST communication between agents.* Rejected because it tightly couples the agents, introduces latency bottlenecks, and does not natively support the asynchronous, continuous nature of real-time environmental monitoring.
  - *Option 2: Event-Driven Architecture via Message Broker.* Accepted as it provides robust asynchronous processing, decoupling of publishers and subscribers, and native scalability for individual worker types.
- **Consequences**:
  - *Pros:* High scalability and clear separation of concerns; agents only process relevant data (e.g., the Weather Agent only listens to weather queues); enables asynchronous recalculations without blocking other system processes.
  - *Cons:* Introduces distributed system complexity; requires operational overhead to manage and monitor the message broker infrastructure; tracing the end-to-end logical flow of a final route decision across multiple asynchronous agents will be more difficult.
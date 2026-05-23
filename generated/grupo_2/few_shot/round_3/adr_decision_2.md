# [ADR-002] Event-Driven Architecture with Message Broker for Agent Orchestration
- **Status**: Accepted
- **Context**: The core system requirement is the orchestration of co-dependent, specialized agents (Traffic, Weather, Cost) that must analyze real-time multimodal transport viability. Relying on synchronous, point-to-point communication between these agents creates tight coupling, limits scalability, and hinders the system's ability to react immediately to asynchronous external events (e.g., a sudden traffic delay).
- **Decision**: Adopt an Event-Driven Architecture (EDA) utilizing a central message broker. Agents will act as decoupled consumers/workers, subscribing only to topics relevant to their domain expertise.
- **Considered Options**:
  - *Option 1: Synchronous API calls (REST/gRPC) between agents.* Rejected because the continuous, unpredictable influx of environmental data requires asynchronous, non-blocking reactions. Synchronous chains would lead to latency bottlenecks and potential cascading failures.
  - *Option 2: Implement a Facade Pattern to simplify direct API interactions.* Discussed initially, but rejected because structural simplification does not solve the fundamental need for asynchronous data distribution and independent agent processing.
- **Consequences**:
  - *Pros:* Highly scalable and natively asynchronous; allows independent deployment and scaling of specific agents; the Python data generator (producer) is entirely decoupled from the business logic (consumers).
  - *Cons:* Increases infrastructure complexity (requires deploying and managing a broker like RabbitMQ or Kafka); complicates system observability, debugging, and tracing of a single routing decision across multiple isolated events.
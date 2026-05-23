# [ADR-001] Asynchronous Event-Driven Architecture with a Message Broker
- **Status**: Accepted
- **Context**: The system is a competitive 10v10 online FPS game. Processing real-time player inputs and game state changes synchronously risks blocking operations, causing severe lag, and losing data during transient network drops. 
- **Decision**: Adopt an asynchronous Event-Driven Architecture utilizing a Message Broker (e.g., Kafka) on the server to manage the continuous stream of game events and player actions.
- **Considered Options**:
  - *Option 1: Synchronous API calls (e.g., standard HTTP/REST).* Rejected due to the risk of blocking the main game thread, inability to handle temporary client disconnects without data loss, and high latency.
  - *Option 2: Standard MVC without a message queue.* Rejected as it cannot efficiently manage the high-frequency, publish-subscribe data distribution needed for real-time multiplayer updates across multiple microservices.
- **Consequences**:
  - *Pros:* Decouples services, ensures event persistence (messages aren't lost if a service momentarily drops), and efficiently handles high-throughput asynchronous data streams.
  - *Cons:* Significantly increases infrastructure complexity, deployment effort, and necessitates careful event orchestration to guarantee correct processing order.
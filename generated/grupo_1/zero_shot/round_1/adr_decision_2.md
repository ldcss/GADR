# [ADR-002] Asynchronous Event-Driven Backend Architecture 
- **Status**: Accepted
- **Context**: The game backend must handle real-time data streams from 20 players, route events, and communicate with various microservices (e.g., persistent player data across global servers, inventory). Synchronous communication risks data loss if a service temporarily drops.
- **Decision**: We will implement an asynchronous, Event-Driven Architecture utilizing a Message Broker (e.g., Kafka) to queue and route backend system messages.
- **Considered Options**: 
  - **Synchronous HTTP/REST with standard MVC**: Rejected because if a downstream service (like persistent storage or a matchmaking node) is briefly unavailable, the request fails and data is lost.
- **Consequences**: 
  - **Pros**: High fault tolerance; messages are buffered and retained even if services crash. Decouples core game server logic from auxiliary systems.
  - **Cons**: Increased infrastructure complexity; requires careful orchestration to manage event ordering and eventual consistency.
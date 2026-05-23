# [ADR-003] Backend Microservices and Event-Driven Communication
- **Status**: Accepted
- **Context**: Beyond the real-time game server, the platform requires persistent global data management (player accounts, inventory, regional server migration, marketplace). These backend systems must be highly decoupled, scalable, and resilient to individual service failures.
- **Decision**: Implement an Event-Driven Architecture utilizing a Message Broker (Apache Kafka) for asynchronous backend microservice communication.
- **Considered Options**:
  - *Synchronous HTTP/REST (MVC direct calls)*: Rejected due to tight coupling and risk of data loss. If the inventory service goes down during a transaction, the request drops.
  - *Monolithic Database Polling*: Rejected due to poor scalability and database bottlenecking across global server regions.
- **Consequences**:
  - **Pros**: High fault tolerance (Kafka retains messages up to 7 days, allowing recovering services to process backlogs). Enables robust orchestration of complex transactions (e.g., cross-region player data migration, purchases).
  - **Cons**: Increases infrastructure complexity, operational overhead, and requires eventual consistency handling in the UI.
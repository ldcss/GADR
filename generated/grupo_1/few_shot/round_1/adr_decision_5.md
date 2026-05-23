# [ADR-005] Event-Driven Architecture for Backend Microservices
- **Status**: Accepted
- **Context**: Outside of the core game loop, the system must handle cross-server data persistence, global inventory, and marketplace transactions. These tasks must not block the main game servers. Furthermore, if a service goes down, critical data (like a purchase or account transfer) cannot be lost.
- **Decision**: Adopt an Event-Driven Architecture utilizing a Message Broker (e.g., Kafka) for all asynchronous communication between backend microservices.
- **Considered Options**:
  - *Option 1: Synchronous HTTP/REST calls between services.* Rejected due to tight coupling and the risk of cascading failures; if the inventory service is offline, the transaction is lost.
  - *Option 2: Monolithic MVC backend.* Rejected because the compute requirements for game servers scale differently than web/transactional services.
- **Consequences**:
  - *Pros:* High fault tolerance and guaranteed message delivery (up to configured retention periods). Game servers are completely decoupled from transactional infrastructure.
  - *Cons:* Significant operational overhead to orchestrate, deploy, and maintain a highly available message broker cluster.
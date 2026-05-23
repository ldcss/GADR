# [ADR-005] Event-Driven Microservices Architecture for Backend Systems
- **Status**: Accepted
- **Context**: The game requires out-of-match services such as cross-region account synchronization, inventory management, and marketplace transactions. These systems must be highly available, fault-tolerant, and capable of handling temporary service outages without data loss.
- **Decision**: Adopt an Event-Driven Architecture utilizing Apache Kafka as the central message broker for asynchronous backend microservice communication.
- **Considered Options**:
  - *Direct Synchronous HTTP/REST (MVC without a broker)*: Rejected. If a downstream service (e.g., inventory) goes offline during a transaction, the request fails and data is lost.
  - *Monolithic Architecture*: Rejected. Lacks the scalability required to support multiple physical server regions (e.g., São Paulo, US) sharing persistent player accounts.
- **Consequences**:
  - **Pros**: High resilience and fault tolerance. Kafka can retain unacknowledged messages for up to 7 days, allowing microservices to process backlogs upon recovery. Decouples systems like payment processing and inventory management.
  - **Cons**: Introduces high infrastructure complexity. Requires strict orchestration and event choreographing to ensure events (like deducting funds and adding inventory) are processed in the correct sequential order.
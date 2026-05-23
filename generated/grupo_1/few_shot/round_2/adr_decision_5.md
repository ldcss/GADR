# [ADR-005] Event-Driven Architecture for Global Backend Services
- **Status**: Accepted
- **Context**: Out-of-match services—such as cross-region player profiles, inventory updates, and marketplace transactions—need to reliably sync across multiple global server locations (e.g., US, São Paulo). 
- **Decision**: Utilize an Event-Driven Architecture leveraging a robust Message Broker (e.g., Apache Kafka) to handle inter-service communication and global persistence.
- **Considered Options**:
  - *Option 1: Synchronous HTTP/REST Microservices.* Rejected because if the inventory service goes down, a checkout service calling it synchronously will also fail, leading to cascaded system outages and lost state.
  - *Option 2: Monolithic MVC Backend.* Rejected because a centralized monolith cannot efficiently handle distributed cross-region roaming (e.g., a player moving their profile from Brazil to Japan) without massive latency.
- **Consequences**:
  - *Pros:* Excellent fault tolerance. If a service goes offline, the broker will retain messages (up to 7 days) until the service recovers and processes the queue, preventing data loss. Allows decoupling of account roaming and inventory systems.
  - *Cons:* Requires dedicated infrastructure orchestration and introduces eventual consistency, meaning players might experience slight delays in profile synchronization when switching global regions.
# [ADR-003] High-Performance Distributed Caching Layer
- **Status**: Accepted
- **Context**: To meet the strict sub-3-second SLA for user identification and workout retrieval, the system must avoid heavy I/O operations and repetitive database queries during peak hours (e.g., Saturday mornings when hundreds of machines are active). Furthermore, the chosen message broker (BullMQ) requires a compatible backend.
- **Decision**: Deploy Redis (via AWS ElastiCache) to serve as a high-performance distributed caching layer for user data and as the underlying storage mechanism for the BullMQ message broker.
- **Considered Options**:
  - **Direct Database Queries**: Rejected. Relying solely on the primary database for repetitive data retrieval during peak loads poses a significant risk of I/O bottlenecks and SLA violations.
  - **In-Memory Application Caching (e.g., Node.js local cache)**: Rejected. Since the compute layer is horizontally scaled across EKS pods, local in-memory caching would lead to data inconsistency and cache misses across distributed instances.
- **Consequences**:
  - **Pros**: Drastically reduces data retrieval latency by fetching pre-loaded user data from memory. Serves a dual architectural purpose by supporting both the application cache and the message broker backend, streamlining infrastructure provisioning.
  - **Cons**: Introduces additional infrastructure costs (AWS ElastiCache). The engineering team must design and implement robust cache invalidation strategies to ensure data consistency between the cache and the primary database.
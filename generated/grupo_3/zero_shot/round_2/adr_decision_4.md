# [ADR-004] Caching Strategy for Low-Latency Authentication
- **Status**: Accepted
- **Context**: The system must authenticate the user via QR code, load their workout, and display the session in under 3 seconds. Relying solely on relational database queries during peak hours poses a significant risk to this latency requirement.
- **Decision**: We will implement Amazon ElastiCache (Redis) to proactively cache user workout data based on anticipated demand (e.g., historical attendance patterns and schedules).
- **Considered Options**:
  - **On-Demand Database Queries**: Rejected. Fetching complex workout structures directly from the primary database for hundreds of simultaneous users will exceed the 3-second SLA due to I/O bottlenecks.
  - **In-Memory Application Cache**: Rejected. In-memory caches are ephemeral and do not share state across the horizontally scaled Kubernetes pods.
- **Consequences**:
  - **Pros**: Drastically reduces read latency, ensures the 3-second SLA is met even at peak times, and shares infrastructure with our message broker (BullMQ).
  - **Cons**: Requires the implementation of proactive cache warming scripts, cache invalidation policies, and additional memory monitoring on ElastiCache.
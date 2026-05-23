# [ADR-003] Distributed Caching Strategy using Redis (AWS ElastiCache)
- **Status**: Accepted
- **Context**: The system has a strict requirement to authenticate users, load their workouts, and display the session in under 3 seconds. To achieve this during high-demand periods (e.g., Saturday mornings), the system needs to preemptively stage and quickly serve frequently accessed student data.
- **Decision**: We will use Redis, deployed via AWS ElastiCache, as our distributed caching layer. We will implement demand-based caching policies to pre-load student workouts based on expected attendance. Redis will also serve as the required backing datastore for BullMQ.
- **Considered Options**:
  - **Direct Database Lookups (No Cache)**: Rejected because disk-based DB queries cannot guarantee the < 3-second SLA under heavy concurrent load across hundreds of active machines.
  - **In-Memory Application Cache (e.g., Node.js memory)**: Rejected because the backend will be horizontally scaled across multiple pods in EKS; local state would lead to cache misses and inconsistent performance.
- **Consequences**:
  - **Pros**: Drastically reduces data retrieval latency; shares infrastructure with the message broker (BullMQ natively relies on Redis), optimizing resource usage.
  - **Cons**: Adds complexity around cache invalidation (ensuring workout updates reflect immediately at the equipment terminal); increases baseline infrastructure costs due to continuous ElastiCache uptime requirements.
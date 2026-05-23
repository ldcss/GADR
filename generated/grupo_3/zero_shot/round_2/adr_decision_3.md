# [ADR-003] Asynchronous Event Processing and Message Brokering
- **Status**: Accepted
- **Context**: Each gym machine acts as an autonomous node, sending real-time execution telemetry and sensor data. If the backend processes this heavy ingestion synchronously, it risks blocking core functions, thereby violating the strict 3-second SLA for user authentication and workout loading.
- **Decision**: We will implement a Message Broker architecture using BullMQ backed by Redis (via Amazon ElastiCache) to decouple sensor event ingestion from core API processing. We will partition processing by dedicating specific worker queues per gym.
- **Considered Options**:
  - **Synchronous API Processing**: Rejected. Directly processing telemetry payloads would consume API threads, creating bottlenecks during peak hours and impacting user identification latency.
  - **AWS SQS**: Rejected in favor of BullMQ due to the planned caching strategy, which already requires Redis. BullMQ allows us to consolidate our tech stack around Redis for both caching and queuing.
- **Consequences**:
  - **Pros**: Protects the core authentication and workout-loading APIs from telemetry spikes. Grouping queues per gym isolates workloads and prevents a single busy gym from degrading the entire network.
  - **Cons**: Introduces eventual consistency for telemetry data and requires managing background worker processes.
# [ADR-002] Asynchronous Processing and Caching Strategy
- **Status**: Accepted
- **Context**: Gym equipment functions as autonomous nodes generating a high volume of real-time monitoring and sensor data. Processing this data synchronously alongside student authentication and workout retrieval would overwhelm the central servers, causing severe latency spikes and violating the 3-second response time SLA during peak hours.
- **Decision**: Implement BullMQ backed by Redis (via AWS ElastiCache) to serve as both the message broker and caching layer. Data processing will be decoupled using dedicated queues segregated by gym location.
- **Considered Options**:
  - *Option 1: Synchronous API Processing.* Rejected because directly handling sensor telemetry on the main thread would block core features, leading to system bottlenecks and authentication timeouts during high-concurrency periods.
  - *Option 2: On-the-fly Database Queries for Workouts.* Rejected. Fetching training data directly from a relational database upon every QR code scan cannot guarantee the <3s SLA under heavy load.
- **Consequences**:
  - *Pros:* Decouples heavy sensor data ingestion from the user authentication flow; prevents server CPU bottlenecks by distributing load across background workers; enables proactive caching of student training data based on attendance patterns, drastically reducing database read operations.
  - *Cons:* Increases infrastructure complexity by introducing stateful caching and queue management components; requires careful configuration of Redis memory limits and worker concurrency settings to prevent queue flooding.
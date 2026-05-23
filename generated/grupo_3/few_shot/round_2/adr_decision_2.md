# [ADR-002] BullMQ and Tenant-Specific Queues for Sensor Data Ingestion
- **Status**: Accepted
- **Context**: Gym machines act as autonomous nodes streaming continuous sensor data regarding exercise execution. Processing this telemetry synchronously would bottleneck the system and violate the strict Service Level Agreement (SLA) of authenticating and loading a user's workout in under 3 seconds.
- **Decision**: Utilize BullMQ as the message broker for asynchronous event ingestion, implementing a multi-tenant architecture where each gym location is assigned its own dedicated queue and worker pool.
- **Considered Options**:
  - *Option 1: Synchronous API calls for sensor data.* Rejected because the volume of monitoring data would saturate the backend and severely impact the latency of critical user-facing requests (e.g., QR authentication).
  - *Option 2: Single global message queue for all gyms.* Rejected because it introduces a "noisy neighbor" risk, where a peak usage spike in one large gym could delay event processing for all other clients.
- **Consequences**:
  - *Pros:* Fully decouples heavy sensor data ingestion from real-time user authentication; ensures workload isolation between different gym branches, preventing systemic bottlenecks.
  - *Cons:* Increases infrastructure complexity, requiring the management of dynamic worker scaling based on the number of active queues.
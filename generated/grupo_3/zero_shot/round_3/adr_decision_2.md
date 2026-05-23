# [ADR-002] Asynchronous Event Processing with BullMQ
- **Status**: Accepted
- **Context**: Gym equipment nodes continuously stream sensor events. Processing this telemetry synchronously alongside student authentication and workout loading would cause severe bottlenecks, violating the strict < 3-second SLA for user interactions at the machine terminals.
- **Decision**: We will implement BullMQ to act as a message broker. This will decouple the ingestion of sensor events from backend processing. We will partition processing by utilizing dedicated queues/workers per gym facility.
- **Considered Options**:
  - **Synchronous API Processing**: Rejected because heavy processing of sensor data during peak hours would directly impact the latency of critical user authentication and workout retrieval requests.
  - **Serverless Compute (Lambda triggers)**: Rejected due to the potential cost explosion of firing individual serverless functions for every continuous sensor event.
- **Consequences**:
  - **Pros**: Isolates critical path performance (user login/workout load) from background telemetry processing; prevents CPU starvation on API servers; tenant isolation (queues per gym) minimizes blast radius.
  - **Cons**: Introduces eventual consistency for real-time sensor monitoring; requires maintaining and scaling dedicated worker instances to process the queues.
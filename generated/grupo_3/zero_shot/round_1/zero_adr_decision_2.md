# [ADR-002] Asynchronous Event Processing and Message Brokering
- **Status**: Accepted
- **Context**: Gym equipment functions as IoT nodes generating a continuous stream of sensor events. Concurrently, users scanning QR codes expect system authentication and workout loading in under 3 seconds. Processing sensor telemetry synchronously during peak hours risks bottlenecking the API and violating the latency SLA.
- **Decision**: Implement BullMQ as a message broker to decouple sensor event ingestion from background processing, utilizing dedicated worker processes distributed by CPU.
- **Considered Options**:
  - **Synchronous API Processing**: Rejected. Processing heavy telemetry events on the same thread/request cycle as user authentication would block responses and easily exceed the 3-second latency threshold during peak hours.
  - **AWS Lambda for Event Processing**: Rejected. Firing a Lambda function for every sensor event was evaluated but discarded due to high cost implications at scale.
- **Consequences**:
  - **Pros**: Strictly decouples user-facing requests from heavy background processing. Allows for queue isolation (e.g., dedicating specific queues per gym or network) and mitigates CPU bottlenecks by controlling worker concurrency.
  - **Cons**: Increases architectural complexity by introducing asynchronous workflows. Requires a highly available Redis instance to persist the message queues.
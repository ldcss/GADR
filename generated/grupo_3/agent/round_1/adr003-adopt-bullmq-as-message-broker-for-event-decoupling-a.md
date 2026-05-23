# [ADR-003] Adopt BullMQ as Message Broker for Event Decoupling and Per-Gym Queues

**Date:** 2026-05-11

## Status
Accepted

## Context
The Gêntica platform is a gym management system where each weightlifting station acts as an autonomous network node. The system must meet strict efficiency attributes, specifically loading workouts and authenticating students within 3 seconds, even during peak hours with hundreds of active devices. 

Simultaneously, the system ingests high volumes of real-time monitoring and sensor data from these stations. Processing this event data synchronously risks bottlenecking the central servers, directly impacting the latency of critical user-facing operations (e.g., student identification). To ensure high availability and responsiveness, we must decouple heavy sensor event ingestion from core synchronous processing.

## Decision
We will adopt **BullMQ** as our persistent message broker to decouple sensor event ingestion from processing workflows. 

Technically, we will:
* Implement an asynchronous messaging architecture where student requests are handled via immediate APIs, while monitoring events are pushed to BullMQ.
* Utilize BullMQ’s group affinity features to implement **per-gym queues**. This allows us to assign dedicated workers per facility, isolating workloads and preventing cross-tenant bottlenecks.
* Leverage BullMQ's built-in rate-limiting and delayed job promotion to mitigate throughput spikes during peak gym hours.

## Considered Options
1. **Synchronous API Processing (No Message Broker):**
   * *Rationale for Rejection:* Fails to meet the 3-second latency SLA. High volumes of sensor data during peak hours would overwhelm server instances, degrading the primary user experience.
2. **On-Demand Ephemeral Compute (AWS Lambda per Event):**
   * *Rationale for Rejection:* While it provides infinite horizontal scaling, invoking a Lambda function directly for every incoming telemetry event would be cost-prohibitive. A messaging buffer is required to batch and control processing execution rates.

## Consequences

**Pros:**
* **Decoupling & Latency Protection:** Offloading sensor data ingestion to a queue ensures that student identification and workout loading remain under the 3-second threshold.
* **Tenant Isolation:** BullMQ’s group affinity enables distinct per-gym queues, ensuring that a surge in traffic at one gym does not impact the processing of another.
* **Bottleneck Mitigation:** Built-in rate limiting and worker-per-CPU configuration stabilize server loads and prevent instance overload during concurrent peak usage.
* **Cost Efficiency:** Replaces the need for expensive per-request serverless scaling with a predictable, queue-driven worker pool.

**Cons:**
* **Architectural Complexity:** Introduces asynchronous processing logic, requiring robust handling for failed jobs, retries, and eventual consistency.
* **Infrastructure Dependency:** BullMQ requires a highly available Redis instance (e.g., AWS ElastiCache) to function as its backing store, adding a stateful component to the infrastructure maintenance scope.
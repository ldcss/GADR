# [ADR-003] Adopt BullMQ with AWS ElastiCache for Queue-Based Processing over AWS Lambda

**Date:** 2026-05-22

## Status
Accepted

## Context
The gym management system requires high availability and efficiency, specifically authenticating and loading student workouts within 3 seconds during peak hours across hundreds of simultaneous, autonomous equipment nodes. To prevent monitoring data volume from impacting student identification latency, event ingestion must be decoupled from processing. Auto-scaling is necessary to handle demand spikes. While serverless functions provide immediate scaling, the continuous high-throughput nature of this system raises severe cost and performance concerns.

## Considered Options
* **AWS Lambda (Serverless):** Rejected. While offering out-of-the-box ephemeral scaling, the per-execution cost model becomes prohibitively expensive under heavy, continuous load. Additionally, Lambda's inherent technical constraints, such as cold starts, jeopardize the strict 3-second response time SLA.
* **BullMQ with AWS ElastiCache (Redis):** Accepted. A managed, queue-based worker model allows us to control concurrency, decouple processing, and predictably manage infrastructure costs.

## Decision
We will reject AWS Lambda (serverless) for auto-scaling due to high cost and latency concerns. Instead, we will implement a queue-based worker model using BullMQ. 

AWS ElastiCache (Redis) will be utilized to back BullMQ, acting as the message broker, controlling concurrency, and caching student data on demand. Processing will be divided by queues (e.g., isolated per gym) and executed via workers scaled to CPU availability to mitigate bottlenecks and ensure immediate system responses.

## Consequences

**Pros:**
* **Cost Predictability:** Avoids the unbounded per-execution costs of the serverless compute model under heavy continuous loads.
* **Performance SLA:** Eliminates Lambda cold starts, ensuring the system meets the 3-second latency requirement for student identification.
* **Efficient Resource Utilization:** Leverages a worker-per-CPU model and enables on-demand student data caching directly via ElastiCache.
* **Bottleneck Mitigation:** Queues decouple sensor event ingestion from core processing, preventing system overload during peak gym hours.

**Cons:**
* **Infrastructure Management:** Unlike fully serverless solutions, AWS ElastiCache is a managed service that requires capacity planning and infrastructure provisioning.
* **Operational Complexity:** Introduces the need to manage Redis clusters, configure BullMQ concurrency rules, and manage worker node scaling mechanisms (e.g., via Kubernetes/EKS).
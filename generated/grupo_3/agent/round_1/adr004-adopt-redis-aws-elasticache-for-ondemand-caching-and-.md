# [ADR-004] Adopt Redis (AWS ElastiCache) for On-Demand Caching and Queue Integration

**Date:** 2026-05-11

## Status
Accepted

## Context
The Gêntica gym management system requires high availability and extreme efficiency. When a student identifies themselves via QR Code at a weightlifting station, the system must authenticate, load the workout, and display the session within 3 seconds. During peak hours, hundreds of devices will be active simultaneously. Additionally, the high volume of sensor event ingestion from the equipment must be decoupled from the main processing to avoid impacting student identification latency. To meet these performance SLAs, we require an ultra-fast caching layer and a reliable backend store for our message broker. 

## Decision
We will adopt Redis, managed via AWS ElastiCache, to serve as our primary in-memory data store. We will use Redis to:
1. Cache student workout data on demand based on their expected gym attendance days.
2. Act as the underlying storage mechanism for our message broker (BullMQ) to decouple sensor event ingestion from main API requests.

## Considered Options
* **Self-hosted Redis on Amazon EC2:** Rejected. Managing infrastructure manually adds significant operational overhead (provisioning, OS patching, failover, and node replacement) that distracts from core product development.
* **Amazon DynamoDB (or standard RDBMS) for Caching:** Rejected. While highly available, disk-based databases cannot guarantee the sub-millisecond latency required to reliably meet the 3-second end-to-end response SLA under heavy concurrent load, nor do they natively support BullMQ integrations.

## Consequences

**Pros:**
* **Sub-Millisecond Latency:** Redis delivers the high performance necessary to easily meet the 3-second equipment response requirement.
* **Fully Managed Infrastructure:** AWS ElastiCache automatically handles OS patching, failure detection, and node replacements, significantly reducing DevOps burden.
* **Scalability:** Supports Serverless deployments for automatic scaling based on workload demands, or cluster setups with up to 5 read replicas for read distribution and failover during peak gym hours.
* **Queue Decoupling:** Provides out-of-the-box compatibility with BullMQ, enabling efficient decoupling of heavy monitoring/sensor data from immediate student identification requests.

**Cons:**
* **Data Volatility:** Because Redis is entirely in-memory, cached data is volatile. In the event of a total system failure, cached values are lost and must be re-fetched from the primary database upon recovery.
* **Operational Cost:** Managed in-memory instances incur constant runtime costs compared to ephemeral compute solutions, requiring strict lifecycle policies (e.g., LRU eviction) to prevent unbounded memory growth and cost bloat.
# [ADR-002] Use AWS ElastiCache (Redis) for On-Demand Student Data Caching

**Date:** 2026-05-22

## Status
Accepted

## Context
The gym management system must operate with high availability and extreme efficiency. A core non-functional requirement dictates that when a student identifies themselves at an autonomous equipment node via QR code, the system must authenticate, load the workout, and display the session within 3 seconds. During peak hours, hundreds of pieces of equipment will be active simultaneously. Relying solely on direct database queries for every interaction will create processing bottlenecks and violate the 3-second latency SLA. The system requires a highly efficient caching layer to store frequently accessed student data and a message broker backend (BullMQ) to decouple sensor event ingestion from processing. 

## Decision
We will use AWS ElastiCache (Redis) to cache student data by demand. Data will be cached based on expected gym attendance patterns to proactively serve high-traffic periods. We will configure a caching policy utilizing Time-To-Live (TTL) timeouts and Least Recently Used (LRU) eviction. Additionally, this Redis instance will serve as the backend for BullMQ to handle queue management and mitigate simultaneous processing bottlenecks.

## Considered Options
* **AWS ElastiCache (Redis) (Selected):** Provides sub-millisecond latency, acts as a unified backend for both our application cache and BullMQ message broker, and removes infrastructure management overhead.
* **Self-Hosted Redis on EKS (Rejected):** While it provides the same caching capabilities, managing stateful workloads in Kubernetes introduces unnecessary operational overhead (provisioning, patching, and scaling) compared to a fully managed AWS service.
* **Direct Relational Database Queries / No Cache (Rejected):** Cannot guarantee the 3-second response time SLA during peak gym hours with hundreds of concurrent autonomous equipment nodes.

## Consequences

**Pros:**
* **High Performance:** Redis is heavily optimized for key/value pairs, significantly reducing system response times to meet the strict 3-second SLA.
* **Zero Operational Overhead:** As a fully managed infrastructure, AWS handles provisioning, setup, patching, and scaling.
* **Built-in Mechanisms:** Native support for TTL, cache miss handling, and LRU eviction simplifies the implementation of our on-demand caching policy.
* **Architectural Synergy:** Seamlessly integrates with BullMQ, providing both caching and message brokering through a single managed technology stack.

**Cons:**
* **Data Volatility:** Redis is an in-memory data store. In the event of a system failure, cached student data is lost, requiring the system to absorb a temporary latency hit to rebuild the cache from the primary database on demand.
* **LRU Eviction Trade-offs:** The LRU policy may prematurely purge rarely used, large, or hard-to-process data payloads during peak demand, necessitating expensive database recalculations when that data is requested again.
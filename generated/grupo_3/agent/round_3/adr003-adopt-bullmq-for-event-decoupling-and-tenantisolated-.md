# [ADR-003] Adopt BullMQ for Event Decoupling and Tenant-Isolated Queuing

**Date:** 2026-05-22

## Status
Accepted

## Context
The gym management system must authenticate users, load workouts, and display the session on IoT equipment within a strict 3-second SLA. During peak hours, hundreds of pieces of equipment are active simultaneously, generating a high volume of monitoring and sensor data. Processing these events synchronously overloads the core application servers, bottlenecking identification latency. We require a mechanism to decouple event ingestion from core processing and isolate workloads per gym facility to prevent noisy-neighbor issues. 

## Decision
We will adopt BullMQ as our primary message broker, running on top of AWS ElastiCache (Redis). We will implement a tenant-isolated queue topology by assigning a dedicated queue to each gym facility, utilizing Node.js background workers (allocated per CPU core) to process decoupled sensor events asynchronously.

## Considered Options
* **AWS Lambda (Synchronous/Direct Triggers):** Rejected. While auto-scaling is seamless, spinning up ephemeral instances for continuous, high-volume sensor event ingestion would be highly cost-inefficient and does not natively smooth out peak concurrency spikes.
* **Traditional Message Brokers (e.g., RabbitMQ):** Rejected. While fully featured, introducing a standalone message broker adds unnecessary infrastructure overhead. BullMQ leverages our planned Redis caching layer (AWS ElastiCache), simplifying deployment while natively supporting our specific queue-per-tenant requirements.

## Consequences

**Pros:**
* **High Throughput:** Built on Redis, BullMQ achieves maximum throughput by utilizing efficient Lua scripts and pipelining.
* **Peak Load Smoothing:** Effectively offloads heavy sensor workloads from the main server, mitigating processing bottlenecks during peak simultaneous usage.
* **Tenant Isolation:** Natively supports isolated job processing per gym facility, ensuring heavy utilization by one gym does not degrade latency for others.
* **Reliability:** Enforces "at least once" delivery semantics (aiming for "exactly once"), ensuring robust communication and no loss of workout history or sensor data upon reconnection.

**Cons:**
* **Narrower Consumer Scope:** BullMQ is highly effective for isolated queuing but lacks advanced built-in routing mechanisms for pub/sub scenarios where multiple independent services must consume the exact same event simultaneously.
* **Redis Dependency:** Tightly couples the messaging infrastructure to Redis, requiring strict memory management and eviction policies to ensure queues do not exhaust ElastiCache resources.
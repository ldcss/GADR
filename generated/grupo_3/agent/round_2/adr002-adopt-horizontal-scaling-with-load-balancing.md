# [ADR-002] Adopt Horizontal Scaling with Load Balancing

**Date:** 2026-05-22

## Status
Accepted

## Context
The gym management platform requires strict high availability during operational hours and efficient processing, mandating sub-3-second response times for user authentication and session loads. The system experiences unpredictable traffic spikes with hundreds of autonomous equipment nodes synchronizing simultaneously. To prevent bottlenecks and infrastructure failures, a scalable architecture is required to handle high-demand periods without service degradation.

## Decision
We will adopt a Horizontal Scaling strategy paired with a Load Balancer over Vertical Scaling. This setup will be orchestrated using AWS EKS (Kubernetes) to dynamically distribute capacity and ensure high availability across the network.

## Considered Options
* **Horizontal Scaling with Load Balancer (Accepted):** Multiplies service instances and distributes requests to handle peak loads. Supports massive growth and avoids single points of failure.
* **Vertical Scaling (Rejected):** Increasing individual machine capacity. While simpler to implement initially, it is bound by strict hardware limitations, incurs higher long-term costs, and cannot provide the required fault tolerance for high availability.

## Consequences
**Pros:**
* **High Availability:** Ensures the system remains reliable and handles increased user load without crashing during peak usage.
* **Traffic Spike Mitigation:** Dynamically clustered load balancers keep applications running smoothly during unpredictable demand surges.
* **Long-Term Viability:** Supports massive growth by allowing seamless, dynamic addition of servers to the infrastructure.

**Cons:**
* **Architectural Complexity:** Introduces the need for complex infrastructure clustering and advanced container orchestration (Kubernetes).
* **Operational Overhead:** Requires careful planning for distributed state management, deployment pipelines, and observability.
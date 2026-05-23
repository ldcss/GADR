# [ADR-001] Selection of AWS as the Primary Cloud Platform

**Date:** 2026-05-11

## Status
Accepted

## Context
The Gêntica gym management system requires high availability (uninterrupted operation during gym hours via active redundancy) and strict efficiency (sub-3-second response time for student QR code authentication and workout loading during peak hours). To achieve this, the architecture requires robust horizontal auto-scaling, load balancing, caching, and message brokering (decoupling sensor ingestion from processing). We must select a cloud provider that natively supports these infrastructure requirements while minimizing the team's learning curve and operational friction.

## Decision
We will use Amazon Web Services (AWS) as our primary cloud platform. 

To support the system's availability and efficiency requirements, the initial deployment will leverage AWS's managed infrastructure, specifically:
*   **Amazon EKS (Kubernetes):** Selected over AWS ECS as the primary container orchestrator due to the Tech Lead's extensive pre-existing experience, ensuring faster and more reliable deployment.
*   **AWS Application Load Balancers:** For horizontal scaling and distributing traffic across instances.
*   **Amazon ElastiCache (Redis):** Integrated with BullMQ to handle queueing and cache student workout data on demand, preventing database bottlenecks during peak hours.

## Considered Options
*   **AWS (Selected):** Chosen for its massive industry adoption, pre-existing team expertise, and extensive community troubleshooting resources. It easily handles the full lifecycle environment needs (Dev, Staging, Prod) and provides infinite server capacity for peak scale.
*   **Microsoft Azure / Google Cloud Platform:** Rejected. While both provide comparable PaaS/IaaS capabilities for horizontal scaling and load balancing, the team lacks deep familiarity with them. Choosing either would introduce an unnecessary learning curve and delay time-to-market.
*   **On-Premises Server Infrastructure:** Rejected. Fails to provide dynamic horizontal auto-scaling capabilities necessary to handle peak gym hours efficiently without incurring prohibitive upfront hardware costs.

## Consequences

**Pros:**
*   **Reduced Learning Curve:** Pre-existing team experience with AWS (specifically EKS) allows for immediate architectural implementation.
*   **High Availability & Scalability:** AWS's native load balancers and auto-scaling capabilities ensure the system will remain operational and meet the sub-3-second latency SLA during peak loads.
*   **Community Support:** Widespread industry adoption guarantees a vast pool of shared knowledge and proven DevOps solutions for troubleshooting.

**Cons:**
*   **Cost Management:** Dynamic horizontal scaling and potential use of serverless/ephemeral compute (like Lambda) require strict monitoring to avoid unexpected cloud expenditures.
*   **Vendor Lock-in:** Relying heavily on AWS-managed services (like ElastiCache) creates tight coupling to the AWS ecosystem, complicating any future migrations.
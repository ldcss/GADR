# [ADR-001] Select AWS as Primary Cloud Provider

**Date:** 2026-05-22

## Status
Accepted

## Context
The genetic platform system is an AI-driven gym management solution where autonomous equipment nodes require real-time workout loading and execution monitoring. The system demands high availability (active redundancy, no downtime during gym hours) and high efficiency (sub-3-second response times during peak hours across hundreds of active nodes). 

To achieve this, the architecture requires horizontal auto-scaling, load balancing, decoupling via message brokers (e.g., BullMQ), and caching (e.g., Redis). We must select a cloud infrastructure provider capable of reliably supporting these distributed, high-demand workloads while offering managed services (like Kubernetes) that align with the team's existing expertise.

## Decision
We will use Amazon Web Services (AWS) as our primary cloud provider to host the central server and backend services. The infrastructure will heavily leverage AWS managed services, specifically Amazon EKS (Elastic Kubernetes Service) for container orchestration, Elastic Load Balancing, and Amazon ElastiCache for caching.

## Considered Options
* **Amazon Web Services (AWS) [Selected]:** Chosen due to unparalleled scalability, widespread enterprise adoption, and the team's direct expertise with AWS ecosystems (specifically EKS). 
* **Microsoft Azure / Google Cloud Platform [Rejected]:** While viable PaaS/Cloud alternatives, AWS was selected over them due to its larger market share, which translates to more extensive community knowledge, documentation, and troubleshooting resources available on the internet.
* **On-Premises Infrastructure [Rejected]:** Cannot dynamically scale horizontally to meet peak gym hours without expensive, permanent hardware over-provisioning. 

## Consequences

**Positive:**
* **Unparalleled Scalability:** AWS's battle-tested global infrastructure allows for seamless horizontal auto-scaling to maintain sub-3-second latencies during peak gym hours.
* **Extensive Service Offerings:** Natively supports our required architectural components, including managed Kubernetes (EKS) and managed Redis (ElastiCache), accelerating development.
* **Proven Reliability:** Built on Amazon's highly available back-end technology, fulfilling our strict active redundancy and uptime requirements.
* **Widespread Adoption:** The massive user base and enterprise awareness ensure rapid onboarding and issue resolution through community knowledge.
* **Team Alignment:** Aligns with the Tech Lead's existing experience deploying to EKS, reducing the learning curve compared to AWS ECS or alternative cloud orchestrators.

**Negative:**
* **Cost Management:** Dynamic scaling and managed services require rigorous monitoring. Unoptimized compute usage (e.g., over-provisioned EC2 instances or unmanaged Lambda sprawl) can lead to rapid cost escalation.
* **Vendor Lock-in:** Relying on AWS-specific managed services (ElastiCache, EKS integration) creates switching costs if a migration to another cloud provider is needed in the future.
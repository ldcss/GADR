# [ADR-002] Use AWS EKS for Container Orchestration and Horizontal Scaling

**Date:** 2026-05-11

## Status
Accepted

## Context
The Gêntica gym management system requires high availability and efficiency. The system must process user authentications and load customized workouts within 3 seconds during peak hours, handling hundreds of concurrent autonomous hardware nodes. To meet these demands, the architecture requires robust horizontal scaling, active redundancy, and load balancing. The team must select a container orchestration platform within AWS that aligns with the required scaling capabilities and the development team's existing expertise to ensure reliable delivery.

## Decision
We will use Kubernetes via Amazon EKS (Elastic Kubernetes Service) for container orchestration and horizontal scaling. EKS will manage our service instances behind a load balancer to ensure high availability and sub-3-second response times.

## Considered Options
*   **AWS ECS (Elastic Container Service):** Rejected. While ECS provides simplicity and deep AWS integration, the tech lead has no prior experience with it. Adopting ECS would introduce a learning curve and unnecessary delivery risk.
*   **AWS Lambda (Serverless):** Rejected. Although it provides on-demand scaling and mitigates idle costs, relying entirely on Lambda for core system processes introduces concerns regarding unpredictable costs at high scale and potential latency bottlenecks, unless heavily mitigated by complex messaging decoupling. 

## Consequences

**Pros:**
*   **Leverages Existing Expertise:** Fully utilizes the tech lead's prior Kubernetes experience, enabling rapid, risk-reduced deployment.
*   **Operational Offloading:** EKS provides a fully managed control plane, reducing infrastructure maintenance overhead.
*   **Industry Standard:** Aligns with the enterprise standard for microservices (93% industry adoption), ensuring portability and long-term viability.
*   **Ecosystem Compatibility:** Natively supports advanced cloud-native networking, horizontal pod auto-scaling, and integrations needed to meet our strict latency and availability SLAs.

**Cons:**
*   **Operational Complexity:** EKS inherently carries a steeper learning curve and configuration complexity for newer team members compared to AWS ECS.
*   **Baseline Cost:** Unlike a purely serverless (Lambda) approach, running EKS nodes incurs continuous baseline infrastructure costs, even during off-peak hours.
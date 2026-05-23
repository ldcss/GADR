# [ADR-004] Adopt Amazon EKS for Container Orchestration

**Date:** 2026-05-22

## Status
Accepted

## Context
The genetic platform system (gym management software) requires highly available and efficient backend services to support real-time integrations with autonomous gym equipment. To achieve sub-3-second response times during peak hours, the system requires robust horizontal auto-scaling, load balancing, and active redundancy. We must select a container orchestration platform on AWS to manage these distributed services. The architectural team must balance platform complexity with operational readiness, factoring in the tech lead's extensive background with Kubernetes and lack of experience with AWS-native orchestrators.

## Decision
We will use Amazon EKS (Elastic Kubernetes Service) over native AWS ECS for container orchestration. This decision is primarily driven by the tech lead's deep, existing expertise with Kubernetes. 

## Considered Options
*   **Amazon EKS (Elastic Kubernetes Service):** *Selected.* Offers a fully managed Kubernetes control plane. It provides the advanced flexibility required for complex scaling while directly leveraging the tech lead's prior experience.
*   **AWS ECS (Elastic Container Service):** *Rejected.* While simpler to use and natively integrated into AWS, it comes at the expense of orchestration flexibility. More importantly, selecting ECS would introduce a significant learning curve for the tech lead, risking deployment velocity.

## Consequences

**Positive:**
*   **Immediate Productivity (Tooling Compatibility):** The team can use the exact same tooling, APIs, and manifests found across the open-source Kubernetes ecosystem without a learning curve.
*   **Advanced Flexibility:** EKS delivers the granular control and flexibility required for the complex horizontal scaling and high-availability demands of our hardware-integrated nodes.
*   **Reduced Operational Burden:** EKS removes the need to manually manage and maintain the underlying Kubernetes control plane infrastructure.
*   **Industry Standardization:** Kubernetes is the dominant enterprise standard (used by ~93% of organizations), ensuring we build on a highly transferable and universally adopted platform.
*   **Security Integration:** EKS tightly integrates with AWS IAM and SSO, allowing secure credential generation via AWS permissions rather than static secret files.

**Negative:**
*   **Inherent Complexity:** Kubernetes introduces a steeper platform complexity and configuration overhead compared to the simplicity of native AWS ECS.
*   **Baseline Costs:** The EKS managed control plane incurs a fixed hourly baseline cost that native ECS avoids.
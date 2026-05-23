# [ADR-001] Adopt AWS EKS for Container Orchestration

**Date:** 2026-05-22

## Status
Accepted

## Context
The gym management platform requires high availability and efficiency (<3 seconds response latency) to support real-time workout monitoring via IoT equipment nodes. The system must handle intense peak hours with hundreds of simultaneously active machines, requiring dynamic horizontal scaling and load balancing. We need a compute infrastructure capable of reliably orchestrating containerized workloads, managing auto-scaling efficiently, and optimizing infrastructure costs without sacrificing the team's operational agility. 

## Decision
We will use AWS as our primary cloud provider and Amazon Elastic Kubernetes Service (EKS) for container orchestration and horizontal scaling. We will manage worker node groups via EC2 instances in autoscaling groups to handle load distribution.

## Considered Options
* **AWS Lambda (Serverless):** Rejected. While ephemeral and highly scalable per request, the sustained volume of high-concurrency IoT monitoring data during peak gym hours would result in prohibitively high compute costs. 
* **Amazon ECS (Elastic Container Service):** Rejected. Although it is AWS's native, operationally simpler alternative to Kubernetes, the tech lead has deep expertise exclusively with EKS. Adopting ECS would introduce unnecessary learning curves and deployment risks.

## Consequences

**Pros:**
* **Accelerated Delivery:** Aligns directly with the tech lead's established expertise in Kubernetes and EKS, minimizing the team's learning curve.
* **Robust Horizontal Scaling:** EKS supports robust horizontal scaling using managed/self-managed EC2 worker nodes and auto-scaling groups, effectively handling peak gym traffic.
* **Streamlined Security:** Kubernetes cluster credentials integrate directly with AWS IAM and SSO, simplifying access management and employee off-boarding.
* **Ecosystem Flexibility:** Provides a well-defined integration framework using maintained Terraform modules and avoids vendor lock-in to default AWS-provisioned container tooling.
* **Standardization:** Enables centralized cluster management and establishes a standard infrastructure deployment pattern for all Dockerized applications.

**Cons:**
* **Operational Complexity:** EKS introduces a steeper operational burden and Kubernetes complexity compared to simpler managed services like ECS or Lambda.
* **Baseline Compute Costs:** Unlike serverless functions, maintaining EKS worker nodes requires always-on EC2 instances, incurring baseline costs even during off-peak gym hours.
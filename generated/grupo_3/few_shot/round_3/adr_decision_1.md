# [ADR-001] Container Orchestration using AWS EKS
- **Status**: Accepted
- **Context**: The gym management system requires high availability and horizontal scaling to handle peak hours across multiple gym locations simultaneously. The architecture must support distributed services and load balancing to ensure system resilience and maintain a strict sub-3-second response time for student authentication. 
- **Decision**: Deploy the core backend services using Kubernetes, specifically managed via Amazon EKS (Elastic Kubernetes Service).
- **Considered Options**:
  - *Option 1: AWS ECS (Elastic Container Service).* Rejected. Although it is the native AWS container orchestrator, the team lacks operational experience with it. Adopting ECS would introduce an unnecessary learning curve and deployment risk compared to the team's established proficiency with Kubernetes.
  - *Option 2: AWS Lambda (Serverless Architecture).* Considered for its cost-efficiency and per-request scaling capabilities. Rejected as the primary compute platform because the system requires long-running worker processes to handle message queues and hardware sensor integrations, which are better suited for a persistent containerized cluster rather than ephemeral 15-minute functions.
- **Consequences**:
  - *Pros:* High availability through horizontal pod auto-scaling; aligns seamlessly with the team's existing technical expertise, reducing time-to-market; provides a robust ecosystem for managing microservices and workers.
  - *Cons:* Higher baseline operational cost compared to a purely serverless approach due to always-on worker nodes; requires ongoing Kubernetes cluster maintenance and configuration management.
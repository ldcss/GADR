# [ADR-001] AWS Cloud Infrastructure and EKS for Container Orchestration
- **Status**: Accepted
- **Context**: The gym management platform requires high availability during operating hours and dynamic horizontal scaling to handle peak concurrent loads across multiple gym chains. The system must process real-time interactions from QR-code-enabled workout machines seamlessly.
- **Decision**: Deploy the core backend on AWS using Elastic Kubernetes Service (EKS) combined with an application load balancer to handle horizontal scaling and redundancy.
- **Considered Options**:
  - *Option 1: Pure Serverless Architecture (AWS Lambda).* Rejected because, despite scaling perfectly on demand, the continuous volume of workout sessions and active connections would make Lambda highly cost-prohibitive.
  - *Option 2: AWS ECS (Elastic Container Service).* Rejected because the engineering team and tech lead have extensive prior operational experience with Kubernetes (EKS) and zero experience with ECS, making EKS a safer and faster choice for deployment.
- **Consequences**:
  - *Pros:* Guarantees high availability through active redundancy and horizontal pod autoscaling; leverages existing team expertise, reducing time-to-market.
  - *Cons:* EKS introduces a higher baseline infrastructure cost and greater cluster management complexity compared to managed serverless functions.
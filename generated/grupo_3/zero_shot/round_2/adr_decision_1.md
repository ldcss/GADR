# [ADR-001] Cloud Provider Selection 
- **Status**: Accepted
- **Context**: The gym management platform requires a highly available and efficient infrastructure to handle simultaneous connections from hundreds of autonomous gym equipment nodes. The system must ensure zero downtime during gym operating hours and provide a robust ecosystem for load balancing, auto-scaling, and managed services.
- **Decision**: We will use Amazon Web Services (AWS) as our primary cloud provider.
- **Considered Options**: 
  - **Microsoft Azure**: Rejected. While capable, the team noted a stronger community presence, wider industry adoption, and deeper internal familiarity with AWS documentation and services.
  - **On-Premise Infrastructure**: Rejected. It cannot provide the required elasticity for peak hours or the native geographic redundancy needed for a multi-gym network.
- **Consequences**: 
  - **Pros**: Access to mature managed services (EKS, ElastiCache, Load Balancers), robust auto-scaling capabilities, and extensive community support.
  - **Cons**: Vendor lock-in to the AWS ecosystem.
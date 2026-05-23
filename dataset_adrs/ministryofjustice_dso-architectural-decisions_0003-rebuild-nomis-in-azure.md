# ADR-003. Continue to rebuild NOMIS in Azure

Date: 11/10/2019

## Status

Accepted

## Context

Since the initial decision to rebuild NOMIS and the Fix & Go infrastructure in Azure we have learned a few things and come to reevaluate our choice. Some context:

- NOMIS, OASys, CAFM, and the rest of Fix & Go resides in Azure under the control and maintenance of the DSO team.
- Database, WebLogic and application installation and management is provided by the Sheffield Studio DBA team.
- Fix & Go has network connectivity to a few key environments, particularly the Quantum network and PSN.
- Uncertainty around IR35 status and contractual renegotiations, as well as a shift in team focus and priorities means we have lost several members of the team. Unfortunately there's a reasonable chance we'll lose more people in the next few months.
- The Delius migration is now live, so the infrastructure code is tested and used in production. 
- Robin helped deliver the Delius DevOps tooling, and has deep knowledge of how it works and where it could benefit us.
- Recent spikes demonstrated that:
  + We can spin up an environment in AWS very quickly – within 3 days we had automated builds and deployment for a simple Oracle/WebLogic stack. While NOMIS wasn't functional (Oracle Forms still needs to be built regardless of AWS/Azure), the supporting infrastructure was "production quality".
  + The Packer images and Ansible is largely reusable in Azure – again with a few days we had a simple Oracle/WebLogic stack, albeit without the production-quality supporting infrastructure and networking. The Terraform configurations would need to be rewritten for Azure, as they are provider-specific.
  + While NOMIS closely resembles a portion of Delius, the latter is significantly more complex.

## Decision

We will continue to build in Azure, and lean more heavily on Azure's native offerings to offset some of the cost of _not_ using the Delius team's AWS code.

This decision is based on a couple of things (as well as the million more nuanced things):

1. Reducing the risk of knowledge silos, knowledge loss (bus/lottery factor), and lowering the barrier to entry for new team members is really important given the current challenges around IR35 and the makeup of our team. Adding a new cloud provider increases the complexity of our systems, even with the potential support we could get from the Delius migration team.
2. Reducing our time to deliver DR in production. We already have network connectivity to Quantum, remote desktop infrastructure, etc. in Azure, and replicating sufficient services in AWS to allow a migration of production is likely to be a significant undertaking involving a number of external stateholders.

## Consequences

- There is a lower barrier for new starters and risk of knowledge loss in the short-term.
- There will be fewer disparate systems in the short-term.
- It will take us longer to rebuild the aspects of the Delius system we like. We believe most of the Packer build and Ansible configuration will be portable with some changes, but the Terraform will need to be almost entirely rewritten.
- We should follow the architectural patterns of Delius unless we're compelled not to (for example to enforce boundaries of ownership). This will take more effort, particularly around the Terraform configurations.
- We cannot leverage AWS RDS for Oracle, but will investigate Oracle Cloud as an alternative in Azure.
- We will need to build either:
  1. an Azure AKS (or similar Kubernetes) to host production systems which need to be close to NOMIS/OASys (if latency between AWS/Azure proves to be a problem), or
  2. a VPN connection between Cloud Platform and our Azure estate to protect connections to various resources in Fix & Go.
- We will lean on Azure native SaaS offerings where possible (e.g. App Insights, Azure DevOps pipelines).
---
layout: layouts/adr.njk
title: "Terraform"
weight: 1
date: 2021-07-23
review_in: 12 months
tags:  
    - adr
    - tools
    - language
    - open_standards
    - testing
areas_of_coverage: ["Digital Service"]
status: "accepted"
contributors: ["John Nolan"]
adr_number: "0005"
---

## Context

We need a way to manage our infrastructure as code (IaC) to support CI/CD and manage and provision our computing, storage and networking resources in the cloud.

We use Terraform extensively on all our existing services, as well as a central Terraform repository for managing all our services resources, permissions and security needs.

## Technical

### Interoperability - How does this enable the exchange of information

Terraform is fully open source and has the ability to do Multi-Cloud Deployment.

Even though there is no plan to split our resources across multiple clouds, having this ability available is advantageous.

A downside of this being community driven means that new features created by cloud providers can sometimes have a delay in being available for use within Terraform.

### Developer Knowledge - How well known is this in our current skill sets

**Overall**: 7/10
We have dedicated Webops Engineers within our teams who have expert knowledge on using Terraform. They encourage others to learn and pair on the work they do.

Different teams have various levels of confidence in its use, but the ability to have a resource within each team with this knowledge makes up for any lack thereof.

### Support/Open Source - Is it well supported

Terraform is Open Source and regularly accepts and releases community based Pull Requests.

Some of our Webops Engineers are also contributors to the project.

### Scalability

Terraform by its nature is incredibly scalable. Enabling IaC, being maintained via Github and controlled via our CI/CD pipelines means it can be versioned, rolled back, monitored and maintained.

## Ethics

### Mitigate against being tech deterministic

N/A - there is no other non-tech solution that could give us the ability to manage our infrastructure.

### Ensure you conduct inclusive research

N/A - the use of this technology does not have an effect on marginalised groups directly.

### Think big and imagine what the impact of your work can be

Building our infrastructure in Terraform will allow us to take learnings and contribute back to wider society. If we develop new modules, add additional functionality to Terraform or raise issues that are found, we can help others who use this technology.

If we decide to Open Source our infrastructure code, we can also take advantage of contributions from other areas outside of our department.

Others will also be able to use our modules or infrastructure, should they wish, in their own implementations.

Working in the open will drive trust in Citizens and open ourselves up to honest debate and critique in our choices.

### Interrogate your data decisions

N/A - there is no place for personal data to be stored within Terraform.

It does enable the use of technologies that can and this analysis should be recorded against their own ADRs.

### Decision

We should continue to use Terraform taking advantage of our existing lessons learnt and best practices.

### Consequences

We will be able to take advantage of our existing best practices and knowledge to quickly setup any new infrastructure.

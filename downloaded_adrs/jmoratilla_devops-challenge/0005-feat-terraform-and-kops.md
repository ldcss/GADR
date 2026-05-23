# 5. feat_terraform_and_kops

Date: 2020-02-20

## Status

Draft

## Context

The kops template can be very useful to deploy clusters, but there are 
 situations where the cluster must be installed in already provisioned
 AWS resources.  Then, you can find lots of issues.

I have found an article about how to solve this issue by integrating
 terraform with kops in a very clever way.  I'm referencing the article
 here for future ideas.

* [Deploying Kubernetes clusters with kops and Terraform](https://medium.com/becnh-engineering/deploying-kubernetes-clusters-with-kops-and-terraform-832b89250e8e)

## Decision

I need to review and test the proposed solution before considerating it.

## Consequences

If applied, it could be great to manage current VPCs with new provisioned
 clusters.


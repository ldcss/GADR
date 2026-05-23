# 9. use terraform to provision Infrastruture as code

Date: 2020-05-26

## Status

Accepted

## Context

Since I moved to AWS EC2 I knew I had to implement Terraform to manage the
 infrastructure.

Why? Because for me it's the only tool I can use to provision for AWS.  Yes, 
 there is an alternative called AWS Cloudformation, but I prefer not to kill
 myself.

Terraform is very powerful, and I have worked with it before.

Terraform also implements a nice feature called remote state.  It allows me
 to share work with other users just sharing the credentials for the AWS.

Terraform allows me to create a big file with all the resources and
 progressively split it into different files to document better the solution.

Last, Terraform has a simple provision system that can help me to launch the
 configuration management solution after creating the instances.
 

## Decision

Implement Terraform to launch the infrastructure.

## Consequences

I have an issue with the 0.12.x versions as they have deprecated interpolation, 
 and I am having issues with it.  Rolling back to 0.11.x version solves the
 issue.
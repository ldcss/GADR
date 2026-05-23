[Home](../../README.md)


# 8. Deployment

Date: 2020-09-21

## Status

Accepted

## Context

We need a way to deploy our application to AWS.

## Decision

We will use [Terraform] to deploy our application. More specifically,
we will use [Chalice] to create the build artifact for the source
code (.zip) and then use [Terraform] to manage the infrastructure
resources.

👉 **Note:** Ideally, we would publish the build artifacts to S3 before
deployment. That way the deployment process could happen independently
of the build process.

👉 **Note:** To begin with, we'll just convert the JSON data created
by [Chalice] to [HCL] and add any other resources needed. Going forward,
we will use modules to create reusable components.


## Consequences

**Pros:**

* Can use [Terraform] to manage other infrastructure resources.
* Supports reusable modules
* Large community

**Cons:**

* Deployments can not be managed by [Chalice]

<br/>

[Previous](007-secrets.md)


[Chalice]: https://aws.github.io/chalice/
[Terraform]: https://www.terraform.io/
[HCL]: https://github.com/hashicorp/hcl/blob/hcl2/hclsyntax/spec.md

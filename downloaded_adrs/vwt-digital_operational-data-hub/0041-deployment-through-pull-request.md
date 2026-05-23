# 41. Deployment through Pull Request

Date: 2020-09-21

## Status

Accepted

Implements [6. Implement Security by Design](0006-implement-security-by-design.md)

Implements [4. Create software defined everything](0004-create-software-defined-everything.md)

Related to [49. gitops Deployment](0049-gitops-deployment.md)

## Context

Deployment of new software to the production environment should be done in a controlled way. The possibility of unauthorized deployment to production is a security vulnerability. Therefore, deployment is [automated](0049-gitops-deployment.md) in CI/CD pipelines. Next to that, a pull request with review procedure can be used to implement 4 eyes principle through review, either by peers or other functions.

## Decision

We will use pull requests to initiate a deployment of new software to production.

## Consequences

Using pull requests provides a controlled, auditable way of deploying software. It protects against malicious code being deployed. The review process delivers improves quality, at the cost of some overhead.

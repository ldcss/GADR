# 49. gitops Deployment

Date: 2020-09-21

## Status

Accepted

Implements [4. Create software defined everything](0004-create-software-defined-everything.md)

Related to [41. Deployment through Pull Request](0041-deployment-through-pull-request.md)

## Context

GitOps is a way of implementing Continuous Deployment for cloud native applications. It focuses on a developer-centric experience when operating infrastructure, by using tools developers are already familiar with, including Git and Continuous Deployment tools.

The core idea of GitOps is having a Git repository that always contains declarative descriptions of the infrastructure currently desired in the production environment and an automated process to make the production environment match the described state in the repository. If you want to deploy a new application or update an existing one, you only need to update the repository - the automated process handles everything else. It’s like having cruise control for managing your applications in production.

## Decision

All cloud objects are deployed using gitops processes. A push to the git repo will trigger a cloud build process which will install all needed objects

## Consequences

[Gitops](https://www.gitops.tech/)

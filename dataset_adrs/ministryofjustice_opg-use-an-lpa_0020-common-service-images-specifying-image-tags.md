# 20. Common service images - specifying image tags

Date: 2022-01-24

## Status

Accepted

## Context

UaL is moving toward a model of reusing code components as docker images. At this time new versions of common services will need to be tested before adoption.

We will need to explicitely define what immutable tag should be used.

## Decision

For common service docker images, we will,

- refer to immutable image tags in docker-compose.yaml for local development
- refer to immutable image tags in terraform.tfvars.json (local.environment.pdf_container_version) for AWS deployment with Terraform

## Consequences

Deploying different versions of a common service to AWS ECS will require edits to the terraform.tfvars.json file and a PR.

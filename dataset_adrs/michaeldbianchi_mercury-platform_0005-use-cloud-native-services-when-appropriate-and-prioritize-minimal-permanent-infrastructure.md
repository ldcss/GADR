# 5. Use cloud native services when appropriate and prioritize minimal permanent infrastructure

Date: 2020-05-17

## Status

Accepted

## Context

Mercury Platform intends to be a teaching platform as well as a financial data processing platform.

One core principle is to use the tools that are best suited for the needs and prioritizing modern DevOps best practices (immutable deployments, microservice architecture, etc).

There is also an additional need of keeping costs low while income is minimal or non-existant.

## Decision

The Mercury Platform will have minimal permanent infrastructure, prioritizing serverless tools when possible.

Containers will be used whenever possible to promote reliable deployments, cloud-agnostic services, and ease of local testing.

Cloud native services will be used when they meet needs and are cost-effective.

## Consequences

Developing processes and tooling for enterprise grade deployments and reliability requires significant time and investment. Fortunately, through the advancements of modern cloud providers and open-sourced tooling, this has become possible for individual developers and small teams.

We will sacrifice additional time and work at the beginning to establish patterns for CI, CD, and reliable and immutable runtimes that all fall within our budget.


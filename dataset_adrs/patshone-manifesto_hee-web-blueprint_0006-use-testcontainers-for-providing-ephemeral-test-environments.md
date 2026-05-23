---
layout: layouts/page.njk
title: ADR-0006 Use testcontainers for providing ephemeral test environments
pageTitle: ADR-0006 Use testcontainers for providing ephemeral test environments
pageDescription: We need to determine the platform on which infrastructure our acceptance tests will run.
path: /blueprint
permalink: /blueprint/adrs/ADR-0006-use-testcontainers-for-providing-ephemeral-test-environments.html
eleventyNavigation:
  parent: Architecture decisions
  key: ADR-0006 Use testcontainers for providing ephemeral test environments
  order: 6
---

# 6. Use testcontainers for providing ephemeral test environments

Date: 2020-03-30

## Status

Accepted

## Context

Having determined to use Gherkin and Selenide to manage the generation of our automated tests, we need to determine the platform on which these tests will run. The platform should be open source, if at all possible and portable between hosting platforms.

## Decision

We have determined to use the testcontainers.org project to manage the infrastructure for our automated tests. This platform provides a way of generically describing the containers that we use to run our tests and can be executed on platforms including Github Actions.

## Consequences

Choosing testcontainers.org provides a portable hosting platform agnostic way of describing the infrastructure required to execute our automated tests.
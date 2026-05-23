---
layout: layouts/page.njk
title: ADR-0003 Use github actions for automation
pageTitle: ADR-0003 Use github actions for automation
pageDescription: We should determine the platform we use to automate the build, test and deployment of the HEE National Website Platform.
path: /blueprint
permalink: /blueprint/adrs/ADR-0003-use-github-actions-for-automation.html
eleventyNavigation:
  parent: Architecture decisions
  key: ADR-0003 Use github actions for automation
  order: 3
---

# 3. Use github actions for automation

Date: 2020-03-09

## Status

Accepted

## Context

We should determine the platform we use to automate the build, test and deployment of the HEE National Website Platform.

## Decision

Having determined to use Github to manage the source code of the platform, the simplest answer to this question was to look at Github actions. We determined after some investigative work to prove out our ability to deploy to the BloomReach cloud that we should use Github Actions to manage platform automation.

## Consequences

Choosing Github actions reduces the number of organisations and platforms to orchestrate, however we did need to build and will need to maintain a brCloud deployment action.

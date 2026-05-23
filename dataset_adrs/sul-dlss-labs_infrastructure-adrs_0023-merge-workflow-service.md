---
layout: default
title: Template
nav_order: 26
permalink: records/0023
---
# Merge Worflow Service into DOR Services App

* Status: proposed
* Decider(s):
  * Infra team
  * Andrew Berger
  * Vivian Wong
* Date(s): <!-- required -->
  * Proposed: 2025-05-16

## Context and Problem Statement <!-- required -->

The goal of this architectural change is to merge the Workflow Server application into DSA.

The resulting implementation would be:

* Addition of a subset of the Worflow Server's API to DSA's API (primarily updating workflow status, checking workflow status, and creating workflows).
* Encapsulation of workflow logic within DSA (similar to other services, e.g., events and versions).
* Existing workflow database would continue to be used from DSA (using Rails multiple database support).

## Decision Drivers <!-- optional -->

* Maintainability
* Complexity
* Performance

## Considered Options <!-- required -->

* The proposal
* Do nothing
* A more substantial re-write of the workflow system

### Positive Consequences <!-- optional -->

* Reduced API calls: The vast majority of calls to the Workflow server are from DSA for indexing, which will be eliminated by this change. These calls add overhead and make SDR susceptible to network issues.
* Reduced reliance on RabbitMQ: The vast majority of RabbitMQ messages are to invoke indexing, which will be eliminated by this change.
* Improved DSA performance: Many DSA operations (e.g., getting version status) require calls to the Workflow server, which will be eliminated by this change. In turn, this will improve other applications, like the rendering of the dashboard in H3.

### Negative Consequences <!-- optional -->

* By not being a standalone application, insight into workflow operations may be diminished.

### Risks

* The change cannot be tested under load/scale in QA or stage environments.
* Managing a large monolith codebase may become increasingly challenging.

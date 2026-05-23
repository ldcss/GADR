# 4. Ownership of topics and queues

Date: 2018-02-22

## Status

Proposed

## Context

The `bus` is designed to decoupled projects from each other, rather than adding a many-to-many web of API calls.

The set of SNS topics should be very much stable as it contains published content types from the API.

Queue listeners are deployed with each interested project, and are the responsibility of each project to empty.

## Decision

Each project should own queues for the content types it consumes, while the topics should be owned by a global `bus` project.

## Consequences

Both topics and queues should be provided as infrastructure.

Queues should be created with each instance of a project.

Topic should only be created when a full new environment is created.

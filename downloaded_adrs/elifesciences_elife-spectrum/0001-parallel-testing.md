# 1. Tests should run in parallel

Date: 2017-09-07

## Status

Accepted

## Context

End2end tests are generally prone to have a long execution time, due to the number of different components involved, natural latency between different nodes and the amount of computation involved.

## Decision

We will execute all tests in parallel, with a fixed batch of workers.

## Consequences

Tests must be written so that they do not clash with each other: each test run must use different identifiers to avoid clashes. For example, every test involving publication of an article should generate a new article id.

We are able to run different tests at the same time even when the two test clients are one on the CI server and one on a local laptop, for ease of development.

# 9. Cloud function entrypoint

Date: 2021-03-24

## Status

Accepted

## Context

We feel the need to define a uniform way of setting entrypoints for Cloud Functions within the Google Cloud Platform

## Decision

- The entrypoint should have the same name as the function directory.
- The entrypoint name should be clear and descriptive.
- The entrypoint should be in `main.py`.
- The entrypoint should not contain business logic.

# 4. Use Airflow and Fargate

Date: 2020-06-05

## Status

Accepted

## Context

The ingest process will be a scheduled task and we have an Airflow instance designed for just this sort of thing.

## Decision

We will use Airflow to handle scheduling the ingest. The ingest process itself will be run inside a Fargate container.

## Consequences

The usual requirements for running a containerized application will apply. This includes treating the file system as ephemeral, writing all logs to stdout, and creating a CLI that is not interactive. In addition, to avoid unnecessary costs, we should strive to keep the application's memory bounded by using streaming throughout.

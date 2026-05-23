# 2. Use Luigi to build workflows from extract/transform/load tasks

Date: 2018-02-15

## Status

Accepted

## Context

Currently this project contains a single step in a single pipeline, which
extracts application error rates. The idea is to use a single metric
that we report on and automate the process end to end, as a proof of concept.

If this is scaled up to other metrics, we'll need some way of joining
up the individual tasks.

Note that we already have a lot of existing jobs that move data around, which are
implemented in different ways. For example:

- Scripts bundled with applications (eg https://github.com/alphagov/content-performance-manager)
- Scripts packaged on their own that do a single thing (eg https://github.com/alphagov/search-analytics)
- The data pipeline for auto-tagging content to the taxonomy (https://github.com/alphagov/govuk-taxonomy-supervised-learning)

These are monitored through a combination of jenkins & icinga. Each time a new data task is created, we have to write puppet code to set this up.

## Decision

Use Luigi to declare dependencies between data processing tasks on GOV.UK,
starting with the tasks in this repository.

Luigi is a lightweight framework for sequencing arbitrary tasks. Tasks can be
anything, they just have to have defined dependencies and outputs.
A Luigi task doesn't have to run pure python scripts - it can be set
up to run spark/hadoop jobs, docker containers etc.

Luigi is already used in GDS for verify's data pipelines, so I think this a
reasonable starting point for us.

The normal way to run Luigi is as a scheduler with a web UI, which lets you
visualise and monitor tasks and their dependencies. We don't have to set this
up straight away, but I think it would be useful if this project grows.
The "local scheduler" mode will work fine until then.

Luigi comes with `contrib` modules for interacting with many data stores we
use on GOV.UK, such as bigquery, postgres, mongodb, elasticsearch, and s3.
This could help us minimise the amount of code we need to write to shift
data from A to B.

When building new tasks we should adhere to these guidelines:

1. Any custom extract/transform/load code is decoupled from the
  Luigi task and testable independently.
2. Each task validates its inputs and asserts things about its output.
3. Each task persists its output somewhere where it can't be modified.
4. Variables and their assumptions are documented in a glossary.
5. Outputs follow a consistent naming convention.

## Consequences

- It should be easy to add in additional pipelines or pipeline steps later
  without making the code hard to navigate.
- Once you're familiar with the pattern, you should be able to quickly debug any pipeline and make changes to it.
- It should be easy to remove Luigi as a dependency if it doesn't meet our needs.
- Pipeline steps are reusable, because tasks make no assumptions about what's already been run.
- Any output or intermediate output can be reused by other tasks.
- These pipelines will only work for batch processing (not stream processing).

See also [Luigi design and
limitations](http://luigi.readthedocs.io/en/stable/design_and_limitations.html)

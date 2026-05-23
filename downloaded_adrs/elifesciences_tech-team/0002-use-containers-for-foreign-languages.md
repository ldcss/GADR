# 1. Use containers to deploy tools from foreign languages source code

Date: 2017-10-25

## Status

Proposed

## Context

eLife has a small set of supported languages: PHP, Python, JavaScript; in-house developers are present for them. All other languages are defined as **foreign**.

There are tools that are peculiar to our infrastructure, such as [goaws](https://github.com/p4tin/goaws) for AWS simulation, but are written in languages no one is an expert in (Go).

There are also tools that were originally written in another language but are being adopted by us, like [INK](https://gitlab.coko.foundation/INK/ink-api) for document conversion, written in Ruby.

These tools are usually distributed as source code. The operational overhead of writing formulas for the environment to build them is a form of waste.

Some tools written in Java instead have a very stable runtime platform (ElasticSearch, even Jenkins), as they are distributed as binaries.

## Decision

We will use existing Docker containers to deploy tools that require building from source in a foreign language, in testing or production environments.

## Consequences

We should not see too many runtimes being supported in builder-base-formula.

We should not allocate time to resolve versioning or building issues for languages such as Go or Ruby, but reuse existing container.

We should tag the container images we use and push them onto [https://hub.docker.com/u/elifealfreduser/] for reproducibility.

# 3. All cli options also respect environment variables

Date: 2020-07-16

## Status

Accepted

## Context

One of the goals of `stentor` is to be integrated into a CI system.
This requires flexibility in how users set command-line options.
In particular, in some CI systems it can be easier to change environment variables than it is to change command-line flags.

## Decision

All `stentor` command-line options can be set via a corresponding enviroment variable.

## Consequences

Writing new command-line options will also require adding, documenting, and sourcing a new environment variable.

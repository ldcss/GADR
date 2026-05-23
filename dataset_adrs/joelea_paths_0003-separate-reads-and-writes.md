# 3. separate reads and writes

Date: 21/02/2016

## Status

Accepted

## Context

Modelling reads and writes with the same model does not match reality - AddResult is very different from getResults. We should make sure to keep those models seperate.

## Decision

Use seperate models for reads and writes (or actions).

## Consequences


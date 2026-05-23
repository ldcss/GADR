# 6. Vellum Node Fails

Date: 2018-06-17

## Status

Accepted

## Context

Vellum node fails

## Decision

Vellum is always addressed by its cluster name and all of its data is stored in distributed databases with replicas of data on multiple nodes.

## Consequences

No data is lost, and Sprout / Dime can continue to access the data via the Vellum cluster domain name

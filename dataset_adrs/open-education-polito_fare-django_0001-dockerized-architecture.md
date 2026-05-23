
# 1. Dockerized Architecture 

Date: 2019-03-10

## Status

Accepted

## Context

The first draft release has to be highly configurable with few efforts.

## Decision

All the deployment phases are done using docker (compose). Local and prod yml
files govern such a deployment. 

## Consequences

The normal way of deploying will not be supported anymore.

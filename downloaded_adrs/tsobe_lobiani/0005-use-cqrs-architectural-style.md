# 5. Use CQRS architectural style

Date: 2021-01-09

## Status

Accepted

## Context

In non-trivial projects with complex business rules, it is often a challenge to come up with the model that scales well
for reads and writes at the same time in regard to performance and maintainability. 

## Decision

We will adopt Command Query Responsibility Segregation architectural style where there may exist 2 models for same 
domain entities each respectively on the Command (write) and Query (read) sides 

## Consequences

- We will have 2 simpler models each having one responsibility, either read or write 
- These 2 models will be optimized for read and write independently of each other
- For entities without, or with simpler, business rules, we may get duplicated models 

# 3. SYS - Use modular monolith

Date: 2020-09-16

## Status

Accepted

## Context

- Constraints
    - Greenfield project
- Quality attributes
    - Expected fast load

## Decision

We will not separate components in to separate deployment units, 
we will use modular monolith approach with single database. 

## Consequences

- Positive
    - Fast reliable and secure communication between components,
    - Transactions,
    - Simple infrastructure,
    - Simple development and deployment,
    - Possibility to extract separate services in future if needed.
- Negative
    - We will have to scale the whole thing when it will be needed,
    - We have to enforce component boundaries on our own.
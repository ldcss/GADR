# 10. All implementation rules will temporarily stay in the main health-modules repository

Date: 2018-05-16

## Status

Accepted

## Context

We currently don't have a good solution of having the code for implementation specific rules separate. The current solution is to add them into the health-modules repository, and switch them on or off through switches in the server. 

We will eventually move away from the solution, but until then, this stays. 

## Decision

Implementations specific rules to stay in the health-modules repository with switching on or off of rules provided by the server

## Consequences


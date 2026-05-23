# ADR 1. Database Inviolability

## Status
Accepted

## Context
There are several databases within the system. One per module.

## Decision
Under no circumstance should a module read/write from more than one database. 

## Consequences
When modules need to talk to each other, RPC communication mechanisms available within the server should be used.
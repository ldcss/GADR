# PostgreSQL server is introduced via docker compose

## Status

Accepted

## Context 

Developers need to be able to run application on their local machines in isolated environment.

Dockerized DB provides required service without the need to setup 
full-blown DB server on each local machine.

## Decision 

We will provide docker compose setup for Postgre SQL server.

## Consequences  

Developers will be able to use isolated DB service on docker host. 
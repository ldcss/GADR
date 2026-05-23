# 2. Use docker-compose v.2

Date: 13/02/2016

## Status

Accepted

## Context

People are very used to traditional layered architectures and request/response cycles which disguise a lot of the complexity of distributed systems. They also restrict extending systems as data is locked down in a specific form in specific systems. We want to give an alternative view with a clear demonstration of the trade-offs involved.

Getting people to give it an initial attempt is going to be hard, so it needs to be super quick to get working on a local machine.

## Decision

We will use a docker-compose.yml (v.2) as the primary entry point of the project

## Consequences

* Nginx caches its DNS lookups, docker-compose dynamically routes when new containers spin up that should now have that hostname. This can play very, very sadly.


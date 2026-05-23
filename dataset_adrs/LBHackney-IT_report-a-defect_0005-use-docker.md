# 5. Use Docker

Date: 2019-05-09

## Status

Accepted

## Context

Hackney have a preference for using containers across their digital services: https://github.com/LBHackney-IT/API-Playbook#containers

## Decision

We will build and run this service using Docker and Docker Compose. Heroku container hosting will be used.

## Consequences

The team will have greater parity between environments, if it works locally we will have high confidence that it will work on Heroku.

If this project needs to move off of Heroku in the future then a containerised service will make that process easier in terms of time and complexity.

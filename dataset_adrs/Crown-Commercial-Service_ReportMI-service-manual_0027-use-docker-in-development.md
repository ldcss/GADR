# 1. use-docker-in-development

Date: 2019-08-06

## Status

Accepted

## Context

The issue motivating this decision, and any context that influences or constrains the decision.

- onboarding a fresh team has consumed a lot of time and we want to improve this for the future as this service moves from a build phase into the support phase.
- 2 ways to start and run the application were documented, depending on your preference you would use the ones you were most comfortable with. This led to docker documentation that fell behind and didn't work out of the box
- when supported by the dxw support team, a different developer will be on hand each week to fix issues. In order to effectively and confidently apply fixes we want to standardise and test the set up process, removing as much manual process as possible and allowing the developer to address problems quickly.
- in ADR 26 we discussed moving from AWS ECS (containers) to GOV.UK PaaS (no containers). Whilst we no longer use containers in production and there aren't the same advantages to parity we would normally fine, we believe there is still good value to using it to make consistent development environments.

## Decision

We are going to use Docker in development exclusively for the frontend and the API.

## Consequences

- docker is a standard tool for containerising applications and is well documented, any future support function should be able to get the same benefits
- GOV.UK PaaS does now support containers so we would make any switch back to using containers in all environments a less complex task
- members of the team who are not familiar with Docker will have an extra overhead of getting comfortable with Docker
- we know that the test suite runs slower with Docker, going up from 40 seconds (no docker) to 150 seconds (docker). We want to try and work through these problems using by investing time to improve the way we're using Docker, perhaps by using something like [docker-sync](http://docker-sync.io/)
- removing non-docker instructions will ensure that we don't have another situation with 2 versions of documentation that achieve the same task that are maintained at different rates

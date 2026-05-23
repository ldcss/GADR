# 9. Use cypress for e2e testing

Date: 2019-03-01

## Status

Accepted

## Context

We need to test the frontend interface from the user perspective.

## Decision

We use [cypress](https://docs.cypress.io/guides/overview/why-cypress.html#In-a-nutshell) as our frontend e2e testing tool.

## Consequences

Easy integration in our pipeline, but limitations in parallism and not the most popular stack that is selenium. I will have to watch out how this scales. Further cypress currently does not integrate with Jest.

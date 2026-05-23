# 15. frontend-backend-architecture

Date: 2020-09-05

## Status

2020-09-05 accepted

## Context

Facing the concern that by serving views from the backend API, I have less opportunity for reusing APIs, creating new apps and staying on trend, I propose to decouple the frontend and backend architecture of the site.

The opportunities that this creates would be to learn new technologies such as

- GraphQL: new approach to APIs to solve the problem of creating different endpoints for different frontend requirements.
- Server-side rendering: important for Search engine optimization and performance.

## Decision

- Re-write the backend in Fastify for better Typescript support.
- Create a server-side rendered frontend.

## Consequences

- Project re-write/refactor - [example project](https://github.com/txchen/fastify-nextjs)
- Learn [NextJS](https://nextjs.org/)

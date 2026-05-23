# 11. Develop main frontend (shopping) as a separate, SSR app

Date: 2021-03-31

## Status

Accepted

## Context

In [ADR 9](0009-develop-admin-tool-as-spa.md) we decided to develop admin tool as an SPA. Unlike admin tool, shopping
has different requirements:
- User experience matters
- Should be accessible for unauthenticated users
- User interface should have unique look and feel, more suited for public use
- Should be SEO friendly

## Decision

We will develop shopping as a separate frontend application employing Server Side Rendering technique to improve the 
user experience without compromising interactivity.

## Consequences

- Overall project complexity will increase, as there are different approaches and technologies to cover
- Having admin and shopping segregated, makes them more focused around their responsibilities and grants them more 
  flexibility to evolve independently

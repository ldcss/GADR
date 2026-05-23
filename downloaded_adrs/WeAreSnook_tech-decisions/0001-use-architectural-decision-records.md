# Use Architectural Deicision Records

## Context

We need a way to record technical decisions not only in projects but for the team more widely. To provide some consistency we suggest using [Architectual Decisions Records](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions) to record our decisions as a team.

Architectural decision records are essentially a formatted log of technical decisions. We provide [a template](TEMPLATE.md) that the team can use for recording these decisions.

## Decision

We will use architectural decision records (ADRs) to record our technical decisions on projects and as a team. When we make a new technical decision, we will create a log using the TEMPLATE.md file and add it to the README.md in the [technical-decisions](https://github.com/WeAreSnook/tech-decisions) repo.

The first technical decision [Github vs Gitlab](0000-github-vs-gitlab.md) will keep its initial formatting.

## Status
Proposed

## Consequences

### Pros

Adopting ADRs should bring greater consistency for documenting decisions. It also takes away uncertainty about how much detail to include / structure the document.

### Cons

There may be a small learning curve for people who are new to writing technical decisions in this format.

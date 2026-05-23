# Repository Structure Frontend/Backend

## Context and Problem Statement

Should we use different repositories for Frontend and Backend or use a single repository?

## Considered Options

* Mono Repo
* Different repositories

## Decision Outcome

We chose option 1, Mono Repo, because as a starting point it reduces unnecessary complexity when working with frontend and backend logic.
Furthermore, we can have a single CI build in order to verify the whole project source code.

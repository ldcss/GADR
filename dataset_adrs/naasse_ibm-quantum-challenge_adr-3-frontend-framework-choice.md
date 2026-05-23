# Architectural Decision Record (ADR) 3: Frontend Framework Choice

## Context and Problem Statement

I would like to add a simple UI, and must choose a technology to use.
This is optional, but will facilitate manual testing, display knowledge on how to act as an API consumer,
and continue the goal of strengthening my own skills.

Primary choices to investigate are:

* ReactJS
* Angular
* VueJS
* Vanilla/jQuery (No Framework)

## Decision Outcome

I will use ReactJs for my implementation.

This is a robust and powerful, yet easy-to-use framework, given my experience with the others and the community opinion.

## Consequences

* We can take advantage of `create-react-app` to quickly build a simple UI
* As our UI will not be complex, we don't have to delve into the more complicated UI features for managing state

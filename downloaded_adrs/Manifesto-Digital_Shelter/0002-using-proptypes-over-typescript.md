# 2. Using PropTypes over Typescript

Date: 2018-02-12

## Status

Accepted

## Context

The use of TypeScript would in turn provide a more stable codebase.

For this particular project since the vast majority of components will receive either strings, objects or arrays of strings as props and have no state due to the fact they just render externally provided content.

We feel that in this use-case adding the complexity, additional dependencies, increased on-boarding and higher risk of incompatibilities the benefits do not out weigh the overhead, with PropTypes being sufficient given the static nature of the website.

TypeScript would increase the complexity of the codebase and the time needed to on-board a developer.

## Decision

We will use PropTypes

## Consequences

We have less risk of incompatibilities and an easier on-boarding process. A risk is that in the future there may be more complicated components were a strictly typed language enforced would make the code more stable.

# 4. Mercury Platform is deliberately a polyglot system (with language suggestions)

Date: 2020-05-17

## Status

Accepted

## Context

Mercury platform could be accomplished by a handful of python scripts run locally on a consumer system.

However, the project is intended to also be a learning platform that uses the strengths of individual languages and cloud native services

## Decision

Mercury platform will use multiple languages to achieve it's goal.

The proposed list:
- Data retrieval and manipulator (Wrangler): Elixir
- Data processor and analyzer: Python
- Controller for end user input: Go
- Infrastructure: Pulumi via TypeScript

Languages will be changed out as we discover more about each language's limitation with regard to our needs.

## Consequences

The project will take longer as we teach ourselves each language and struggle through the differences. At the end of the day though, we should still be able to have a well architected and scalable platform that separates concerns due to the lack of ability to call other services directly.


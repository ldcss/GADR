# ADR 0009: Organise by feature

Date: 2018-10-29

## Status

Accepted

## Context

There are two main strategies for organising source code that I'm aware of:

- Organise by kind
- Organise by feature

With "Organise by kind" we group modules that are related architecturally together. I.e. group all
"Effects", group all "Data", group all "Scenes".

This is a fairly common approach, particularly given that website architectures often typify this
style by grouping all "modules", "views" and "controllers".

Alternatively we can "Organise by feature", ideally in this style the source code required to
implement a particular "Feature" is grouped together instead. Ideally this would mean that
removing a feature would simply mean deleting it's grouping any removing any dependent links.

For this project I want to experiement to see what "Organise by feature" would look like for a game.

## Decision

We're going to organise by *feature*!

## Consequences

- All the code needs to be regrouped
- We need to figure out what "features" we have and how to best group them
- Wwe need to figure out what the dependency graph between features looks like. And how to separate
  high level features like "The Toad" from low level features like "Rendering"

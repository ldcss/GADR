# 7. Use React

Date: 2019-06-24 (Backfilled 2019-11-11)

## Status

Accepted

Supercedes [3. Use AngularJS 1.x](0003-use-angularjs-1-x.md)

## Context

When this application was first built [AngularJS 1](https://angularjs.org/) was one of the more popular frameworks for building frontend applications.

Since then [Angular 2](https://angular.io/) and beyond was released. Angular 2 is not backwards compatible and a non-trivial amount of effort was required to learn the new version and to migrate the application over.

[React](https://reactjs.org/) had also gained more market share and had become the framework I had grown most familiar with.

## Decision

The application will be rewritten in React.

## Consequences

- Existing AngularJS constructs were migrated into React components or managed in state.

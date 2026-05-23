# 5. Implement yarn as a CLI for Node package management

Date: 2018-05-15

## Status

Accepted

## Context

Yarn and NPM can both manage the Node packages for a project. Recent updates to NPM mean that Yarn only has a negligible performance advantage over NPM.

## Decision

We will use `yarn`, `yarn start`, `yarn add`, `yarn remove` etc. for the management of Node packages in our project.

## Consequences

We will have fast package installs and updates.

We will have locked versions for reproducible installs across devices, due to the `yarn.lock` file.

We will be able to change to using `npm` if necessary at a later date, with a minimal amount of effort.

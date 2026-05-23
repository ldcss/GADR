# Design decision 3 - NPM package for each component

## Background

Need to decide whether to organize this repository to export a single NPM package, or a package for each component.

## Findings

- React compliation will use tree-shaking, removing unused imports.
- Using a single package will have a simpler setup, allowing for quicker development.
- As library grows decision can be re-evaluated if single imports has a large preference.

## Decision

Decision to export as a single package was made.

# Design Decision 7 - Accessibility Testing

## Background

Decision for how to test the accessibility of components.

## Findings

The react testing libraries considered were:

- [jest-axe](https://www.npmjs.com/package/jest-axe)
- [axe-core](https://github.com/dequelabs/axe-core-npm/tree/develop/packages/react)
- [a11y](https://www.npmjs.com/package/a11y)

### jest-axe

Runs with jest as automated unit tests. Returns console information about general accessibility violations.

### axe-core

Runs in browser, logging accessibility violations to the console.

### a11y

Runs against a url, returning information about general violations

## Decision

While running accessibility tests against the entire loaded website can be more accurate for catching accessibility violations, for testing a library of individual components having individual unit tests is preferable. However, the ability to add a11y as an add-on to storybook for in browser manual testing will be a useful addition for viewing accessibility criteria in-browser.

The package jest-axe will be used for automated accessibility testing, and a11y for in-browser testing via the storybook add-on.

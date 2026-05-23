# 13. cypress-e2e-tests-in-typescript

Date: 2019-09-21

## Status

2019-09-21 accepted

## Context

I'm getting Typescript errors in the e2e tests. If I'm relying on Typescript for linting then keep errors clean is good hygiene. I'v tried ignoring the `e2e/` or `cyperss/` folders and that is not working. Why? Not sure.

## Decision

In the context of getting Typescript errors in my e2e tests and facing the concern to keep errors clean, then use Typescript for e2e tests. Especially since it seems to be [well documented][cypress-ts] with examples. Therefore the burden should be light.

## Consequences

Choose between [Webpack][cypress-webpack] or [Browserify][cypress-browserify]. I choose Browserify because the [Webpack config][cypress-axe-broken] doesn't support accessibility testing.

[cypress-ts]: https://docs.cypress.io/guides/tooling/typescript-support.html#Transpiling-TypeScript-test-files
[cypress-webpack]: https://basarat.gitbooks.io/typescript/docs/testing/cypress.html
[cypress-browserify]: https://github.com/cypress-io/cypress-example-recipes/tree/master/examples/preprocessors__typescript-browserify
[cypress-axe-broken]: https://github.com/avanslaars/cypress-axe/issues/7

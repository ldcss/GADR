# ADR 1 - Module Bundling with RollupJS

## Context

A module bundler combines multiple files into fewer files (this is likely a single file
for libraries but may be multiple files for web apps). Common choices include Webpack and
more recently rollup.js; less common choices include Parcel and perhaps SystemJS.

While Webpack is currently the most popular bundler for web applications, rollup.js is
an increasingly popular choice for libraries. A notable example of a library using rollup.js is
[React](https://github.com/facebook/react/tree/master/scripts/rollup).

### Rollup.js Pros

Rollup.js produces smaller bundles (due to treeshaking and omitting a runtime).

### Rollup.js Cons

- Smaller community. This means fewer plugins and less unofficial documentation
  (blog posts, StackOverflow questions, etc).
- Missing support for code-splitting and hot module reloading (due to missing runtime). This
  is a bigger concern for web apps.

## Decision

We will use [Rollup.js](https://rollupjs.org/guide/en) for the smaller bundle size (~4K savings).
However, it's unclear how significant this benefit will be to end users and we can re-evaluate
if needed.

## Status

Adopted. This project currently uses rollup.js but could switch to Webpack with minimal effort. The
bundle size savings (~4K) may not make a significant difference to end users.

## Consequences

See the pros / cons listed in Context.

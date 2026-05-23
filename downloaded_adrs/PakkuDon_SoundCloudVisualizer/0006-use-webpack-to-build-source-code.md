# 6. Use Webpack to build source code

Date: 2019-06-23 (Backfilled 2019-11-11)

## Status

Accepted

Supercedes [4. Use Gulp to build source code](0004-use-gulp-to-build-source-code.md)

## Context

When this project was first starting out [Gulp](https://gulpjs.com/) was one of the tools of choice for running tasks such as bundling and minifying code.

Since then task runners seem to have fallen out of popularity and bundlers such as Webpack and Parcel are the preferred approach.

## Decision

Webpack will be used to bundle source code.

## Consequences

- `gulpfile.js` and references to Gulp tasks will be replaced with Webpack config and CLI invocations.
- CSS files will be imported in source code so they are processed by configured loaders.
- `index.html` will no longer link to JavaScript bundle as this will be injected by [`html-webpack-plugin`](https://webpack.js.org/plugins/html-webpack-plugin/)

# 4. Use Gulp to build source code

Date: 2016-02-23 (Backfilled 2019-11-11)

## Status

Superceded by [6. Use Webpack to build source code](0006-use-webpack-to-build-source-code.md)

## Context

The application's JS code was loaded via `script` tags in `index.html`. As the project was migrated from Vanilla JS to AngularJS the number of source files that needed to be included grew, and this approach became unwieldy. 

I looked into how we could bundle our code. At the time of development Grunt and Gulp were the two main task runners available.

## Decision

[Gulp](https://gulpjs.com/) will be used to bundle client-side code.

## Consequences

- Tasks to bundle and concatenate source code were written in `gulpfile.js`.
- Links to individual source files in `index.html` were replaced with a link to the bundle output by Gulp.

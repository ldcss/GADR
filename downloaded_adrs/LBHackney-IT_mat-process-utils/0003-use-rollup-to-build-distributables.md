# 3. Use Rollup to build distributables

Date: 2019-10-29

## Status

Accepted

## Context

We want to be able to distribute this library to me ingested by TypeScript or
plain JavaScript (both commonJS and module) applications.

[Rollup](https://rollupjs.org/guide/en/) is a popular JavaScript bundler with
support for TypeScript and simple configuration.

## Decision

We will build distributables using Rollup.js.

## Consequences

With Rollup.js we can build type declarations, commonJS, and module code using a
single simple command, and some simple config. This makes it easier for us to
distribute our code.

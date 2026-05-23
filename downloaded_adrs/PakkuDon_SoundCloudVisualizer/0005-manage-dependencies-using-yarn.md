# 5. Manage dependencies using Yarn

Date: 2019-06-23 (Backfilled 2019-11-11)

## Status

Accepted

Supercedes [2. Manage client-side dependencies using Bower](0002-manage-client-side-dependencies-using-bower.md)

## Context

When this project was first starting out [Bower](https://bower.io/) was the tool of choice for managing frontend dependencies.

Bower has since been deprecated and its creators have [advised its users to migrate to other solutions](https://bower.io/blog/2017/how-to-migrate-away-from-bower/).

## Decision

Dependencies will be managed using [Yarn](https://yarnpkg.com/).

## Consequences

- All dependencies will be declared in `package.json` and managed via Yarn.
- Bower dependency and `bower.json` removed.

# 2. Use Yarn rather than npm

Date: 2017-06-19

## Status

Accepted

## Context

Package versions specified in `package.json` are often never any more precise than the major version.
By default, [Yarn](https://yarnpkg.com/lang/en/) records the exact version of the packages. In contrast, [npm](https://www.npmjs.com/) version 4 uses an opt-in feature called [npm-shrinkwrap.json](https://docs.npmjs.com/files/shrinkwrap.json) and in version [5](http://blog.npmjs.org/post/161081169345/v500) this has been superseded by a new file - [package-lock.json](https://docs.npmjs.com/files/package-lock.json). The feature no longer opt-in for version 5 of `npm`.

## Decision

We will use `Yarn` as we have more experience of this than version 5 of `npm` and `Yarn` has been proven to work for our use cases.

## Consequences

`Yarn` is newer than `npm` and isn't always going to be installed in the development environment. In order to mitigate this there is a [pre-bootstrap](../../scripts/pre-bootstrap) script that will help people install `Yarn` and any other dependencies required for the basic development environment.

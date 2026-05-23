# 9. place-tests-next-to-source-files

Date: 2019-08-27

## Status

2019-08-27 proposed
2019-09-02 accepted

## Context

While migrating to Typescript, fixing tests means switching between the source file and their test files. Where the test files are in another folder, the journey is longer. If they were side-by-side then once I had the source or test, finding the related file would be much easier

## Decision

Moving test files next to the source code makes it much easier to switch between source and tests. It's also easier to see which test files do not have any unit tests.

## Consequences

- Refactoring

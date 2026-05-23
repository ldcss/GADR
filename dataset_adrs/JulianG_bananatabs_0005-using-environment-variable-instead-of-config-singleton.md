# 5. Using environment variable instead of Config singleton

Date: 2019-07-19

## Status

Accepted

## Context

We had a `config.ts` that exported a single `Config` object with a single `debug` boolean property.
This was being used in DebugUtils.tsx to control whether or not to render some extra debug information.

One problem was that in order to activate this we had to change the value in a file that was under version control, and then remember to revert it and never to commit it with `debug: true`.

## Decision

We removed the `config.ts` file and used an environment variable instead. This environment variable is set is set when running a new script defined in `package.json`.

## Consequences

We can now start the watcher as `yarn start:debug-info` to enable this, without having to modify any files.

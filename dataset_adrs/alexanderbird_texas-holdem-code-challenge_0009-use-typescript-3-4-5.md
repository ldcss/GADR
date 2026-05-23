# 9. Use TypeScript 3.4.5

Date: 2019-05-30

## Status

Accepted

Expands on [8. Use TypeScript](0008-use-typescript.md)

## Context

The TypeScript plugin for ESLint requires TypeScript below 3.5.0. The next earlier
version is 3.4.5 (from ~ 1 month ago)

Warning from ESLint:

```
=============

WARNING: You are currently running a version of TypeScript which is not officially supported by typescript-estree.

You may find that it works just fine, or you may not.

SUPPORTED TYPESCRIPT VERSIONS: >=3.2.1 <3.5.0

YOUR TYPESCRIPT VERSION: 3.5.1

Please only submit bug reports when using the officially supported version.

=============
```

Further, there are no cutting edge TypeScript features I need for this.

## Decision

Use TypeScript 3.4.5

## Consequences

No more ESLint warning. Risk of missing out on cool new TypeScript features.

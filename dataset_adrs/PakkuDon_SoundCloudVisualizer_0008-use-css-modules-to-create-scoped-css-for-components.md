# 8. Use CSS modules to create scoped CSS for components

Date: 2019-07-21 (Backfilled 2019-11-11)

## Status

Accepted

## Context

The CSS declarations for all components was declared in a single file. This has become difficult to manage as the relevant CSS is located separately from its component and there are a lot of declarations in one file.

## Decision

We will enable [CSS Modules](https://github.com/css-modules/css-modules) and co-locate each component's CSS declarations with its code.

## Consequences

- All CSS declarations aside from truly global styles will be extracted out into a separate `styles.css` for each component.
- All components will need to import their `.css` file and reference the generated class names rather than using a hard-coded class.

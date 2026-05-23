# 9. Use PostCSS

Date: 2019-11-07 (Backfilled 2019-11-16)

## Status

Accepted

## Context

As mentioned in [ADR # 8. Use CSS modules to create scoped CSS for components](0008-use-css-modules-to-create-scoped-css-for-components.md) this application has separate CSS files for each component's CSS. We now require a need to define commonly used variables such as colours, spacing and so on in a centralised location so that these values are not duplicated across the codebase.

There were two solutions considered:

1. [Sass](https://sass-lang.com/)
  - Superset of CSS that compiles to CSS.
  - Supports variables, nesting, partials, operators, and so on.
  - Has two major implementations in JavaScript:
    - [`sass`](https://www.npmjs.com/package/sass) which is implemented in Dart.
    - [`node-sass`](https://www.npmjs.com/package/node-sass) which provides bindings to the C library LibSass.
2. [PostCSS](https://postcss.org/)
  - Transforms CSS with JavaScript plugins.
  - Plugins that add support for Sass features such as variables, nesting, imports, and so on are available.
  - Allows for auto-vendor prefixing via [`autoprefixer`].

## Decision

This system will use PostCSS to process CSS.

## Consequences

- Commonly used values such as colours will be extracted into a separate CSS file which can then be imported as needed.
- PostCSS and several PostCSS plugins will be added to the project's devDependencies.

# 8. Use styled-jsx

Date: 2019-10-10

## Status

Accepted

## Context

We want to be able to style our components in a way that reduces chances of
clashes, or unwanted styles.

We could use a convention like [BEM](http://getbem.com/), but they are generally
hard to enforce.

[`styled-jsx`](https://github.com/zeit/styled-jsx) is an alternative that scopes
styles to individual components, and is integrated into Next.js by default. We
can still fall back to global stylesheets if required (for instance if we are
using GOV.UK styles).

## Decision

We will use `styled-jsx` for internal component styling.

## Consequences

Using `styled-jsx` means styles for components are contained within those
components, ensuring they never leak out unintentionally. We can share styles
between components via
[`styled-jsx/css`](https://github.com/zeit/styled-jsx#external-css-and-styles-outside-of-the-component)
as needed.

`styled-jsx` also allows styles to be dynamic without dealing with stateful
classes.

# 3. Using Styled Components

Date: 2018-02-13

## Status

Accepted

## Context

Using either plain CSS or CSS Modules instead of using Styled Components.

One main driver for not using styled components was that it could be more portable in the future, but there was no real use case for this.

A limitation of CSS modules is the inability to pass values to CSS. CSS modules would potentially have to use a mix of inline styles and classes to achieve this.

## Decision

We will use Styled Components

## Consequences

A risk is that Styled components is a step away from standard CSS files and would require JS knowledge to make changes.

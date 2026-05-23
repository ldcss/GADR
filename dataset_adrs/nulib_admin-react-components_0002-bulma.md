# 2. bulma

Date: 2020-04-21

## Status

Accepted

## Context

We needed a straight-forward, customizable UI style framework that was somewhat opinionated (we don't have a design team), customizable, intuitive in naming convention, and one which would not interfere with our JavaScript React component implementations.

We reviewed a few UI frameworks including Ant Design, Bootstrap, Bulma, and TailwindCSS.

## Decision

We've chosen [Bulma](https://bulma.io/) for it's blend of simplicity, ease of use, and CSS-only approach, and current market share. It has a modern look & feel, seems to be gaining in popularity, and doesn't look like a lot of Bootstrap applications.

## Consequences

By choosing to use Bulma, we're assuming that new applications which consume the component library would use Bulma themselves (possibly) for main layout and individual application styling.

A risk could be Bulma flavoring doesn't mesh with non-Bulma applications.

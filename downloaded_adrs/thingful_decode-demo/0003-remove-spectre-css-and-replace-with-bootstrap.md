# 3. Remove Spectre CSS and replace with Bootstrap

Date: 2019-01-04

## Status

Accepted

## Context

The deployed demo site must be designed to render nicely on mobile devices.
This is so that participants in the pilot can pretend the demo site provides
the same basic user experience as the wallet once this exists.

Spectre CSS at least in the configuration implemented in the original version
of this app doesn't render a UI that is usable from a mobile device,
particularly when it comes to form inputs (buttons and fields were tiny and
hard to read).

## Decision

We will replace [Spectre.CSS](https://picturepan2.github.io/spectre/) with
[Bootstrap](https://getbootstrap.com/).

## Consequences

* Will require restructuring and rewriting some of the site HTML and CSS as the
  two frameworks are not exactly aligned in the semantics of how they describe
  content.

* In contrast we have tested that Bootstrap forms are rendered in such a way
  that they are naturally usable from mobile devices, so we can be confident
  this implementation will work for both.

# 3. component-bundling

Date: 2020-04-21

## Status

Accepted

## Context

When bundling components for usage in consuming applications, should we require consuming applications to have the same dependencies as this repository? Or should exported components be packaged assuming no dependencies?

## Decision

We'll package components with their own inline styles. No external dependencies needed.

## Consequences

Exported components will appear consistent across any consuming application. A risk could be components are somewhat rigid, but we'll see how implementation goes.

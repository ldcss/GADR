# 3. Implement CSSinJS with Emotion as default approach to styling

Date: 2018-05-15

## Status

Accepted

## Context

The govuk-react components library uses CSSinJS with Emotion for styling. Our approach to styling needs to be efficient and maintainable, and this could be achieved either through a preprocessor like SCSS/SASS, or by using CSSinJS.

## Decision

We will use CSSinJS with the [Emotion library](https://emotion.sh/), with SCSS available as a fallback should it be necessary.

## Consequences

Our approach to styling will be consistent with the govuk-react components library.

Our approach to styling will be highly maintainable, re-usable and modular.

Contributors need to learn Emotion and CSSinJS as well as SCSS.

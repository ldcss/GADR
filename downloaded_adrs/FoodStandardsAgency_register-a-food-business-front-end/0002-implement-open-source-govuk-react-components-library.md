# 2. Implement open source govuk-react components library

Date: 2018-05-15

## Status

Accepted

## Context

The website needs to comply with the GDS design language. In the future, the standard GDS design language might need to be themed to match food.gov colours, fonts, etc.

## Decision

We will implement the open source govuk-react npm package hosted at [https://github.com/penx/govuk-react](https://github.com/penx/govuk-react) wherever it has a component that fits our needs.

We will create custom components and layouts where necessary to follow the GDS design language.

We will contribute back to the project to ensure it fulfils all of our needs.

## Consequences

The govuk-react library uses CSSinJS with Emotion as its default method of styling. We will need to consider this when making decisions on CSS styling.

It might be marginally more difficult to modify these components if or when necessary.

Tests and quality standards are currently defined by those who started the project.

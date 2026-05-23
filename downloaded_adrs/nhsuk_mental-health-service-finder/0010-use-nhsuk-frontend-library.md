# 10. Use nhsuk-frontend library package

Date: 2019-11-11

## Status

Accepted

## Context

The service uses an old version of the nhsuk-frontend library. When the service moves from beta to
live we want it to look consistent with other nhs.uk services.

## Decision

Use the Nunjucks macros, SCSS and JS available in the nhsuk-frontend NPM package. Consuming these
directly from the package allow us to take advantage of any updates to the library.

## Consequences

The application will be visually more consistent with nhs.uk.

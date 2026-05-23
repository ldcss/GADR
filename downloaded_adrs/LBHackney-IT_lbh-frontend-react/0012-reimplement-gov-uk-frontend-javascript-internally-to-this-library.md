# 12. Reimplement GOV.UK Frontend JavaScript internally to this library

Date: 2019-11-28

## Status

Accepted

## Context

[govuk-frontend](https://github.com/alphagov/govuk-frontend) doesn't do a good
job of detecting if it's in a browser environment or not, and therefore, whether
`document` and friends are available or not. It also performs a number of
polyfills that rely on the presence of those browser globals. This means that it
throws exceptions when attempting to import some JavaScript modules from that
library.

The way `govuk-frontend` JavaScript is generally written is under the assumption
that you'll want, and be able, to pass the raw DOM nodes to the module
constructors. React doesn't work that way, and we could dig into the prototypes
of the objects created by those constructors, but given that these methods are
not intended to be used directly, it would be compliant with
[Semantic Versioning](https://semver.org/spec/v2.0.0.html) to completely change
their implementation without releasing a new major version. This makes relying
on their behaviour being fixed unreliable.

## Decision

We will re-implement JavaScript features from `govuk-frontend` in more idiomatic
React in this library.

We will link to the version and the source of the original implementation
alongside our implementation for reference, linking to the code in the specific
commit we were referring to, not `master`.

## Consequences

This allows us to make the functionality more idiomatic React, making it easier
to integrate. We already diverge in some ways from `govuk-frontend` so there are
likely to be implementations in the source that wouldn't work with our
implementation, anyway.

However, it also means that updating versions of `govuk-frontend` needs some
extra care to check if the original implementation has changed in ways that we
need to duplicate. We can mitigate some of that by preventing Dependabot from
automerging updates to `govuk-frontend`, to ensure a human reviews the changes
before merging them. Some extra care looking at the diff will be required for
those reviews than might otherwise be needed.

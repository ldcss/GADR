# 2. Use experimental annotation

Date: 2017-09-25

## Status

Accepted

## Context

Downstream libraries such as API client, SDK, validators, bot-lax-adaptor rely on the schema provided by api-raml.

It is difficult and error-prone to point the downstream libraries to a particular branch; in particular given this branch would need to rebuild dist/ after checkout.

It is forbidden to update in place a schema exposed by an API without versioning: the content types follow semantic versioning.

## Decision

We will annotate with `@experimental` APIs that are being worked upon, and merge the into `develop` and `master` (indirectly).

## Consequences

Clients should not rely on `@experimental` APIs, at they may break the schema or disappear at any time.

API definitions can be merged as soon as they are ready, even without services implementing them, as long as they are tagged with `@experimental`.

When APIs tagged with `@experimental` are reworked, anything about them can change, from content type to parameters to the response schema.

# 8. Support IndexedDB as a data store

Date: 2019-11-12

## Status

Accepted

## Context

We need to persist the user data to the backend. Rather than building our
frontend to be tightly coupled to an API, we want a layer that can sit between
the application and the API.

We know that we will need to support offline use of these forms. We also want
users to be able to recover unsubmitted forms if they haven't gone online
between sessions.

We also know that some forms will require the upload of images.

IndexedDB is a [well supported](https://caniuse.com/#feat=indexeddb) browser
database that persists data across sessions. It supports storing blob data (such
as images), and has decent storage limits.

## Decision

We will support IndexedDB as a data store layer, sitting between the application
and the API.

## Consequences

IndexedDB has a fairly complicated interface. There is some overhead in
understanding and using it, but hopefully we can insulate the user for most of
it by using libraries and wrapping the implementation.

If a consumer of this library doesn't need to support offline use, they may not
need IndexedDB, and may be able to use a plain object. We should make sure we
continue to support that use case.

IndexedDB has good support in modern browsers, except Edge and IE. Those
browsers support a subset of features, so we should make sure we're testing on
those browsers when we need to support them, and that we polyfill any missing
features we need.

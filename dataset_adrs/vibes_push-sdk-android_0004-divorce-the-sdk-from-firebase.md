# 4. Divorce the SDK from Firebase

Date: 2017-08-04

## Status

Accepted

## Context

There was much discussion over whether the SDK should implement the
Firebase-related services for token refresh and notification handling, or leave
that up to the consuming app. If the SDK handles it, it's less setup for the
consumer; however, this comes at the cost of much flexiblity.

## Decision

In the end, we decided that the lack of flexibility (e.g. for supporting both
"register on first launch" and "register/unregister on log in and log out"
models) warranted removing the services from the SDK. They will be implemented
in the demo application instead.

## Consequences

We may want to create some code samples (beyond the demo app) for how to
implement the services; however, because they are highly consuming-app
dependent, this may be best to do after a few implementations have been
completed.

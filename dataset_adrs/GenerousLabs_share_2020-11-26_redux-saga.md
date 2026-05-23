# Redux saga

# Status

Accepted.

# Context

This is a rebuild of the plans project. I used thunks in plans. This was
okay, but not very testable. It gets messy dispatching thunks inside thunks.
When I started working on share (this repo), I felt like thunks weren't going
to cut it.

# Decision

I switched redux-thunk for redux-saga.

I implemented a saga "layout" something like follows:

- `root.saga.ts` - The root saga which wires up each other saga
- `service/service.sagas.ts` - Sagas for a given service
  - The default export is a single saga which invokes all the other sagas in
    this file

# Consequences

Sagas are conceptually harder to understand. They're less obvious /
intuitive. It's also harder to follow the code path. A developer not familiar
with the saga workflow may not have any idea that
`store.dispatch({type:'SHARE/someAction'})` results in some async code
running somewhere in a saga.

Sagas are much easier to test / mock than thunks. I wrote some tests for one
of the sagas and they were already useful in flagging issues. Plus, when
starting out without any UI, it's easier to know that sagas are behaving as
they should do from the tests.

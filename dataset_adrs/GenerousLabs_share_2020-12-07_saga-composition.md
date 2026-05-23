# Saga Composition

## Status

Accepted.

## Context

I'm trying to compose sagas. For example, the setup saga needs to create the
"me" repo then the "commands" repo. Each of these is a series of steps. The
steps need to complete in a specific order. Each step can only begin after
the previous step has completed.

There's no clear, idiomatic, way to achieve this with sagas. For example, I
have a `createNewRepo` saga and a `gitCommitAll` saga. If I dispatch an
action at the end of the `createNewRepo` which triggers the `gitCommitAll`
saga, I have no way of knowing once the `gitCommitAll` saga completed. I
could wait for a finished event from that saga, but I cannot be sure that the
saga was not triggered somewhere else.

There's some useful discusson on this topic here:
https://github.com/redux-saga/redux-saga/issues/886

The recommended approach seems to be invoking sagas from within other sagas
using `call()` instead of `put()` (calling the saga function, not dispatching
an action).

There are some packages which try to help with this.

- [redux-saga-callback](https://github.com/kutlugsahin/redux-saga-callback)
  watches for an `onComplete` property on actions, and calls it when a saga
  consuming that action completes.
- [redux-saga-promise](https://github.com/adobe/redux-saga-promise) creates
  "promsie actions" which can be resolved in sagas. They can then be awaited
  with `putResolve()` in other sagas, amongst other things.
- [redxu-saga-promise-actions](https://github.com/tomekkleszcz/redux-saga-promise-actions)
  is very similar to redux-saga-promise but written in TypeScript.
- [typescript-fsa-redux-saga](https://github.com/aikoven/typescript-fsa-redux-saga)
  automates disaptching started, finished, error actions within a saga.
- [redux-saga-try-catch](https://github.com/killtheliterate/redux-saga-try-catch)
  exposes 2 helpers to wrap sagas and ensure they catch, invoking a callback
  attached to the action which triggers the saga.

This came up specifically with the `addOneRepo` action. It was originally a
state update action, then I tried to `call()` that saga within another saga.
The consequence was that the action was never dispatched, and so redux state
wasn't updated. Having a single action for both saga triggering and state
update didn't work.

## Decision

Actions which trigger sagas MUST NEVER update redux state.

Effectively, actions are split into 2 types. Saga trigger actions and state
update actions. If a saga needs to update redux state, it can dispatch a
state update action immediately when it starts, potentially with an identical
payload.

Saga trigger actions should be called `SagaAction` and should be defined and
exported from the saga file. In some way, they are completely separate from
"redux" state actions.

## Consequences

If this pattern is rigorously followed, I can safely trigger a saga via
`call()` instead of `put()`, wait for it to complete, and trust that it will
have updated redux state if required.

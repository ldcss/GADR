# ADR 0012: Use concrete state monad

Date: 2018-11-25

## Status

Superseded by [adr-0013](/docs/architecture/decisions/adr-0013-use-ioref-for-state.md)

## Context

In [adr-0007](/docs/architecture/decisisons/adr-0007-SUPERSEDED-mtl-style-for-effects.md) we decided to use
mtl-style for effects. This implied that we would use `MonadState` for state like so:

```haskell
someFunction :: (MonadState s m, HasSomeState s) => m ()
someFunction = ... -- Do something using SomeState
```

Unfortunately MonadState has a significant drawback: We cannot use `zoom` from the lens library
with it. (See [here](https://github.com/ekmett/lens/issues/316#issuecomment-20894162) for more
info).

With the current structure of the game there are _a lot_ of situations where we want to use zoom.

Consider the current structure of a SpawnPoint which has two timers:

```haskell
data SpawnPoint = SpawnPoint
  { __position :: Position   -- ^ Position to spawn at
  , __direction :: Direction -- ^ Direction the spawned entity should face
  , _spawnTimer :: Timer     -- ^ Interval between spawns
  , _loopTimer :: Timer      -- ^ Interval between loops
  } deriving (Eq, Show)
```

We want to be able to call `Timer.step` on both timers. Without zoom we have to do something
like this:

```haskell
stepSpawnPoint :: (Time m, MonadState s m, HasSpawnPoint s) => m ()
stepSpawnPoint = do
  spawnTimer' <- use spawnTimer
  newSpawnTimer <- Timer.step spawnTimer'
  spawnTimer .= newSpawnTimer

  loopTimer' <- use loopTimer
  newLoopTimer <- Timer.step loopTimer'
  loopTimer .= newLoopTimer
```

With zoom we can greatly simplify the code:

```haskell
stepSpawnPoint :: (Time m, MonadState s m, HasSpawnPoint s) => m ()
stepSpawnPoint = do
  zoom spawnTimer Timer.step
  zoom loopTimer Timer.step
```

This is very desirable! But it doesn't work with `MonadState` :(

There is apparently a way to work around this using some combination of `Functor`, `Zoomed` and
`Zoom` in the typeclass constraints as outlined [here](https://stackoverflow.com/a/30831627) but
I don't understand how it works well enough to be confident in using this approach.

We could also define a specific `zoomSpawnPointToTimer`, `zoomGameStateToCar`, `zoomAtoB` function
for each zoom we want to do as outlined [here](https://stackoverflow.com/a/41131823) but given
the amount of zooming we are going to do I'm not a fan of this approach.

With all this in mind I think it makes sense to use `StateT` directly. I have a feeling
this may eventually lead to a completely different approach but for the moment it seems
to be a reasonable way to solve the problem.

## Decision

We're using a concrete `StateT` instead of `MonadState`

## Consequences

- This invalidates [adr-0007](/docs/architecture/decisions/adr-0007-SUPERSEDED-mtl-style-for-effects.md)
- The top-level `Main` and `CrossyToad` modules will be more complicated as they need to manually unwind
  the stack
- We can use `zoom`!

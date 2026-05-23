# Broadcast Messages

## Context and Problem Statement

Heroes can kill nearby enemies on a certain range, but there is no central place in the game that knows every hero position on the board at any time. Each one of them is the source of truth.
In order to do that a hero must broadcast the intent to the rest of players.
How to send messages to all heroes at once?

## Decision Drivers

* Less possible changes
* Performance is not a concern

## Considered Options

* `:pg2` - Implement broadcast on top of an `:all_heroes` group
* Registry for PubSub
* Manager GenServer - Stores and monitors heroes PID
* `Supervisor.which_children/1`

## Decision Outcome

Chosen option: "`Supervisor.which_children/1`", because it comes out best.

## Pros and Cons of the Options

### `:pg2`

* Good, because it's designed for such use cases
* Good, because it's optimized for speed
* Bad, because it's an extra application in the release

### Registry for PubSub

Example: https://hexdocs.pm/elixir/Registry.html#module-using-as-a-pubsub

* Good, because it allows multiple use cases
* Bad, because of some extra complexity

### Manager GenServer

* Good, because it's simple and focused
* Bad, because it reimplements existing solutions

### `Supervisor.which_children/1`

Docs: https://hexdocs.pm/elixir/Supervisor.html#which_children/1

* Good, because it can be done with existing parts of the system
* Bad, because of uncertainties if system was to be scaled

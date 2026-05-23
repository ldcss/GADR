# Temporary Heroes

## Context and Problem Statement

Heroes are now permanent, which means they are always restarted.
Should they be?

## Decision Drivers

* A Hero must not exist on the system once the player leaves the game (normal exit)
* Restoring them from failures is not a requirement but nice to have
* Project is not finished, lacks most important features

## Considered Options

* Restart `:temporary` - regardless of the supervision strategy any termination (even abnormal) is considered successful
* Restart `:transient` - child process is restarted only if it terminates abnormally

## Decision Outcome

Chosen option: "Restart `:temporary`", because it has the minimum impact.

## Pros and Cons of the Options

### Restart `:temporary`

* Good, because it works with current design of the system
* Bad, because it doesn't allow to continue playing the game in case of failure

### Restart `:transient`

* Good, because it allows recovering from failures
* Bad, because it requires making changes to register heroes with dynamic names (restarting a process assigns a new PID)
* Bad, because restoring a problematic state can cause more issues

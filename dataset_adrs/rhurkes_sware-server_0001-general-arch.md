# sware's general architecture should be a single process, multi-threaded mono-repo

* Status: accepted
* Date: 2020-04-14

## Context and Problem Statement

There are three  major decisions we need to make that have an impact on what technologies are used and how the code is implemented:
- Should this be a single process or multiple processes?
- Should distinct pieces of functionality live in separate GitHub repos?
- How many threads should be used?

## Decision Drivers

* I want to use RocksDB in any solution, but RocksDB does not support multiple processes unless all of them are readonly. Since I need a writer, I am forced into having all reads/writes happening on a single process.
* Multiple repos ended up being a distributed monolith, and I needed a `wx-shared` repo to hold shared functionality and domain structs. I do not want to deal with this again.
* ZeroMQ was fun to learn, but the serde and IPC added a layer of complication whenever I tried refactoring or troubleshooting.

## Considered Options

* Old way: multi-repo, multi-process
* Single-repo, multi-process
    - This could be mono-crate or use multiple crates in a workspace
* Single-repo, single process

## Decision Outcome

Chosen option: `Single-repo, single process` because it keeps things simple and allows me to focus on writing new features and making the existing feature more bulletproof instead of trying to wire up multiple repositories/processes.

### Positive Consequences

* Reduced complexity is easier to read and understand
* Reducing the repos involved allows the shared library to just be a module that all other code uses
* Removing multiple processes from the solution means that IPC isn't needed, which means all of the code around ZMQ transport and serde can be removed. This greatly simplifies interactions with the store.

### Negative Consequences

* Unable to scale horizontally if needed, however RocksDB makes that difficult to do anyways
* I don't get to learn with functionality like crate workspaces, ZMQ, or MPSC queues
* Have to rebuild RocksDB when making changes to unrelated things like API routes

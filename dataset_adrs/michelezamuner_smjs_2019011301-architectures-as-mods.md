# Local architecture interfaces


## Context

Sloth machine applications need to support any type of processor architectures, that can be loaded and chosen by users when running the applications. The architecture with which to run the virtual machine will be selected at launch time: for example, a command-line application could be used like:
```
$ sm --arc=sma program_file
```


## Decision

We will support adding new architectures as mods, or user-side plugins, that are provided by the user without needing to rebuild the application.

We won't provide integration tests with real code targeting specific architectures in any Sloth Machine suite, because they become actually independent from the architecture, and as such they cannot know about any specific architecture, not event in tests, where we might just use stubs instead. Integration tests for architectures must be included in the specific architecture packages.

### Local architectures

The local architecture loader, which is selected by an adapter to load architectures from local files, will load an architecture object from the module file.

This architecture will implement the `<Architecture>` domain interface, thus providing a `getInterpreter(<System>)` method, taking a System to return an Interpreter for that specific architecture.

The module file must be named `lib`, and must be located directly inside a directory called with the name of the architecture.

The architecture module is only allowed to depend on the `smf`, and no other external packages, because the environment where the architecture module is loaded is controlled by the suite loading it, for example the Sloth Machine virtual machine.


## Status

Proposed


## Consequences

The architectures supported by any Sloth Machine suite are not limited to the ones built within the suite itself.

It's not necessary to change nor rebuild the application to add support to new architectures.

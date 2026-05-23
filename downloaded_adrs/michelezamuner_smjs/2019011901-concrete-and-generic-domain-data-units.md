# Concrete and generic domain data units


## Context

We've been thinking of defining abstract concepts of `DataUnit` and `Data`, so that `DataUnit` shares the interface with `Data`, and this interface contains a lot of methods, for example for comparison, arithmetic, etc. However, upon reviewing the usage of these concepts in the other domain modules, it's been evident that all these complex features weren't actually needed.

In addition to this, the idea was that the domain defined only the interfaces for the data units, and then each architecture provided implementations for them. This introduced the annoying problem of having to let the architecture control the loading of programs, because programs would need to contain the actual data units defined by the architecture. This was leading to the definition of a `StringLoader` in the framework domain, where programs were considered just strings (so independent from the specific architecture), and then also of an architecture specific program loader, using the given string loader to translate string programs to data unit programs: this was making the domain, and both the logic and the structure of the system, quite complicated.


## Decision

We'll agree that, whatever special data implementation an architecture may come up with, it must be base on the concept of Byte, because that's what programs are ultimately made of: thus, our data unit will be a byte (actually a runtime-independent implementation of it).

Additionally, since domain framework modules only need the concept that data units are laid out in sequences to create bigger chunks of data, we'll define `Data` as just a list of `DataUnit`. No other feature will be needed, no comparison, no arithmetic, etc.

Also the concept of `Size` will be simplified to become just an integer (again a runtime-independent implementation of it), and the concept of `Address` will be moved from the program module ot the data module, since we can talk about the address of a data unit within a chunk of data.


## Status

Proposed


## Consequences

Architectures are still free of defining more specific implementations of data, for example with Words, Doubles, etc., just these definitions won't be used outside of the architecture code.

The data module is much more simple, and the program loader is now completely independent from the architecture, greatly simplifying the design.

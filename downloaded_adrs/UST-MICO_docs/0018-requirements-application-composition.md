# Requirements regarding the Composition of Applications


## Context and Problem Statement

We want to have clear and simple requirements when it comes to the way applications can be created in the user interface.

## Decision Drivers

* MUST be compatible with Lombok

## Considered Options

* Applications cannot be composed out of other applications. Applications can only be created using single services.
* Applications can be part of other (new) applications. Therefore inheritance between MicoApplication and MicoService is necessary. This would mean difficulties with Lombok.

## Decision Outcome

Chosen option: the first option, since we want a simple solution, in order to have the system running as soon as possible.

### Positive Consequences

* Lombok can be used.
* Better code quality.

### Negative consequences

* Applications cannot be created using other existing applications.
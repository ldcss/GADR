# 3. Adopt hexagonal architecture

Date: 2018-12-27

## Status

Accepted

## Context

Adopting the [Domain-driven design](0002-adopt-ddd-approach.md) approach requires isolating domain elements (i.e.
aggregates and services) from the infrastructure (i.e. application clients and persistence).

## Decision

`menu-generation` application will adopt [hexagonal architecture](https://en.wikipedia.org/wiki/Hexagonal_architecture_(software)),
as it aims to provide this separation.

## Consequences

To isolate domain elements from infrastructure, the `menu-generation` package structure will be split in two main categories:

* the core hexagon, consisting of different base packages (e.g. `org.adhuc.cena.menu.ingredients`) that will contain
every class that compose an aggregate and its related domain and application services and repositories. Those packages
won't depend on any infrastructure implementation, but rather on interfaces providing the contracts to be implemented by
infrastructure services.

* the outer hexagon, consisting of a `org.adhuc.cena.menu.port.adapter` base package with different subpackages containing
the different infrastructure services implementation, known as adapters, implementing the interfaces defined in the
aggregate packages and the clients using the application services. Thus those adapters may be splitted into either
incoming adapters (e.g. REST controllers) or outgoing adapters (e.g. database specific implementations).

The core hexagon will provide public interfaces only for the infrastructure services to be implemented and application
services to be used by the incoming adapters. Domain services won't be exposed outside of the aggregate packages, to
enforce application services usages, thus providing a unified interface to communicate from the outer hexagon to the core
hexagon.

Incoming adapters must use application services to access to the application features. It is not allowed for those
adapters to bypass those application services and get direct access to the outgoing adapters.

Inversion of control will be used to inject infrastructure implementations dependencies into the services defined in the
core hexagon.

Different bounded contexts will have their dedicated core and outer hexagon, to enforce boundaries. Communication between
bounded contexts will consist of an outgoing adapter from the upstream context to call an incoming adapter from the
downstream context.

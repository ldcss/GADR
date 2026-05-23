# 2. Structural Patterns

Date: 2019-02-02

## Status

Accepted

## Context

A layered architecture allows us to clearly separate responsibilities for each part or our application. We also ensure that no unwanted access to a layer is granted, if we follow our layered architectural guidelines. 

## Decision

The `AdventOfCodeService.class` not only provides specific instances of a requested Day by a _factory method_, it also serves kind of as a _Facade_ to hide the underlying system's complexity (the specific solutions for each Day's puzzle). It exposes public methods to be used by the `AdventOfCodeController.class` to retrieve requested results for puzzles.

In the same manner, one or several service classes will manage the interaction with the repository/persistence layer in the future.

The `AdventOfCodeController.class` provides the API for a RESTful communication with our Spring application. It communicates only with the service layer and shall contain no business logic. This is to be done in the service layer. The controller is the real _Facade_ to our subsystem: the entry point to the application.

To ensure that we follow our own architectural guidelines, we will set up ArchUnit tests for each decision made here.

## Consequences

See what is described in the context of this ADR.

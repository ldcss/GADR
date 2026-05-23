# 1. Creational Patterns

Date: 2019-02-02

## Status

Accepted

## Context

We want to have a common contract for the way that our specific solutions for each Day behave in the application context. For that, we will enforce the implementation of specific methods. In addition, we want to have an easy access to those specific implementations and will rely on Spring's application context.

## Decision

The interface `Days.class` is part of an _Abstract Factory_ for concrete Day classes, allowing us to use polymorphism for days. The instances for the specific Days are created and provided by the Spring context upon annotating the specific days with `@Component` and making them implement the interface, so it is not a real factory - just part of it. 

In the `AdventOfCodeService.class` (think of it as a _Facade_ to the subsystem), a `List<Days>`, which is populated by Spring with instances of the specific Days, is used by a _factory method_, or _repository method_ if you want to name it that way in order to find the correct instance for a specific requested day. Note that `AdventOfCodeService.class` is in our case part of the creation, but has also Structural Patterns characteristics. We will cover that more deeply in a corresponding ADR section.

## Consequences

Any new requirements to a Day must be passed on to every specific Day implementation.

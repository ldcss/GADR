# Hexagonal Architecture - Clean Architecture variant
To improve the clarity and testability of the code, we organize the codebase according to the Hexagonal Architecture 
model. With this model, we aim to separate the influences of frameworks and libraries from our business logic and create 
a clear interface between them.

From the available variants of the architecture model, we choose the 
[Clean Architecture from Robert Martin](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html).

## Context and Problem Statement
- How can we maintain a clean design?
- How will we be able to maintain our architecture iteratively in accordance with the TDD practice?

## Decision Drivers
* We employ TDD, which favors small iterations.
* We aim to implement full Continuous Delivery.

## Considered Options
* No model (current)
* [Hexagonal architecture](https://en.wikipedia.org/wiki/Hexagonal_architecture_(software)) and variants 
* [Model-View-Controller](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller) and variants

## We choose Hexagonal Architecture over MVC
While the MVC is still the go-to architecture in the industry its drawbacks and pitfalls are well-documented for over a 
decade. Hexagonal architecture has proven superior both in theory and in personal experience. Its main gains over MVC are:
- Separation of concerns and testability: Imposing clear boundaries ensures a modular design
- Principle of locality: Objects that *change* together are found near each other  

Of the different HA-variants, the Clean Architecture by Robert Martin is the most specific. By explicitly specifying the
directional responsibilities of the different parts of the interface ("arrows always point towards the boundary") it 
allows the boundary to be independent of the adapters as well as the business logic.  

### Positive Consequences
* improves testability by separating framework specifics
* adds clarity to the codebase by introducing explicit boundary-interfaces
* principle of locality: Items closely related should remain close together.

### Negative Consequences <!-- optional -->
* boilerplate and formality in the simplest cases might be disproportional (as compared to the current lack of modeling)

## Pros and Cons of the Model-View-Controller Architecture
* (+) Simple 
* (+) Well known
* (-) Advocates the [Anemic Domain Model](https://www.martinfowler.com/bliki/AnemicDomainModel.html) anti pattern.
* (-) Separates closely related concepts into remote locations based on irrelevant technical similarities

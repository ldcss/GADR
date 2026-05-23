# 5. ViewModel parameters should be injected by Dagger

Date: 2019-09-28

## Status

Accepted

## Context

We want to unit test the ViewModel classes but the ViewModel class itself creates a specific UseCase and is using hardwired Rx Schedulers.
This makes it impossible (or unnecessary hard) to mock the dependencies used by the ViewModel.

## Decision

The creation of a UseCase instance is moved to a factory class. The factory itself is passed to every ViewModel class (using an interface for inversion of control).
For unit testing we simply can mock the factory.
As the factory only holds the creation of a specific UseCase, it should be enough to only create a single factory for all UseCases.
In the future it could be necessary to create additional factories if a single one is polluted to much.

The Schedulers are also passed as parameter to be able to mock them too.

## Consequences

All ViewModel classes have to be refactored. They no longer should create a UseCase directly but only through a factory (new parameter).
Nor should they use Scheduler types directly
DI and the ViewModelFactory also has to be changed, to inject the UseCase factory into every ViewModel upon creation.
It is no longer necessary to pass the repository to every ViewModel, which is a good thing (as only the UseCases need access to the database).
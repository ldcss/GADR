# Interactor handling concurrent requests


## Context

An application can generally handle concurrent requests coming from different device adapters.

If the interactor's dependencies don't depend on the request parameters, the same interactor instance can be used for every request. In some cases, however, some of the interactor's dependencies depend on the details of the request, for example the concrete presenter to be injected in the interactor in place of the presenter interface depends on the output model of the specific request, i.e. on the specific device adapter that is handling the current connection.

In some cases interactor's dependencies might have an identity, for example services with a specific configuration, like loggers, database drivers, etc., that shouldn't be created anew every time they're injected into the interactor.

If the same instance of an interactor is shared, then, we'd also face concurrency issues, because different requests would be sharing the same resource.

Finally, different requests might be coming in parallel, and routing to the interactor should be handled in a proper manner.


## Decision

From a design point of view, each request can require a different concrete presenter to be used, meaning that a different interactor should be used in general for each request. This means that all application components should in theory be duplicated for each different requests: controllers, presenters, views, interactors and interactors' dependencies.

There are two main drawbacks to this, one related to design, and the other to performance. From a design perspective, we might need to share dependencies with the same identity (like services with a specific configuration) among different interactors. If we assume that all dependencies are injected, we can solve this by properly configure the DI container, so that it resolves certain references always to the same instance, so that each time a new interactor is created, the same service is passed to the constructor.

The design of the system should then be independent from any performance issue. For example, if we decide that the construction of certain dependencies is too expensive, we can replace some of these services with a proxy or decorated version that does some caching. Whatever solution we decide to use, however, it shouldn't impact the design of the system.


## Status

Proposed


## Consequences

The design is greatly simplified because we remove the requirement of the application layer to be unique for every connection, and thus we remove the need to have a broker component in the system.

Design and performance issues are kept properly separated.

Service applications are even closer to native applications in terms of design, because the only difference is the number of duplications of the same application (no duplication/one instance in native applications, several in service applications), with the high level design structure staying the same.

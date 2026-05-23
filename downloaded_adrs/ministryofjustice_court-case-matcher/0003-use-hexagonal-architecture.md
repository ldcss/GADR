# 3. Adopt hexagonal architecture

Date: 2021-08-20

## Status

Accepted

## Context

Historically the `court-case-matcher` has only had to deal with data from one source (Libra) and output to one other (`court-case-service`). With the introduction of Common Platform as a source and the corresponding changes at the `court-case-service` to support this, our single source, single sink data model requires significant refactoring. Doing this in small steps without making breaking changes is impossible with the current multi-purpose data structures. 

## Decision

To make accepting and posting multiple different data formats easier the decision was taken to precede this work with a major refactor to explicitly separate out the incoming, domain, and outgoing data models using the [hexagonal/ports and adapters](https://en.wikipedia.org/wiki/Hexagonal_architecture_(software)) architectural pattern. This will allow each interface to vary independently of the others allowing us to make small, isolated, non-breaking changes.

This pattern has the disadvantage of requiring extensive tedious mapping back and forth between superficially similar objects. There are libraries that will do this automatically but we've decided not to go down this route, at least initially, as previous experience with these libraries leads us to believe they ultimately produce more of a maintenance headache than they save. Manual mapping is tedious, but it's also simple and easy to understand and when it fails it does so in an obvious and easily debuggable way.  


### General principles:
- The domain model is pervasive and may be passed freely between services
- Interface models should only exist on the periphery of the application and should not be passed around. This is to localise tight coupling to external interfaces.
- Interfaces can know about the domain model but the domain model should never know about an interface. This is to prevent tightly coupling the domain model to interfaces.

### In practice:
- The domain model lives under [`java/uk/gov/justice/probation/courtcasematcher/model`](java/uk/gov/justice/probation/courtcasematcher/model). This model should be used for all internal logic and operations.
- Each external interface should provide its own POJOs, for example [`java/uk/gov/justice/probation/courtcasematcher/messaging/model/libra`](java/uk/gov/justice/probation/courtcasematcher/messaging/model/libra) and [`java/uk/gov/justice/probation/courtcasematcher/restclient/model/courtcaseservice`](java/uk/gov/justice/probation/courtcasematcher/restclient/model/courtcaseservice)
- All port and adapter model instances should provide an `asDomain()` method to convert themselves to the domain model
- All port and adapter models should provide a static `of(<DomainModel> obj)` method to convert from the domain model to the interface model
- Prefixing interface models makes it easier to spot them and differentiate them (e.g. [`CCSCourtCase`](java/uk/gov/justice/probation/courtcasematcher/restclient/model/courtcaseservice/CCSCourtCase.java))

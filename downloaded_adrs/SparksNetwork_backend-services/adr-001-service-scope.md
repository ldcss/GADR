# ADR 1: Service Scope

* Jeremy Wells
* Frederik Krautwald

## Status

**proposal** | ~~accepted~~ | ~~depreciated~~ | ~~superceded~~

## Context

### Definitions

* **Function**: A JavaScript function
* **Service Function**: A complete function that takes messages from a 
messaging service
* **Topic**: A name within a messaging service that any service can listen to
* **Message**: A message that is distributed to topic listeners
* **Command**: A message indicating a user action

The first task implementation required a service function that takes a command, transforms the data, and then writes that data to Firebase. In order to make
sure that other tasks know about the data change the change then needs to be
broadcast on to another topic.

The above means that the function has two responsibilities, writing the data
and broadcasting a new message. Writing the tests for such a service function
showed that mocking two targets is hard and causes complexity.

## Options

1. Have a single service that receives Commands for a particular domain object,
makes transformations, then writes to Firebase AND broadcasts to another topic.

**Pros**
* Service is fast
* If you look at the service you can see everything that happens

**Cons**
* Harder to write tests
* Single service with dual responsiblities
* Changes to the way data is stored need to be reflected in many services

2. Have 2 services. Service 1 will recieve Commands for a domain object, make
transformations and broadcast to other topics. Service 2 will read messages from
a particular topic and write to Firebase.

**Pros**
* Services have single responsibility
* Testing is easier
* Firebase service can be reused

**Cons**
* Commands take longer to run

## Decision

Option 2, use 2 services. We will name these *business* services and *repository*
services.

## Consequences

* Business services that receive commands and produce data should NEVER save 
that data. Instead they MUST rebroadcast the changes as ONE OR MANY messages 
to other topics.
* Repository services that store data MUST NOT rebroadcast that they have stored
the data.
* Broadcasting to a repository topic is SYNONYMOUS with storing that data. Any
listeners to that topic that are NOT repository services MUST consider that
data stored.
* If a repository service enters a failure mode the above rules mean that data
sent to the repository topic is still considered saved, and the normal response
to a failure mode is to fix and reprocess existing messages.
* As a consequence of the above NO service that listens to repository topic
 broadcasts can rely on the state of the underlying data store of a repository
 service.

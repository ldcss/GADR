# ADR-002: How to generate record IDs

* Jeremy Wells

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
* **Repository service**: A service that reads messages and saves data to some
kind of store.
* **Business service**: A service that reads *Command* messages and performs business logic transformations on the data, eventually sending further messages.

When data records are created at some point a unique key for the record needs to be generated.

Usually we rely on the database to do this work. A database can be set up to generate an incrementing id or a uuid.

Firebase itself will generate a unique key for the data that is pushed. However, firebase unique keys are generated on the client side, and indeed the code is even available here: https://gist.github.com/mikelehen/3596a30bd69384624c11

Because the data being generated is put onto a topic before being committed to a database by a repository service the data should have a key before being sent to the data topic.

## Options

Options for generating keys:

1. Generate the key during a push operation in the firebase repository and send the key to interested parties with an update message.

**Pros**
* Same key generation as current backend

**Cons**
* Goes against ADR-001, repository services should NEVER broadcast to topics.
* Means dealing with extra messages

2. Generate a UUID in the business services that respond to Command messages.

**Pros**
* UUID library is easy and fast
* UUIDs have a very low chance of collision

**Cons**
* We have to generate them
* UUIDs are very long

3. Generate a key using the Firebase algorithm

**Pros**
* Keys are time orderable
* Code is available and easy to read

**Cons**
* We have to generate them
* Keys have a higher probability of collision

4. Use the ID attached to the Kinesis record

**Pros**
* UUID format, low chance of collision
* Means that there is a tracking mechanism between the Command message and the stored data.

**Cons**
* Not as obvious what is happening
* Very long
* Unknown probability of collision / uniqueness

## Decision

## Consequences


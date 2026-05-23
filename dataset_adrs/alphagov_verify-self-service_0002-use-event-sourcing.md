# 2. Use Event Sourcing

Date: 2019-03-08

## Status

Accepted

## Context

The self-service application needs to provide a facility where we can view and
audit the events that occur within it. For example, if we become aware of
a security incident where a user's account has been compromised we need to be
able triage possible damage by investigating how that account has used the
service. 

## Decision

The app will be built using the principle of Event Sourcing:

>Event Sourcing ensures that all changes to application state are stored as a sequence of events. Not just can we query these events, we can also use the event log to reconstruct past states, and as a foundation to automatically adjust the state to cope with retroactive changes.

When a change is made an event will be written into an events
table that fully represents that change. With the events table it will be
possible to view the changes that have occurred in the system.

The primary aim for this implementation will be to be able to view historical
changes to the system, but it should also be possible to use the events table to
recreate the previous states of the system.

This behaviour is implemented 'natively' in ActiveRecord and is heavily inspired
by Kickstarter's [Event Sourcing made Simple](https://kickstarter.engineering/event-sourcing-made-simple-4a2625113224)
and [its demo](https://github.com/kickstarter/event-sourcing-rails-todo-app-demo/)

All distinct events will be defined as Ruby classes that inherit from an [`Event`](app/models/event.rb) class. 
They will be stored in the `events` table and Rail's Single Table Inheritance will used to identify the class of each event.

Aggregate objects will inherit from an abstract class [`Aggregate`](app/models/aggregate.rb).
When an event is saved a callback will be used to update an aggregate object
(equivalent to a Calculator object or function).
Aggregates should not be changed unless told to by an event.

Events will associate themselves to an aggregate using a polymorphic association.

When the state of an object needs to be changed the Aggregate shall be used.

## Consequences

- All actions that change the configuration provided to the Verify Hub should be
    recorded using an event object
- Validations for actions should be placed on event objects
- Aggregates shouldn't be updated unless told to by an event

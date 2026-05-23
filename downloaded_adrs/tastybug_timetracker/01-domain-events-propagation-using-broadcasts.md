# 1 Domain Event Propagation Using Broadcasts

## Status

Accepted

## Context

Whenever a domain related events happens (checkin, checkout, project update etc.), a number of 
interested components are to be notified. Those components might show warnings, update the UI etc.
Unfortunately, not all components are being executed in the main process all the time, so Otto 
events will not reach them. There needs to be a mechanism that reaches background services.

## Decision

Jede an einem Domain Event interessierte Komponente stellt einen BroadcastReceiver bereit, der 
mittels Intents informiert wird. Alle DomainEvents werden per Broadcast verteilt.

Alle Events sollen haben die Intent-Kategorie `com.tastybug.timetracker.LIFECYCLE_EVENT` sowie eine
Action, die das Domainobjekt beschreibt: `com.tastybug.timetracker.PROJECT_CHANGE` oder 
`com.tastybug.timetracker.TRACKING_RECORD_CHANGE`.
In den Extras des Intents sind die UUIDs der betroffenen Entities abgelegt.

Every component interested in Domain Events provides a BroadcastReceiver that will be notified via
Intents. Every Domain Event will be propagated using Broadcasts.

All events have category `com.tastybug.timetracker.LIFECYCLE_EVENT` an an action that describes the
affected object type. Currently this is `com.tastybug.timetracker.PROJECT_CHANGE` and 
`com.tastybug.timetracker.TRACKING_RECORD_CHANGE`. UUIDs of affected objects can be taken from
intent extras.
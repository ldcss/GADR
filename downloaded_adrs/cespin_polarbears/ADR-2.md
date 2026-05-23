# ADR 2. Use of async communication between Location Inventory component and (External) Fridge/Toast APIs for reconciliation

## Status
Accepted

## Context
When the delivery people deliver meals to the smart fridges or kiosks, they update the system with the delivery information (the location and the meals).
To determine the inventory at a certain location, the Location Inventory component has to reconcile between the two sources of truths: 1) the information fed
to the system by the delivery people 2) the inventory reported by the external Fridge/Toast APIs.

Upon receiving the delivery confirmation, the Location Inventory component can 1) query the Fridge/Toast APIs and update its data upon synchronous 
reconciliation 2) asynchronously query the Fridge/Toast APIs and reconcile.

## Decision
We will use asynchronous communication between the Location Inventory and the External Fridge/Toast APIs for reconciliation.

Waiting for the synchronous reconciliation at a location will increase the time delivery people spend at a location and 
even may not be possible if the External Fridge/Toast Inventory APIs are down for some reason.

## Consequences
If the delivery information and inventory reported by the external API's match, no further action needs to be taken.
If the delivery information and inventory reported by the external API's does not match, admin users will be notified to take manual action.
At worst case, we might need to redeliver to the same location, but since these are only rare cases, overall, our delivery times will improve.

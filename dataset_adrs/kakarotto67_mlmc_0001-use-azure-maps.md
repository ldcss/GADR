# Use Azure Maps instead of Google Maps

* Status: [accepted]
* Deciders: [[@kakarotto67](https://github.com/kakarotto67)]
* Date: [2019-09-10]

Technical Story: [Change map provider to Azure Maps](https://github.com/kakarotto67/mlmc/issues/3)

## Context and Problem Statement

Map have to be added to the product so missiles can be shown there at real time.

## Decision Drivers

* Easy to use
* Some knowledge already exists
* Native for other product technologies

## Considered Options

* [Google Maps](https://developers.google.com/maps/documentation/)
* [Azure Maps](https://azure.microsoft.com/en-us/services/azure-maps/)

## Decision Outcome

Decided to use Azure Maps since

* They are native to Azure and .NET which are used for the product
* They are well integrated with Azure SignalR that is going to be used for real-time notifications
* I got some experience with Azure Maps already

### Positive Consequences

* Implementation will be faster and easier in this particular case

### Negative Consequences

* I planned to get some Google Maps API knowledge as well

## Links

* n/a

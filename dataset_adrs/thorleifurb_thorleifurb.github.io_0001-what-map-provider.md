# Which map / routing library provider to use

* Status: accepted
* Deciders: Þorleifur Bjarnason
* Date: 2019-12-26

Technical Story: Implementation of web client with map interface for viewing and analyzing traffic cost (time/distance) for defined group of people based on workplace location. 
We need map and routing engine to both provide the following:
* calculation of time and distance between two addresses.
* drawing of route between two addresses. 

## Context and Problem Statement

We want to base our user interface on map software and calculations in routing engine.
Which map provider should we use?

## Decision Drivers

* Since this is research project of using free software, we require that the map usage MUST be free.
* Required is that the map has supporting library to generate and draw actual routes between two points.
* Required is that the map has supporting library or methods to calculate actual routes and time for driving, cycling and walking between two points.

## Considered Options

* [`Google Maps`](https://maps.google.com), with services provided by [`Google location api` and `Google directions api`](https://cloud.google.com/maps-platform).
* [`Openstreetmap`](https://openstreetmap.org), with services provided by [`OSRM routing engine`](http://project-osrm.org/). 
* [`ja.is`](https://ja.is/kort/) with services provided by [gagnatorg.ja.is](https://gagnatorg.ja.is/).

## Decision Outcome

Chosen option: "[`Openstreetmap`](https://openstreetmap.org) with service provided by [`OSRM routing engine`](http://project-osrm.org/)", because 
* Only option that is free for implementatation and does not require registration of any kind.
* The product is research only, and not intended to installation to production.
* `ja.is` did not provide any documentation about using routing engine and tiles, so it cannot be considered.

We accept that usage of `Google maps` would be lot easier to implement. `Google maps` does host and maintain all required api's and geographical data.
`Google directions api` seems to have better geographical data for Iceland than we see in accessable `OSRM routing profiles`
If product was intended for production we must add in our decision conideration about the price of using `Google maps` compared with the cost of hosting and maintaining `OSRM routing engine`.

### Positive Consequences

* We do not need to pay for usage of map.

### Negative Consequences

* We need to install, host and maintain `OSRM routing engine`.
* We need to update and maintain routing info on local `OSRM routing engine` to avoid outdated map data and route calculations.

## Pros and Cons of the Options

### [Google Maps](https://maps.google.com)

* Bad, because it is not free to use routing engine.
* Bad, because it is not free to use map without limitation. Requires credit card registration and profile.
* Good, because of popularity and features [comparison from similartech](https://www.similartech.com/compare/google-maps-vs-openstreetmap)
* Good, because it contains better information, and can rely on real time traffic.
* Good, because it contains large community and large number of data providers
* Good, because no hardware / software needs to be installed and hosted for routing engine.

### [Openstreetmap](https://openstreetmap.org)

* Good, because it is free to use routing engine
* Good, because it is free to use map without limitation
* Bad, because of popularity and number of data providers (https://www.similartech.com/compare/google-maps-vs-openstreetmap)
* Bad, because it needs installation locally on `OSRM routing engine` and maintenance on routing engine data.
* Bad, because it costs hardware for hosting routing engine.

### [ja.is](https://ja.is/kort/)

* Bad, because map used is `Openstreetmap`, so why not use `Openstreetmap` directly.
* Bad, because documentation does not expose any type of subscription to any routing api, so no routing api is provided.
* Good, because tiles files of Iceland is outstanding. Both for satilite and street view.
* Bad, because tiles files of Iceland does not seem to be exposed for usage by third party.

## Links

* Reference [compare of `Google maps` vs `Openstreetmap` from similartech](https://www.similartech.com/compare/google-maps-vs-openstreetmap)

<hr>

Template: Licence [CC0](https://creativecommons.org/share-your-work/public-domain/cc0),
provided by [Architectural Decision Records](https://github.com/adr/madr)

<hr>

Content of decision: Copyright © 2020 Þorleifur Bjarnason, All Rights Reserved.

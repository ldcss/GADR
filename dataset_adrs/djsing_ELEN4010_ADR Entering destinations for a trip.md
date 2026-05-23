# 1. Entering locations/destinations for a trip

Date: 2019-04-09

## Status

Accepted 

## Context

Destinations need to be entered into a trip somehow. The two most obvious choices seem to be by typing (some kind of auto-completion feature) or by clicking directly on a map, to set markers. These paradigms are the dominant ones in most existing APIs and site/map websites.

## Decision

We will aim to support both autocomplete AND clicking on the map. This would be the most convenient for users of the site. 

## Consequences

Two methods of adding destinations will mean two (or more) additional functions in code, more complexity and added maintenance and testing. The methods will both need to work on Mobile/Responsive well.

 * Vastly better UX
 * Additional UI work
 * Additional Testing
 * Additional Code
 * Additional code complexity

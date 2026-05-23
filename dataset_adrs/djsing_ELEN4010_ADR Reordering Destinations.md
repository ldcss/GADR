# 1. Reordering Destinations

Date: 2019-04-09

## Status

Accepted 

## Context

A list of destinations should be reorderable, not fixed

## Decision

A trip is made up of a list of destinations. This list should be able to be reordered, on the main site or the mobile version of the site. Draggable would be the best, but a button for moving an extry up and down will also work.

## Consequences

It may not be best to write the trip to the database everytime a destination is reordered. Perhaps better to store the trip locally, and only write to the database once (with a 'Save' button)

 * Affects planned log functionality
 * Affects groups (others on trip)
 * Need to add JQuery UI or specialised Javascript to enable reordering

# 2. Track Municipalities

Date: 2021-02-15

## Status

Accepted

## Context

We need the geometries (boundaries) of a municipality to derive the municipality of road segments that do not have an associated left or right street.
We can't rely on the geometries used in the municipality registry because they are (1) not exposed and (2) they do not match the boundary along which road segments have been split up.
When the boundaries in the municipality registry change, one can't expect all segments to change as well.

## Decision

We keep track of municipalities as defined in the legacy road registry database because those are the ones along which road segments have been split up.
We use `ImportedMunicipality` as the main event to track this. It contains all the data we need for now. This event is assembled while extracting events and imported during deployment.

## Consequences

We can now derive the municipality a road segment belongs to using the correct boundaries.

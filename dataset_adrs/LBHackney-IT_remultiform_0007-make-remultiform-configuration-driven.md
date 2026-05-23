# 7. Make remultiform configuration driven

Date: 2019-10-30

## Status

Accepted

## Context

We want to build a reusable React library, that generates multipage forms
quickly. We need logic that extends beyond simple "show this element on this
page", such as conditional logic for displaying sections dependant on values in
other sections, and to skip pages based on values elsewhere in the journey.

## Decision

We will build remultiform to export a series of small orchestration components.
We will pass the entire multipage form configuration in via props to those
orchestrators. The configuration should be agnostic of the set of components it
might receive.

## Consequences

We believe that separating the logic to render forms and routing to subpages of
multipage forms from the definition of those forms will speed up development of
multipage forms in general.

Putting logic into that configuration adds some complexity in building type
definitions for that configuration that is generic enough to be reused in many
different situations and agnostic of the components used. We believe that is an
ok trade-off to make in exchange for being able to build new forms more quickly,
than if we had to build each multipage form as a series of pages.

We also believe that the complexity of having generic orchestrators ingesting
varied configuration is a trade-off worth making in exchange for making it
possible to specify varied forms quickly.

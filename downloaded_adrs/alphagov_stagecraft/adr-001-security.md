# ADR 1: Security

# Context

As someone responsible for ensuring accurate data is published by the
government, I need to ensure that people authoring content can only
view and edit things that they own, so that there are no embarrassing
updates published.

We need to ensure that datasets and dashboards can only be edited by
the right people.

We currently have signonotron2 accounts for all of the people using
this application. That will continue to be in place for the future.

We need a way of restricting which signon accounts have access to
different entities within the admin application.

We have tried to model this in various ways.

As someone working at the DVLA, should I have the ability to edit
all of the DVLAs dashboards? The answer to that is no.

We've had some discussions with our user population, but what is
actually good still isn't known at this point. So we are going to
incrementally do this functionality, as a series of vertical slices,
and accept that we will need to refactor, rework and do data
migrations as we learn more about the problem space and how best to
meet those needs.

Initially, we proposed using custom Django Managers in stagecraft to
implement this. We don't think this is the right approach; it smells
too complex.

A simpler start point will be to define the URLs (resources) and
have permissions per resource.

# Decision

Define the matrix of URLs, and map permissions per resource.

# Status

Accepted.

# Consequences

Trading shipping a thing with future technical debt for now.

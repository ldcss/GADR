# 3. Use progressive enhancement

Date: 2018-10-12

## Status

Accepted

## Context

The service manual clearly states that teams should use progressive enhancement
when building services: https://www.gov.uk/service-manual/technology/using-progressive-enhancement

This supports [point 12 of the service standard](https://www.gov.uk/service-manual/service-standard/create-a-service-thats-simple),
which is about ensuring that all users can use the service successfully the
first time they try - including users with accessibility needs.

The service manual is also clear that [internal services should be held to the
same standard as public-facing services](https://www.gov.uk/service-manual/design/services-for-government-users).

Some of the services for prison and probation staff which have been built over
the last couple of years are not progressively enhanced. Without JavaScript
they display no content.

Since these services are in a similar space to our work and have overlapping
user bases with ours (although they are not the only existing services in this
space), we have considered whether we should take a similar approach to them.

## Decision

We will use progressive enhancement for all our user-facing applications.

## Consequences

Our user-facing applications will automatically be more accessible than they
would be if we did not take this approach, and more robust against network
problems.

We are much more likely to meet the service standard, which we will be
continuously assessed against.

We are less likely to be able to reuse code from the subset of
prison-staff-facing services which do not take this approach.

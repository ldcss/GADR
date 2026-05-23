# 8. Move away responsibilities from Civi

Date: 2018-01-10

## Status

Accepted

## Context

eLife has a CiviCRM monolithic system that covers the contacts with key groups such as authors, editors, and newsletter subscribers.

CiviCRM is difficult to develop on, test and debug, and no in-house expertise is available.

CiviCRM is usually in the hands of (several) external consultants, which lack contact with the rest of the architecture.

## Decision

We will push responsibilities away from CiviCRM, favoring [Separate Ways](http://culttt.com/2014/11/26/strategies-integrating-bounded-contexts/) or API-based integration of an external microservice over developing inside CiviCRM.

## Consequences

We should see more services like [civinky](https://github.com/3sd/civinky-service) to satisfy MarComms requests.

We should test these services in isolation from CiviCRM so that they are easier to debug and potentially reuse.

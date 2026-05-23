# Remove support for loading forms via play-partials

* Status: accepted
* Deciders: platui
* Date: 2023-07-17

Technical Story: PLATUI-2393

## Context and Problem Statement

Even though we support loading contact forms via play-partials it's listed as deprecated, should we remove support
altogether?

## Decision Drivers

We want to:

* host the service with less resources
* make the service easier to maintain and change
* avoid lots of work for service teams

## Considered Options

* Option 1: do nothing
* Option 2: remove support for play-partials

## Decision Outcome

Chosen option Option 2, remove support for play partials

### Positive Consequences

* Large reduction in resources needed to run the service. It seems like a very high percent of our traffic comes from
  services using play-partials, where in some cases it appears the partial forms are being loaded on each page view of
  the service rather than when someone wants to use the form.

* There will be a lot less code and test cases to maintain, so it will be easier to make future changes. We don't have
  any of our own services that use play-partials so it's hard to verify changes won't introduce regressions for services
  that still do.

* We can drop our dependency on play-ui and assets-frontend.

### Negative Consequences

* Some work for teams needed. However, it shouldn't require a big change - it will mean changing their existing link so
  rather than revealing a form inline via javascript, it functions as a standard link and takes the user to our hosted
  contact form. Most tricky for services not using play-frontend-hmrc who will have to construct the link themselves.
  However this should be a very small (if any at all) number of services. We'll mitigate this by giving several months
  to make the changes, and monitor traffic so we can ensure teams are notified.

## Links

* [Roadmap entry for service teams](../roadmap/removing-ability-to-load-contact-forms-via-play-partials.md)

# Use data attribute for configuring GTM container in tracking-consent-frontend

* Status: accepted
* Date: 2020-10-22

Technical Story: PLATUI-803

## Context and Problem Statement

In order to simplify the tracking consent build and deploy process and
make integrating with tracking consent less surprising, should
the configuration of the GTM container used by tracking consent be via
data attributes rather than separate bundles?

## Decision Drivers

* The need to keep things simple for service developers
* The need to improve the operability of tracking consent

## Considered Options

* Continue to use separate bundles for each GTM container
* Use a data attribute attached to the tracking consent SCRIPT tag

## Decision Outcome

Chosen option: "Use a data attribute", because based on the benefits listed below the team
believes this is the best way forward.

### Positive Consequences

* The Javascript bundle creation process is simplified.
* The Scala Play routing is simplified
* Only one endpoint needs to be managed in production
* Future additional containers can be supported more easily
* Service developers only have to configure a single URL to tracking consent and use
a data attribute to configure the container.
* The central common configuration repo (owned by a separate team) only requires a single URL to 
tracking consent defining for each environment, rather than one for each GTM container.

### Negative Consequences

* Service developers need to add id="tracking-consent-script-tag" to the SCRIPT
tag when integrating.

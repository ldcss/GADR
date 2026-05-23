# Use an id and data attributes on the SCRIPT tag for configuration

* Status: accepted
* Date: 2020-10-19

## Context and Problem Statement

In the context of the need to inject configuration into the tracking consent snippet (PLATUI-775 and PLATUI-649)
while not wanting to duplicate knowledge of the platform and tracking consent url structure, 
delivering a simple, easily testable solution and delivering a solution that works on IE. How
should the tracking consent script be identified?

## Decision Drivers

* not wanting to duplicate knowledge of the platform and tracking consent url structure, 
* delivering a simple, easily testable solution and
* delivering a solution that works on IE

## Considered Options

* Regular expression pattern matching on SCRIPT src attribute
* id attribute to the SCRIPT tag
* data-id attribute on the SCRIPT tag
* document.currentScript (not supported on IE)

## Decision Outcome

Chosen option: "id attribute", because this is likely to produce a more flexible robust solution than the regex
based solution. The team opted for using id over data-id.

### Positive Consequences

* Solution is more flexible and more likely to withstand changes to url paths, port numbers,
and platform environment naming.
* Solution is simpler and easier to test and verify.

### Negative Consequences

* Service developers will need to add this identifier to the SCRIPT tag albeit with the
   assistance of a helper.
* Very small risk that if an insufficiently unique id is chosen, service code that relies on
other elements with the same id may break.

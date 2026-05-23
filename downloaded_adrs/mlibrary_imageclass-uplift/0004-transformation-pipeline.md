# 4. Transformation Pipeline

Date: 2021-01-28

## Status

Accepted

## Context

The timeline for how long the uplift will be in operation is vague and undetermined.

* DLXS has a concept of collection-specific templates to extend/modify the default transformations

* It is likely that DCC staff will need to continue creating local templates in the future

* Some of the proposed Design System technologies can be verbose; updating component definitions across collections would be tedious

## Decision

We will adopt a **transformation pipeline**.

* DLXS XML will be transformed into **UI XML**, which will write to pre-defined component "blocks"

* The UI XML will then be transformed into **Design System HTML**, which is served to the client

DCC staff will _ideally_ work against the UI XML.

Updates to the Design System transformation can be centrally managed.

## Consequences

* Components will have to be outlined and defined and documented

* DLXS will be extended to support the transformation pipeline


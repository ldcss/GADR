# Converter configuration in backend

## Context and Problem Statement

Each converters may take some configuration. Where do we store this information?

## Decision Drivers

* Usability – The configuration should not be duplicated too much.
* Flexibility – per-project configuration of converters should be possible to cater for the needs of different projects

## Considered Options

* Configuration in connector  – put all converter configuration into the connector config.
* Configuration in backend  – put converter configuration in the backend and query it with the connector.
* Configuration in both backend and connector – put the parts of the connector config relevant to each component in that component.

## Decision Outcome

Chosen option: "Configuration in backend", because configuration options of the backend are much more flexible. It also avoids any duplicate and possibly conflicting configuration.

### Positive Consequences

* Flexible configuration.
* Duplication is avoided.

### Negative Consequences

* Unconfigured converters may not function correctly.
* Hard-coded configuration in the converter may conflict with settings in backend.
* Updates to the backend converter config have to be propagated to the connector.

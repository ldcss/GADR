# 30. Life cycle management

Date: 2020-09-21

## Status

Accepted

Implements [6. Implement Security by Design](0006-implement-security-by-design.md)

## Context

Using 3rd party components, like libraries, modules or executables, introduces the risk of importing security vulnerabilities in those components. Hackers might target these components in a software supply chain attack. A basic precaution to this is to keep all components up-to-date, a practice referred to as life cycle management.

## Decision

We will keep 3rd party components up-to-date to mitigate software supply chain attack risk.

## Consequences

### Advantages

* Fixes for potential security vulnerabilities will be applied soon.
* 3rd party software components will be at a recent version, providing up-to-date functionality.

### Disadvantages

* Updating 3rd party components requires testing, which comes as an additional cost, especially when no other changes are done.
* Updating 3rd party components could introduce bugs due to changes in API or behaviour of the component.

## References

* https://eccitsolutions.com/software-supply-chain-attacks-are-on-the-rise/, retrieved 19 October 2020

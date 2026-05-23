# 2. Standalone NRPE Custom Check module
Date: 2018-12-19

## Status
Accepted

## Context
We need to add new functionality to the project - the ability to create custom NRPE checks. 
This means having templated configuration for adding service-specific plugins for the purposes of monitoring.

The `base` module already contains NRPE specific code.
It installs NRPE and ensures it is running. It also configures a set of default monitoring plugins.

## Decision
We considered three possible approaches to adding the new NRPE functionality:
- Add it to the `base::nrpe`
- Create a separate `nrpe_custom_checks` module and keep `base` the way it is
- Create a separate `nrpe_custom_checks` module and refactor `base` to use it for check creation

Rather than extending the base NRPE class, we chose to create a standalone NRPE custom checks module and keep `base` independent.

## Consequences
This decision has some positive consequences:
- By not adding the new `nrpe_custom_checks` functionality to `base`, we can keep the scope small and tightly focused on being a standalone foundation for CentOS 7 images
- This guarantees faster builds because there are no dependencies and the contents are deliberately kept minimal
- The `nrpe_custom_checks` module can evolve its own design decisions without being constrained by the design restrictions `base` has 

There are some potential negative consequences or arguments against this decision:
- There is merit in providing the ability to create a custom check as a part of `base`
- There is logic duplication for plugin configuration between `base::nrpe` and `nrpe_custom_checks` module
- Testing the `nrpe_custom_checks` module becomes a bit tricky 
  - Some resources in the `nrpe_custom_checks` module are parameterised to use an external NRPE installation and configuration: `base::nrpe` 
  - `base::nrpe` depends on hiera data - we must mock this in our tests
  - If the `base::nrpe` implementation changes it could break the `nrpe_custom_checks` module tests

This decision is based on the current context and can change in the future if there's new information.
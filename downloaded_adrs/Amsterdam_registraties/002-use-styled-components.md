# 2. The application will use Styled Components instead of SASS

Date: 2019-05-01

## Status

Accepted

## Context

SASS is used in most of the [Amsterdam](https://github.com/Amsterdam) projects. The way SASS is compiled by Webpack, however, has all defined style rules affect the global scope. This can lead to unwanted and unexpected side-effect and will increase maintenance, because each developer working on the project needs to be aware of the rules that have been defined and are scattered throughout the code base. Also, using SASS requires a naming convention to prevent specifity problems.

An alternative to global scope CSS is [styled components](https://www.styled-components.com/). This approach is also used by the [Amsterdam reusable component library](https://amsterdam.github.io/amsterdam-styled-components), it makes sense to also apply it to projects (like this one) that make use of components from that library.

## Decision

SASS will not be used in the Registraties project. Instead, styled components will be used.

## Consequences

CSS will be scoped per component, less `!important` rules will be necessary and there is no need to have a strict naming convention.

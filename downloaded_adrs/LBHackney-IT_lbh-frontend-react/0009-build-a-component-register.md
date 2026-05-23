# 9. Build a component register

Date: 2019-11-11

## Status

Accepted

## Context

There will be times when the user has external components that they wish to
connect to components within the component library, so they can use the core
functionality of those external components, while also using the Hackney styles.
An example of this is routing, where they may have custom anchor components
needed to interface with that their routing library. In order to do this, we
will need to create a way for the user to tell `lbh-frontend-react` to use
specific components in certain roles.

## Decision

We will build a component register, where the user can register custom
components to be used by the components in this library.

## Consequences

If the user wishes to use certain components within the library in a way that
interacts with their external components, they will be able to register them. We
will need to indicate this to the user through documentation, so that they know
which components can be registered.

Components provided to the component registry at runtime need to conform to a
certain shape, and accept certain props. We can mitigate this with suitable
documentation.

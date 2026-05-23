# 4/ Use basic-auth to secure published prototypes
**Author(s)**: Steven Adams   
**Status**: Accepted   
**Date**: 29th August 2017

## Context
Given that prototypes built using the NHSUK prototype kit will use the same styling and branding as live NHSUK services, if a member of the public came across the prototype they may confuse it with a live service. It would be beneficial to secure these prototypes behind some level of authentication.

## Decision
We will use the [basic-auth](https://www.npmjs.com/package/basic-auth) package to add a layer of authentication when the prototype application is run on a production environment. This will allow the creator of the prototype to set a username and password to access the prototype when published.

## Consequences
  * There will need to be instructions written and made available to tell consumers of the prototype kit how to set a username and password.
  * There will have to be settings put in place to enforce the use of a username and password when a prototype is published.
  * The consumer of the prototype kit will need to set a username and password.

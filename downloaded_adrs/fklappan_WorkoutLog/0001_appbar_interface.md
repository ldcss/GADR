# 1. Interface for Application Bar

Date: 2019-07-23

## Status

Accepted

## Context

We need a consistent way to access the Application Bar to update the Caption or change the Hamburger menu to homeAsUp

## Decision

We create an interface which will be implemented by the Activity. Due to the single activity architecture, the base
fragment will cast the context to which the fragment is attached to the interface and set a member variable. Also some
methods will be exposed by the fragment so that extended fragments can make use of these methods.

## Consequences

A new interface is necessary and changes to the base fragment has to be made.
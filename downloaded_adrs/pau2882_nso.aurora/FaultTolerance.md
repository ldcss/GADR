# Title
Fault tolerance for Smartfridges

## Status

accepted

## Context

We have a polling mechanism for getting Smartfridges' inventory.  We would have its last known inventory even if it goes down.

## Decision

The decision is to have the polling mechanism to regularly obtain Smartfridges' state/inventory.

## Consequences

Without this, we might not have any of the Smartfridges info if the fridge is offline.  

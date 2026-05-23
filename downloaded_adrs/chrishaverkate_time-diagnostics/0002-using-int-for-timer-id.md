# 2. Using int for Timer ID
Date: 2020-11-15

## Status
Implemented

## Context
Timers need a way of being uniquely identified in order to be processed after several are recorded. The ID should be something easy for the user to work with. 

## Decision
Integers will be used over the alternatives of strings, enumerations, enum classes, or custom object.

## Consequences
What becomes easier or more difficult to do and any risks introduced by the change that will need to be mitigated.

**Advantages**
* Easy to understand for beginners and advanced users
* Light-weight to reduce overhead while using library
* Requires fewer objects / types

**Disadvantages**
* Lacks type safety
* Requires extra work to associate with label or name for reporting

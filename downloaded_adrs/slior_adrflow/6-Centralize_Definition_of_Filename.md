# 6 Centralize Definition of Filename

## Status

Proposed 2017-12-26
  
Accepted 2017-12-26

## Context
With the evolution of the tool, several places in the code need to somehow relate to how the format/template of the ADR file name.  
This immediately means that a change to the template has to take into account these different places.

An example for a feature that suffers from this is customizing the ADR file name template, e.g. in [issue #17](https://github.com/slior/adrflow/issues/17).  

Currently identified places that refer to the file name:
1. The `new` command (`new.js`)
2. The `adr_util.js` file, in several functions.
3. The `adr_util_sync.js` file.

## Decision
We will centralize the definition of the ADR file name template, so it can be easily changed and configured.

Given that we want shared code to be more in `adr_util_sync` we will probably centralize the definition there.

## Consequences
Given that the file name template is centralized, all code places that refer to the file name template will need to reuse the same place.   
Functionality shouldn't be harmed otherwise.


    
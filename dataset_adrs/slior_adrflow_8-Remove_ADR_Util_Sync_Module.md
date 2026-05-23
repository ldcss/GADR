# 8 Remove ADR Util Sync Module

## Status

Proposed 2018-12-09

Accepted 2018-12-10

supersedes [5](5-Utility_Context_Lazily_Initialized.md)

mentions [6](6-Centralize_Definition_of_Filename.md)

## Context

The ADR Util module grew as an attempt to centralize a list of utility functions that require the context of the ADR file and directory.  
The resulting module was very central to the logic of the entire program, but resulted in a module that had too much differing concerns (too many responsibilities/reasons to change).

This has eventually resulted in tangled code, and sometimes to (unintentional) circular dependencies, e.g. as when trying to isolate the handling of links.

At the same time, the usage of the shared context - ADR files and directory - hasn't proved that useful in most case.  
In the cases where it should be used, it can be defined and cached.

## Decision

Divide the utilities defined in this module to other, more focused modules (under `core` directory):
1. `files.js`: handles all file reading and writing
2. `adrobj.js`: handles all ADR logical-level operations. Essentially linking the ID to the file.
3. `links.js`: handles logic around linking ADRs

In cases where caching the ADR files is needed, e.g. in `adrobj.js`, it is done in that module.

## Consequences

In some cases, the API has to change - instead of the API defined at the logical ADR level (the ADR ID), it is defined at the file level, and client modules (namely commands) need to bridge the gap.  
In cases we see that this repeats itself, we can add a wrapping in the `adrobj` module to bridge the gap; e.g. as it is done for the `contentOf` function.


    
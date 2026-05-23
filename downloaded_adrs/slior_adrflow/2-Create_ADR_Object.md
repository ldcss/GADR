# 2 Create ADR Object

## Status

Proposed 2017-07-08  
Accepted 2017-07-12

## Context

Different commands in the ADR utility require manipulating the content of an ADR.  
For example, changing its status.

Instead of spreading the structure and management of ADR *content* into different commands, it would be better to centralize this related piece of knowledge into one file.

Also, we may want to change how manipulate content, or export it. Centralizing it in one place will encapsulate that aspect of the tool into one place.

## Decision

All ADR content manipulation is to be written and centralized in a single ADR object, under the `core` directory.

## Consequences

All commands that need to manipulate the content of an ADR will need to import this file and use its functions.  
All ADR content management will abstracted in this file.


    
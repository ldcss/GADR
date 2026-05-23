# ARD-0002 Solution Layout (Microservices or Monolith)
## Context
*This section describes the forces at play, including technological, political, social, and project local. 
These forces are probably in tension, and should be called out as such. The language in this section is value-neutral. 
It is simply describing facts.*

Should the application be implimented as a monolith or microservices.  While a monolith approach would work for this simple 
application, CAH builds sophisticated, complex applications composed of multiple logical components.

## Decision
*This section describes our response to these forces. It is stated in full sentences, with active voice. 
"We will ..."*
 Given these facts, a multi-repository microservices approach will be used
 
 SCM Repos:
 - UI
 - Microservice #1
 - Microservice #2
 - Microservice #3

## Status
*A decision may be "proposed" if the project stakeholders haven't agreed with it yet, or "accepted" once it is agreed. If a later ADR changes or reverses a decision, it may be marked as "deprecated" or "superseded" with a reference to its replacement.*

- Proposed - 11/2016
- Accepted - 12/2016

## Consequences
*This section describes the resulting context, after applying the decision. All consequences should be listed here, not just the "positive" ones. A particular decision may have positive, negative, and neutral consequences, but all of them affect the team and project in the future.*

Using the multi-repo approach facilitates components being released independently.

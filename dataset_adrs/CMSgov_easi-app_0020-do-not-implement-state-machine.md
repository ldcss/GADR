# Do not implement state machine to handle transitions in Services

**User Story:** [EASi 670](https://jiraent.cms.gov/browse/EASI-670)

As the map of the flow of a system request grows larger and more complicated,
how will we keep endpoints testable, maintainable, and secure. Currently, many
transitions use the same API endpoint. For example, updating a draft system intake,
submitting a system intake, and deciding a system intake all use the `/system_intake
UPDATE` endpoint. However, they have different authorization permissions and side
effects. It is important that the endpoint's Service not become too bloated.

An idea was floated to implement a Finite State Machine, which would capture
information about the transition map in a structured way. However, we determined
that the goals of a refactor (security, maintainability, and readability) could
be accomplished without the overhead necessary of a state machine.

## Considered Alternatives

* Do nothing
* Refactor services into smaller parts without building a state machine
* Implement a state machine

## Decision Outcome

* Chosen Alternative: Refactor services into smaller parts without
building a state machine

## Pros and Cons of the Alternatives <!-- optional -->

### Do nothing

* `+` No work involved
* `-` Services continue to get bigger
* `-` Bugs remain harder to locate and fix

### Refactor services into smaller parts without building a state machine

* `+` Services can be smaller components that are more easily testable
* `+` These services, where they have the same implementation,
can be easily plugged-and-played
* `-` Does not unify all transitions in one location in the code
* `+` Does not force all transitions to be of one format

### Build a state machine

* `+` Implements the transition map in a way that structures
the transitions in a readable way
* `+` Allows for easy modification of the transition map
* `-` Requires significant overhead to set up state machine
* `-` Would section state machine off from other endpoints and
services without compelling reason
* `-` Enforces a rigidity of transitions that may be counterproductive
(since different transitions take different inputs and produce different outputs)

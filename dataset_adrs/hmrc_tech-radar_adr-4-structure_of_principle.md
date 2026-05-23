# ADR 4: Structure of a principle

# Context

We need consistency in terms of format and structure for our patterns across the customer facing, integration and other architectures.
We are also keen to link back to business strategy directly so we can isolate points for consideration in design, implementsation and assessment.

# Decision

We propose the following struture for principle artefacts:

* Context
  * Where possible link to URI's for business strategy identifying bullet points the principle is designed to promote
* Problems
* Rationale
* Examples
* Discussion Points
  * Case by case topics (e.g. If service uses legacy APIs, contact TRAP: add TRAP/Arc Triage email hyperlink)

# Status

Proposed

# Consequences

Stakeholder groups will need to re-factor the format and structure of pattern material in a later editing phase. The first phase is to get the material into the repository.

# Example

* Independently deployable services

* Context
  * (Link to URI for business strategy)
  (see Martin Fowler) [http://martinfowler.com/articles/microservices.html#ComponentizationViaServices]

* Problems
  * Respond to change quickly
  * Availability
  * Scalability

* Rationale
This could otherwise be stated as “loose coupling and high cohesion”. When changes must be made, they should be achieved through independently deployable services. Loose coupling means that a change in one service does not require a change in any other service. High cohesion means that related changes are typically made in a single location.

This allows teams to deliver at their own speed, without being constrained by any of their consumers. Failing to do this correctly would limit our ability to deliver quickly and incrementally.  

* Examples
(TODO: MDTP Link explaining)

* Discussion Points
Not Applicable
TODO: Given scenario X, contact TRAP (email hyperlink).

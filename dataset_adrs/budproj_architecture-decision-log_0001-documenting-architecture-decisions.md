# ADR 0001: Documenting Architecture Decisions

* [Table of contents](#)
  * [Context](#context)
  * [Decision](#decision)
  * [Status](#status)
  * [Consequences](#consequences)
  * [Experience report](#experience-report)
  * [More reading](#more-reading)

## Context

We're a fast-paced company. Being so, we cannot create massive and complex records for every architecture decision we made. But also, if we never record anything, we can lose track of the rationale between each move and risk repeating old mistakes.

## Decision

To solve that, we've decided to create lightweight records in our git repositories regarding architecture decisions, following the [Lightweight Architecture Decision Records](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records) pattern.

In a nutshell, each ADR contains the following sections:
* **Context**
* **Decision**
* **Status**
* **Consequences**
* **Experience report** (optional)
* **More reading** (optional)

You have two options regarding where to store your ADR:
1. **In this repository:** Only company-wide architecture decision records
2. **In your microservice repository:** If your ADR relates to your microservice directly. We suggest storing it at `docs/adr`

## Status

Accepted.

## Consequences

Since this is an unpopular pattern, we must explain this new pattern for any new developer in our team. Our developers may also have a pretty good high concept overview regarding our general architecture to understand if their feature requires a new ADR.

---

## Experience report

In past companies' experiences, we found that ADRs are the optimal way to centralize and organize architecture knowledge in distributed systems.

## More reading

* [Documenting architecture decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)
* [Tech radar](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records)
* [When should I write an ADR?](https://engineering.atspotify.com/2020/04/14/when-should-i-write-an-architecture-decision-record/)

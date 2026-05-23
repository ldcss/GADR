# ADRs

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [What's an ADR?](#whats-an-adr)
- [What's an AD?](#whats-an-ad)
- [Where are the ADRs?](#where-are-the-adrs)
- [How do I create a new ADR?](#how-do-i-create-a-new-adr)
- [How do I remove an ADR?](#how-do-i-remove-an-adr)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## What's an ADR?

An [Architectural Decision Record](https://adr.github.io/) is a document that captures an AD with research and outcomes.

## What's an AD?

An [Architectural Decision](https://en.wikipedia.org/wiki/Architectural_decision) is a design decision that is hard to make and/or costly to change.

## Where are the ADRs?

ADRs are listed in [/docs/adr](/docs/adr).

## How do I create a new ADR?

Copy `docs/adr/.000-template.md` into a new file, and increase the number sequence.

Is this ADR answering a common question? Consider placing a link within DEVELOPING.md.

## How do I remove an ADR?

ADRs should not be removed. Instead they can be rejected, deprecated, or superseded with a new ADR. See the 'Status' field in the template file.

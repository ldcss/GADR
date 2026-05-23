# Adopt Architecture Decision Records

Status: Proposed

## Context

Decisions are very hard to understand in the future without surrounding context.
We need a way of keeping track of the context surrounding a decision.

## Decision

Adopt ADR - Architecture Decision Records as a tool to keep track of decisions
of a certain impact.

Our ADRs should contain the following:

Title: short present tense imperative phrase, less than 50 characters, like a git commit message.

Status: proposed, accepted, rejected, deprecated, superseded, etc.

Context: what is the issue that we're seeing that is motivating this decision or change.

Decision: what is the change that we're actually proposing or doing.

Consequences: what becomes easier or more difficult to do because of this change.

### ADR file name conventions

* The name has the date as YYYY-MM-DD. This is ISO standard and helps for sorting by date.
* The name has a present tense imperative verb phrase. This helps readability and matches our commit message format.
* The name uses sentence capitalization and spaces. This is helpful for readability.
* The extension is markdown. This can be useful for easy formatting.

## Consequences

Each decision will be recorded in the form of an ADR.

# Architectural Design Records

* Deciders: Menno Morsink
* Date: 2018-04-10

## Context and Problem Statement

I need a way to document design decisions.

## Considered Options

* One big markdown file
* Smaller markdown files
* Format MADR
* ADR cmd tool
* In source control or on a wiki

## Decision Outcome

Chosen option: Smaller markdown files in Git of format MADR, no cmd tool, IDEA is sufficient.

Positive Consequences:
* Choices and reasoning are persisted and versioned

Negative consequences: 
* Having to document

## Links

* [MADR](https://adr.github.io/madr/)
* [Format MADR](https://github.com/joelparkerhenderson/architecture_decision_record/blob/master/adr_template_madr.md)


---
layout: page
status: accepted
adr: "0000"
title: Use Markdown Architectural Decision Records
deciders:
date:
---

## Context and problem statement

We want to record architectural decisions made in this project.
Which format and structure should these records follow?

## Considered options

* [MADR][0] 2.1.2 – The Markdown Architectural Decision Records
* [Michael Nygard's template][1] – The first incarnation of the term "ADR"
* [Sustainable Architectural Decisions][2] – The Y-Statements
* Other templates listed at @joelparkerhenderson's [repository][3].
* Formless – No conventions for file format and structure

## Decision outcome

Chosen option: "MADR 2.1.2", because

* Implicit assumptions should be made explicit.
  Design documentation is important to enable people understanding the decisions
  later on. See also [A rational design process: How and why to fake it][4].
* The MADR format is lean and fits our development style.
* The MADR structure is comprehensible and facilitates usage & maintenance.
* The MADR project is vivid.
* Version 2.1.2 is the latest one available when starting to document ADRs.

[0]: https://adr.github.io/madr/
[1]: http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions
[2]: https://www.infoq.com/articles/sustainable-architectural-design-decisions
[3]: https://github.com/joelparkerhenderson/architecture_decision_record
[4]: https://doi.org/10.1109/TSE.1986.6312940

---
layout: default
title: ADR-0000
nav_order: 3
permalink: records/0000/
---
# Use Markdown Architecture Decision Records

* Status: decided
* Decider(s):
  * Infrastructure Team
    * Justin Coyne
    * Mike Giarlo
    * Peter Mangiafico
    * Jeremy Nelson
    * Justin Littman
    * Naomi Dushay
    * John Martin
    * Aaron Collier
* Date(s):
  * Proposed: 2019-04-04
  * Decided: 2020-01-28

## Context and Problem Statement

How do we make architectural decisions as a team? In particularly, how do we do this in a way that is:

* **broad-based**, making clear that a decision was made by a group of people;
* **contextualized**, with the decision living alongside its rationale and alternative options;
* **versionable**, with a log of changes over time;
* **transparent**, with a process that is open;
* **centralized**, not squirreled away in project-specific wiki pages or documents; **and**
* **discoverable**, available on the open web for all to see?

## Decision Drivers <!-- optional -->

This is particularly important because:

* the department no longer has a dedicated architect role;
* we have begun working in earnest on the 2018-2019 SDR evolution initiative; and
* the DLSS Infrastructure team must be accountable for its own architecture decisions.

## Considered Options

* MADR: Use MADR format for recording architecture decisions (with Jekyll as the static site generation framework, GitHub Pages for hosting, and GitHub pull request workflow for discussion and approval)

## Decision Outcome

Chosen option: "MADR", because it was the only option considered, but also because we're already "all in" on Markdown documentation and GitHub. This is well timed given the Decision Drivers above.

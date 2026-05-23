---
layout: default
title: ADR-0004
nav_order: 7
permalink: records/0004/
---
# Remove the Workflow Datastream from Fedora

* Status: Decided
* Decider(s): <!-- required -->
  * Andrew Berger
  * Vivian Wong
  * Infrastructure Team
    * Justin Coyne
    * Mike Giarlo
    * Peter Mangiafico
    * Jeremy Nelson
    * Justin Littman
    * Naomi Dushay
    * John Martin
    * Aaron Collier
* Date(s): <!-- required -->
  * Drafted: 2019-10-31
  * Decided: 2020-01 (mid-January or thereabouts)

## Context and Problem Statement <!-- required -->

To advance SDR evolution towards decoupling from Fedora, we should store workflow state outside of Fedora (in the workflow service's database).

## Considered Options <!-- required -->

* Remove the datastream
* Do nothing

## Decision Outcome <!-- required -->

Remove the datastream.

This was done in dor-services v9.0.0 ([commit](https://github.com/sul-dlss/dor-services/commit/8745e7c2e86edbbaa7577af85779c4ea06258dd3)).

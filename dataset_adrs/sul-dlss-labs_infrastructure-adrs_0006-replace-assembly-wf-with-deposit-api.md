---
layout: default
title: ADR-0006
nav_order: 9
permalink: records/0006/
---
# Create a Deposit API for SDR

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
  * Decided: 2020-02-04

## Context and Problem Statement <!-- required -->

Currently the way to create new objects in the SDR is to:

1. Register an object (typically using Argo)
1. Move files into the `/dor` mount
1. Run the assembly workflow (pre-assembly?)

The Google Books project will grow SDR by millions of new objects. This growth is an opportunity to inject an API into the SDR architecture that serves as the "face" of SDR. Creating an external-facing API allows SDR to accept deposits from on-campus stakeholders such as Big Local News and Open Neuro. Fronting SDR with a new API affords us a mechanism to validate the completeness and correctness of deposited data very early in the accessioning process. Furthermore, we might also use such an API to refactor internal projects (such as ETDs) so these projects no longer require intimate knowledge of the internals of SDR, which reduces coupling.

## Decision Drivers <!-- optional -->

* APIs make it possible to decouple implementations. Our current deposit process is tightly coupled to (Fedora) persistence and we would like to sever this coupling.
* We have potential projects on campus that would like to deposit to SDR in self-service mode.
* Bad data is occasionally deposited, causing problems in the workflow. Fronting SDR with an API that strictly validates deposits would help us detect these problems earlier.

## Considered Options <!-- required -->

1. Use existing process (no API)
1. Create an API

## Decision Outcome <!-- required -->

Option 2: we will create a deposit API as part of work on the 2020 Google Books work cycle.

## Pros and Cons of the Options <!-- optional -->

### 1. Create a deposit API

* Pro
  * Early data validation.
  * Depositors don't need to understand how DOR works.
  * Offer SDR services to more patrons.
* Con
  * We have another service to monitor and keep updated.

### 2. Do nothing

* Pro
  * Less work
* Con
  * Depositors need intimate knowledge of DOR to deposit
  * Less clear path to opening up content flows to campus stakeholders

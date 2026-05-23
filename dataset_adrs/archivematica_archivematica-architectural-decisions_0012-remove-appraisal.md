---
layout: page
adr: "0012"
title: Removal of Appraisal Tab and appraisal related functions
status: proposed
deciders: Sarah Romkey
date: 2026-01-21
---

## Context and problem statement

The Appraisal tab was introduced in
[Archivematica version 1.6 in 2017](https://wiki.archivematica.org/Archivematica_1.6_release_notes).
This was a significant development effort, sponsored by Bentley Historical
Library at University of Michigan, which introduced Angular to the
Archivematica code base and offered users the opportunity to inspect, assess
and arrange transfers in backlog before proceeding with the creation of a
SIP/AIP.  Several additional efforts were made in consultation with other
users/sponsors to expand Appraisal tab functionality, such as the addition
of AtoM levels of description.

The feedback in recent years, from the original users as well as from others, is
that the Appraisal tab has fallen into disuse. The workflows it supports are very
particular and prone to user error. Many Archivematica users have come to favour
more automated, API-driven workflows over those that utilize the user interface
so highly.

The most pressing concern though is that the version of Angular and other tooling
used in the Appraisal tab is out of date and poses security issues in the
Archivematica code stack.

## Decision drivers

* As noted above, the Appraisal tab is posing a security concern meaning it
  must be either removed or overhauled.
* Overhauling the Appraisal tab would be a significant piece of effort that
  does not seem to be aligned with current usage of the Appraisal tab.
* The Appraisal tab does not support more automated, API-driven workflows that are
  now favoured by Archivematica users.
* If the Appraisal tab is removed, it is important to avoid a scenario where users
  have placed transfers in Backlog but have no mechanism for turning them into SIPs.

## Considered options

* Remove both the Appraisal tab (and its related functionality) and the
  Backlog tab, and disable the ability to send transfers to Backlog.
* Remove the Appraisal tab (and its related functionality) while retaining the
  Backlog tab but add an API call and a UI element to take a transfer from the
  Backlog and start it as a SIP.

## Decision outcome

TBD

## Links <!-- optional -->

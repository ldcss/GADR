# 2. Use event sourcing for the back-end

Date: 2017-09-12

## Status

Accepted

## Context

Our back-end needs to store state somehow.

Traditional Object-Relational systems store the current state of the application as the source of truth.
While these are simple to build, they are less conducive to changes in the way data is stored in the long run.

Systems built under our current shareholders have shown to be very prone to change over time, which gives us the need for systems that are conducive to change.

Our experience with our previous system under these shareholders, `Wegwijs`, has shown to be very permissive to change. `Wegwijs` had rather simple data manipulations, with the difficulty of the system lying in the presentation of this data.

 We built `Wegwijs` using event sourcing, which uses a record of all changes as its source of truth. These events can then be used to create different representations of the data using `projections`.

 Due to this, we were able to capture the manipulations easily, while still allowing the stakeholders to change their mind about the presentation of this data.

## Decision

We will use event sourcing the single source of truth for our application.

## Consequences
We will be able to create a system more permissive to change.

We will be able to reuse our knowledge and experience from `Wegwijs`.

We will be able to continue to deliver the benefits of event-sourced systems they already know and expect, eg: rebuilding projections.

Developers will possibly need training on event sourcing, since most developers are only familiar with Object-Relational systems.



# 8. Use Rails

Date: 2018-11-16

## Status

Accepted

## Context

We have already decided to use Ruby for our new applications (see [ADR 0007](0007-use-ruby-for-new-applications-for-manage-offenders-in-custody.md)).

The team are already very familiar with Rails and it is widely used within MOJ.

## Decision

We will use Rails as our web framework for our new applications.

## Consequences

We won't need to make as many decisions about other libraries to use for common
functionality as we would if we chose a more minimal framework.

Rails does more by default than we need everywhere in a microservices context,
so we should try to only include the parts that we need to reduce the risk of
unneeded behaviour introducing vulnerabilities or bugs.

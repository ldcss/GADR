# 2. Implement using Phoenix

Date: 2019-01-04

## Status

Accepted

## Context

It is required to create a demo app to show the component parts for DECODE
working together in order to be able to prove that the system works. An
earlier version of this was implemented in Python using Flask and
Flask-socketio. This largely worked but was prone to weird socket failures,
and I wasn't very happy with maintaining or extending it (which may be
required).

The finished service should be easy to deploy somewhere public (e.g. Heroku).

The system should be amenable to being extended should we need to add any
more functionality (e.g. to support logging into the dashboard).

## Decision

We will reimplement the demo service using Elixir/Phoenix rather than the
Python/Flask/Socketio version previously worked on.

## Consequences

* This will entail rewriting a bunch of code that is largely successfully
  operating which is time we can barely spare.

* This will be the third service implemented using Elixir/Phoenix so we are
  becoming more comfortable and productive in this environment. We will feel
  much more confident in taking this forward with any other features that may
  be required.

* We have experience in deploying Phoenix apps to Heroku, so should be
* straightforward to port that across.

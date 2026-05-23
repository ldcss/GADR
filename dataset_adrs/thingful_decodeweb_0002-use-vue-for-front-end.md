# 2. Use Vue for front end

Date: 2019-03-29

## Status

Accepted

## Context

We need to build a UI that allows users to "login" by entering a PIN - the UI
should allow access to pages if the user logs in. In addition we want to run
Zenroom code in the browser using the Zenroom WASM build. To build this
moderately complex UX we could use vanilla HTML with sprinklings of jQuery or
something more structured.

## Decision

To use Vue (https://vuejs.org) to build the front end UI as a SPA that sends
messages to Phoenix backend via sockets in order to make use of the required
DECODE services.

## Consequences

Building a SPA using a framework like Vue is more complex than banging HTML
together however I think it will give a better final result.

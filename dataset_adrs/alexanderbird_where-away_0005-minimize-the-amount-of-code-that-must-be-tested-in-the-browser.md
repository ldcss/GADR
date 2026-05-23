# 5. Minimize the amount of code that must be tested in the browser

Date: 2020-11-06

## Status

Accepted

Extended By [6. Let the build step generate config for the client code](0006-let-the-build-step-generate-config-for-the-client-code.md)

## Context

There are three main things the package must do:

1. give useful feedback if the input is in an invalid format
2. transform the input into an HTML file (including embedded CSS & JavaScript)
3. that HTML file must show the links and respond correctly to user input.

Items #1 and #2 are very easy to test, item #3 is not. 

## Decision

Minimize the amount of code that must be tested in the browser. Do as much as
possible in the build step and as little as possible in the browser.

## Consequences

I'll need to be creative about how to make the client as simple and foolproof as
possible. The simple solution is to generate some HTML with the input stored as
JSON to be handled at runtime -- but that minimizes the logic in task #2 and
puts it all in #3. That's hard to test & so that's hard to build. Easier to
design, but harder to build.

So instead I'll need to do some thinking & come up with a design that's easier
to build.

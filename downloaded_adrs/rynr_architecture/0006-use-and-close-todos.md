# 6. Use and close TODOs

Date: 2018-07-04

## Status

Accepted

## Context

Using TODO comments in the code are a good way to notify yourself on open topics when dealing with larger parts to deal with. Most IDEs have support for those comments as well so that it's easy to know what still has to be done.  
Unfortunately it's not easy to distinguish between issues that really should be done and others that are an advice.

There are multiple ways to deal with this. You can use further tags like `FIXME` or `XXX` to distinguish between those. You could also decide not to keep any open `TODO` issues in your code and (if valid) move them to your issues.

## Decision

I favor not keeping any open issues in the code.

## Consequences

When submitting code, I will not have any `TODO` comments or at least not merge any `TODO` comments in the code. If they are reasonable, I will bit them to the issue management to be able to decide on their priority.

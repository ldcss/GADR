# 3. Install citerus as a git submodule

Date: 03/06/2018

## Status

Accepted

## Context

I can't be bothered to be installing the citerus library into my
repositories all the time.

I want to keep my copy of that closely synchronized to the common
project, so that any progress that is made can be incorporated
into my work.

I want a convenient way to introduce fixes in the existing implementation
as I discover the need.

I want to keep the touch on the existing code _light_; I expect
to be making some fairly drastic changes in approach, and I don't
want to be debating my choices with the maintainers.

I'm not currently comfortable working with maven projects where
the elements are not rooted under a common location.

## Decision

Add the upstream as a git submodule, so that it's clear precisely
which version of the upstream is in play at any given time.

Changes that are of general interest can be in that space.

Most radical changes (for a _gentle_ definition of radical) should
be maintained elsewhere.

## Consequences

Well, I have to learn how git submodules work.

I'll need to be careful about how to make global changes, for
concerns like formatting, removing unused imports, and so on.


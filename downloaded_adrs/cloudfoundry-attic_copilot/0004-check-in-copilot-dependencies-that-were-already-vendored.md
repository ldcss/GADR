# 4. Check in Copilot Dependencies That Were Already Vendored

Date: 2018-11-07

## Status

Accepted

## Context

Previous packaging of Copilot in istio release relied on the fact that you would
be building copilot on the local machine (bosh pre-packaging).  This meant that
you could reliably fetch all of your dependencies using dep (which was included
as a blob in the release).

When we moved to get rid of pre-packaging and instead do all packaging on a bosh
vm (just known as packaging) we ended up missing one key external dependency for
dep to work (git). Including git as part of release would have meant adding
another blob and packaging step just for git.

## Decision

We removed the .gitignore of the vendor directory and checked-in all of the
source code that dep was placing in that directory at build time.

## Consequences

- No team member should have to fuss with dep when trying to build copilot.
- Team members will need to remember to check in their vendor dir changes when
  upgrading / adding / removing dependencies
- Removal of pre-packaging means that building of copilot got more consistent as
  it cannot vary depending on the user's external machine that is running the
  bosh deploy
- Dep has been removed as a blob for releases going forward since it is no
  longer required to build copilot

We may have to reconsider this approach when go.mod becomes an actual thing but
that isn't until at least go 1.12.

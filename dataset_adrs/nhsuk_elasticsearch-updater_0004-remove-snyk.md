# 12. remove snyk

Date: 2018-03-26

## Status

Accepted

## Context

Many of the vulnerabilities identified by snyk have no fixes, and can only be ignored in the synk config file for a set number of days.
After the number of days are up, the vulnerabilities will fail the build and prevent merge on new PRs, with the only option to ignore the
vulnerabilities again.
Many of the snyk failures are for build tools that are not exposed when applications are deployed.
The overhead of ignoring many snyk vulnerabilities to get builds passing outweighs the potential risks.

## Decision

Snyk will be removed and replaced with a combination of Greenkeeper and Github vulnerability subscriptions.
Greenkeeper will ensure the dependencies are up to date, and the subscription notifications will provide visibility of serious vulnerabilities.
An automated replacement will be put in place in the near future.

## Consequences

Snyk will not be run as part of the git hooks, or on the CI builds.

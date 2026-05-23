# 2. Replace Travis CI with GitHub Actions

Date: 2019-09-23

## Status

Accepted

## Context

GitHub Actions are the new shiny and have been in Beta for sometime. They are
going to be generally available on
[2019-11-13](https://github.blog/2019-08-08-github-actions-now-supports-ci-cd/).
GitHub Actions will have a long term future. It is likely GitHub Actions
will become the default CI mechanism (and possibly more) for projects hosted on
GitHub. Using them in this repo, which has a basic use case will provide some
exposure to the service.

## Decision

The decision is to replace Travis CI with GitHub Actions.

## Consequences

The level of knowledge about GitHub Actions is less than Travis CI due to the
newness of it. This might cause some additional time in understanding
what or how the Actions are working. Mitigation comes in the form of the 
documentation available plus the frequency of change for workflows is typically
low once the workflow has been setup. The low frequency change results in the
documentation needing to be referenced when changes are made regardless of the
system being used.

From experience, the duration to complete the same tasks within GitHub Actions
is shorter than when they are run on Travis. This should result in quicker
feedback.

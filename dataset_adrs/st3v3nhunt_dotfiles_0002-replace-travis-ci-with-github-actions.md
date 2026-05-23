# 2. Replace Travis CI with GitHub Actions

Date: 2019-09-18

## Status

Accepted

## Context

GitHub Actions are the new shiny and have been in Beta for sometime. They are
going to be generally available on
[2019-11-13](https://github.blog/2019-08-08-github-actions-now-supports-ci-cd/).
They are a thing that will have a long term future. It is likely GitHub Actions
will become the default CI mechanism (and possibly more) for projects hosted on
GitHub. Using them in this repository which has a very basic use case will
provide some exposure to the service.

## Decision

The decision is to replace Travis CI with GitHub Actions.

## Consequences

Whilst GitHub Actions are a much newer service than Travis CI the ability for
an organisation such as GitHub to manage the heavy demand one would imagine
will be placed on the service is likely to be first class.
The act of executing shellcheck on the scripts in the repository is not critical.

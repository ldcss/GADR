# 1. Trunk-Based Development

Date: 2019-04-24
Modified: 2019-05-02 (Tyson)
Modified: 2019-05-07 (Tyson)

## Status

Accepted

## Context

To perform Continual Integration and development, with weekly releases, it would be convenient and useful to have a testing branch as well. Accidental pull requests into the main branch may introduce features that have not been tested from the interfac/front-end. It is difficult to automate these front-end interface tests, and there may be factors not present in a localhost/express server that only become apparent in an online scanario.

The use of **master** branch as the release branch is useful, as 'master' is usually the most protected on GitHub, with the most warnings about deleting, modifying, etc. 

Code reviews ar essential from all developers, to become familiar with each other's code, and to learn about javascript, and web-development. THis way we all learn from each other, and also learn good review and communicaton practice.

## Decision

**master** will be the release branch

**development** will be the main development/test branch. This will also be made into the "default" branch for all pull requests, to avoid accidentaly PR into master

**feature** branches must be made off development, with unique names. All pull requests for completed features to be made into "development".

* All PRs must be reviewed by at least two developers to merge into "development"
* All PRs must be reviewed by at the three other developers to merge into "master"
* All PRs must pass all tests (Jest, Travis, and Coveralls) in order to be considered valid for a merge
* Stale reviews will be automatically dismissed if a new commit is pushed to the same branch 
* Accepted PRs for completed features (User Stories) should be deleted after sucessfully merging

## Consequences

This setup complexifies the deployment requirements, and a seperate test website will need to be setup in Azure.
Travis CI -> main site / GitHub CI -> directly to test site

**Update** Coveralls has a problem with repos that use "development" as their main branch: cannot see "master" at all.

**Update** Coveralls has resolved its error with not seeing "master" - logged issue and was fixed

**Update** Change in Admin rights on GitHut means we can no longer deploy directly to testawaywego from GitHub. Instead, Travis will use azure push features with branch rules to both sites (on: master / on: development) but lack of deployment slots means that we must use the same login/password between both test and main sites, with script-specified config for the sitename

**Update** The Travis azure deplyment is very flaky and doesn't complete the deployment predictably. Instead, a script has been written which directly issues a git force push command to send the repo from Travis to azure, if the tests complete sucessfully.



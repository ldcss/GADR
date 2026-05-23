# Use major version branches when publishing and consuming our own GitHub Actions

* Status: accepted
* Deciders: Gary Crye, Josh Gubler, Spencer Tuft, Blake Morgan, Tyler Ray, Jamie Visker
* Date: 2020-11-20

Technical Story: Slack conversation [#1](https://byu-oit.slack.com/archives/C014455NV40/p1590792360006800) and [#2](https://byu-oit.slack.com/archives/CQ2BE663T/p1605907223154800)

## Context and Problem Statement

We want to use [Semantic Versioning (SemVer)](https://semver.org/) when publishing our GitHub Actions, but [we cannot use SemVer ranges](https://github.community/t/semver-ranges-docs-issues/16723/2) when consuming them.

<details>
  <summary><b>More Context</b></summary><br>

When we do
```yaml
uses: byu-oit/github-action-tf-plan-analyzer@v2
```
in GitHub Actions, we're telling GitHub to grab the repo at the _branch_ or _tag_ labelled `v2`.
There's [currently no concept of SemVer](https://github.community/t/semver-ranges-docs-issues/16723/2) in GitHub Actions, but there are some conventions. A common convention is to cut "releases" (tags) using SemVer, e.g. `v2.0.1`, but that doesn't change the `v2` tag or branch by default.

We would like consumers to be able to get `^2.0.0`, but currently that requires moving the `v2` tag or updating the `v2` branch.

GitHub for a while suggested using moving around tags like `v2`, but has [since suggested](https://docs.github.com/en/free-pro-team@latest/actions/creating-actions/about-actions#using-tags-for-release-management) either using branches or tags for that purpose. It is otherwise very unusual to move tags on GitHub, so we prefer branches to convey mutability.

</details>

## Decision Drivers

* Versioning is necessary to communicate changes (especially breaking changes)
* We don't want to break deployments
* Breaking somebody's ability to deploy doesn't actually bring down production
* We want to make it easy to roll out updates
    * Many consumers of our GitHub Actions are unfamiliar with how they work

## Decision Outcome

When publishing actions, use branches corresponding to major versions (e.g. `v1`, `v2`) and keep them updated. Treat updates to the major-version branches as production changes. Continue to tag new releases according to SemVer (e.g. `v2.0.1`, `v2.1.0`).

When consuming [our actions](https://github.com/search?q=org%3Abyu-oit+github-action+archived%3Afalse&type=Repositories), refer to the major version branches (e.g. `v2`). This will allow us to roll out most changes to the organization quickly and effectively.

## Links

* [Initial Slack conversation](https://byu-oit.slack.com/archives/C014455NV40/p1590792360006800)
* [Slack conversation when this ADR was made](https://byu-oit.slack.com/archives/CQ2BE663T/p1605907223154800)
* [GitHub's recommendations (which have evolved)](https://docs.github.com/en/free-pro-team@latest/actions/creating-actions/about-actions#using-tags-for-release-management)

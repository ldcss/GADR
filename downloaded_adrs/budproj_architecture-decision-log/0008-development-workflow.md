# ADR 0008: Development Workflow

* [Table of contents](#)
  * [Context](#context)
  * [Decision](#decision)
  * [Status](#status)
  * [Consequences](#consequences)
  * [More reading](#more-reading)

## Context

While developing a new feature or solving a bug, each developer has a style. Some developers push code to the `main` branch (never do that) while others create their feature branches.

Although not mandatory, having a pattern makes it easier for developers to communicate and can make our process seems intuitive.

## Decision

We are going to use three main patterns for our development process:

* [Forking](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/fork-a-repo)
* [Gitflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)
* [Commit](https://www.conventionalcommits.org/en/v1.0.0/)

The first one relates to **how we host our development code**. Based on this ADR, you should not create branches in the `origin` remote. Instead, create your fork and make your branches there. This decision avoids many unwanted side effects and accidents.

You can create branches at `origin` if those branches are long-lived and relate to a newer version or a massive work from multiple developers. There are some default branches all our repositories might have:
* `main` (default branch)
* `develop` (next stable release branch)
* `test` (working environment for testing purposes)

The second one relates to naming and Git workflow. Our branches naming should follow Gitflow standards, like: `feature/<sub-path>/<name>`, and others.

Also, the `develop` branch must remain stable, receiving only new finished features in it.

The third one relates to linting our commits. We should learn how to write useful commit messages, using that convention, to improve our developer experience.

## Status

Accepted.

## Consequences

This pattern can remove unwanted accidents and side-effects, but we can find hard for some developers to start using those conventions.

---

## More reading

* [Github fork](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/fork-a-repo)
* [Gitflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)
* [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)

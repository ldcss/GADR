# Automated Dependency Release Management

## Status

Proposed

## Context

Whilst tools like [Dependabot](https://github.blog/2020-06-01-keep-all-your-packages-up-to-date-with-dependabot/) simplify the process of testing updates to a repository's package dependencies, there can still be signficant coordination work to apply such changes and have the resulting updates cascade through the rest of your software estate.

Before committing a dependency update there are several considerations:
* What type of [semantic version](https://semver.org) increment is this change?
* How confident are we in the repository's tests for catching breaking changes in dependencies?
* How reliable is the publisher's SemVer attribution?
* Should this dependency update trigger a new release?  If so, how should such updates be batched?
* To what extent could this update trigger a cascading update across other repositories?

This ADR describes an automated process that can reduce the burden associated with such updates and their cascading effects, whilst still providing control mechanisms to prevent unrestricted updates.

**NOTE**: *The process, as described, assumes the use GitHub Dependabot (as opposed to the dependabot.io service that has slightly different functionality)*

## Decision

The process for approving, merging and releasing these types of updates can be automated so long as suitable control measures are in-place to manage the different package promotion requirements.

### Concepts

A number of terms are used to describe the process, they are defined as follows:

* `semver-increment`: The scale of a given update as indicated by the change in the semantic version (i.e. patch, minor, major)
* `auto-approve`: The process of a CI/CD bot approving a pull request
* `auto-merge`: The process of a pull request being merged by a bot, once in a mergeable state (e.g. passing checks, approved etc.)
* `auto-merge-candidate`: A pull request that is approved for `auto-merge`
* `auto-release`: The process of triggering the release pipeline of the consuming project (e.g. creating a git tag)
* `auto-release-candidate`: A pull request that is approved for `auto-release`
* `no-release`: An override mechanism for suppressing the `auto-release` behaviour
* `release-pending`: The state a pull request is in when it is approved for `auto-release`

### Principles

These set out the core requirements for the process we wish to automate.

1. Dependabot updates can utilise `auto-approve` and `auto-merge` based on an allow list of package names
1. Dependabot updates otherwise approved for `auto-merge` can be opted-out based on their `semver-increment` - by default, 'major' changes should be ignored by this process
1. Dependabot updates approved for `auto-merge` can additionally utilise `auto-release`, based on an allow list of package names
1. Regular pull requests must never utilise `auto-approve`
1. Regular pull requests will, by default, utilise `auto-release`
1. Regular pull requests may opt-out of `auto-release`
1. All `auto-release-candidate` pull requests must be batched together, to avoid unnecesary release churn

A process that implements these mechanisms is illustrated in the following flowchart diagram:

![pr-autoflow: High-Level Process Flow][flowchart]

### Implementation

The current implementation consists of the following components:

* a PowerShell module [`Endjin.PRAutoflow`](/module) - implements the pull request title parsing and version comparison logic
* 2 x GitHub Actions (docker-based)
    * [`dependabot-pr-parser`](/actions/dependabot-pr-parser) - given a PR title, it identifies Dependabot pull requests that meet the specified naming & `semver-increment` criteria and extracts the required metadata
    * [`dependabot-pr-watcher`](/actions/dependabot-pr-parser) - given a list of PR titles, it returns those that meet the specified naming criteria
* 3 x GitHub Actions workflows:
    * [`dependabot_approve_and_label`](https://github.com/endjin/.github/workflow-templates/dependabot_approve_and_label.yml)
    * [`auto_merge`](https://github.com/endjin/.github/workflow-templates/auto_merge.yml)
    * [`auto_release`](https://github.com/endjin/.github/workflow-templates/auto_release.yml)

These are used to identify `auto-merge-candidate` and `auto-release-candidate` pull requests and perform the required processing on them.

The Pull Request title parsing expects the following convention:

```
Bump <PackageName> from <FromVersion> to <ToVersion> in <SolutionName>
```

### Limitations

The current implementation is tailored to the NuGet eco-system which results in the following limitations:

* The pull request title parsing is unlikely to work for Dependabot pull requests created for other eco-systems
* The [`auto_release`](https://github.com/endjin/.github/workflow-templates/auto_release.yml) workflow utilises [GitVersion](https://gitversion.net/docs/) (a cross-platform .Net tool) to generate the version number used to create the release tag, which implies certain expectations in terms of git usage

## Consequences

* Overhead of maintaining external dependencies is reduced, provided adequate automated test coverage is available to validate such changes
* Control over which dependencies benefit from this automation whilst ensuring that, for example, major changes to such dependencies still require manual approval
* Streamlines a continuous delivery process for the typical pull request workflow
* By combining `auto-merge` with `auto-release`, dependency updates can automatically propogate through a hierarchy of related repositories with manual intervention only by exception
* The use of [NuGet meta-packages](https://endjin.com/blog/2020/09/streamline-dependency-management-with-nuget-meta-packages) can further streamline the full-hierarchy propogation process

## Future Considerations

* Add instrumentation to this process to faciliate centralised tracking of metrics related to the propogation of updates across repositories

[flowchart]: /docs/images/flowchart.jpg "pr-autoflow: High-Level Process Flow"
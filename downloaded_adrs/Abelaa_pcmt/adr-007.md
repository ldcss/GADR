# 7. Versioning and Release Mechanism

## Status

Accepted, 2019-10-15

## Context

PCMT wants to accomplish a number of goals through the use of versions:

1. Convey to stakeholders the initial suitability of the project:
    * Pre-v1: In development for global stakeholders.
    * Version 1: Production ready for global stakeholders.
    * Version 2: Production ready for national stakeholders.
1. Leverage semantic versioning to convey to dependents the nature of the
  release.  e.g. is it a patch-release, major new functionality, etc.
1. Mark a specific state of the code-base, tied to a released asset.
1. Indicate which version of Akeneo that PCMT is derived from.

## Decision

1. We will version PCMT by [Semantic Versioning 2.0][semver].  However since  
    Docker tags do not support the use of the `+` symbol, we'll use `-` in  
    its place.
1. We will have a build number (from the commit SHA), which is from a CI  
   pipeline, that includes a distinct set of commits.
1. We will expire and remove old Build numbers, so they need to be pruned 
   regularly.
1. We will not publish assets if a pipeline fails, and conversely if a pipeline
   is re-run, it consists of the same commits (state of the code), and therefore
   it should have the same build number.
1. We will promote build numbers to a showcase or UAT server, manually.
1. We will promote build numbers to a release, manually.  
1. We will keep the semantic version of the system separate from the build
   number, in a file in the SCM.  When an asset is labeled from
   the CI pipeline, it'll use the full form by placing the build number in
   the build meta-data of the Semantic Version.  e.g. `1.0.0+48af4a30`
1. When promoting to a release we will co-label the published assets such that
   one asset will have the build number, and the released asset will not include
   that number. e.g. version 1.0.0 might be `image:v1.0.0+SHA` and
   `image:v1.0.0`, which are equivalent assets.

## Consequences

1. Semantic versions must be set carefully and intentionally.  They should only
   be set by those intending to designate a release.
1. Builds, pre-releases, and stable releases are all controlled through the
   setting of the semantic version in the SCM, and the commits that the CI
   server builds.


[semver]: https://semver.org/spec/v2.0.0.html
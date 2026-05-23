# 7. Continuously deliver with Github Actions

Date: 2019-12-10

## Status

Proposed

## [Context](https://docs.google.com/document/d/1zRy8OCZ_JJpbs6scwrvx5PYkWwaWbR-5DLuq3AujhBA/edit)

Libero products need automated builds for pull requests and release candidates.

Travis CI has been [acquired](https://techcrunch.com/2019/01/23/idera-acquires-travis-ci/) by a private equity firm and has an [uncertain future](https://twitter.com/ReinH/status/1098663375985229825). We also have run into performance bottlenecks of [5 concurrent jobs](https://travis-ci.com/plans) in the open source offer.

Github Actions is a Github-native general workflow system that can provide CI/CD capabilities; it has been in general availability [since November](https://github.blog/2019-08-08-github-actions-now-supports-ci-cd/). It offers fully managed, sandboxed environments and a per-repository limit to concurrency.

## Decision

We will create Github Actions builds for all new projects.

We will port existing Travis CI builds of maintained projects onto Github Actions, on an as-needed basis.

## Consequences

Projects have to look out for possible bugs in Github Actions, as a bleeding edge platform.

We are addressing the risk of Travis CI undergoing outages or reduced support.

Teams and projects should have no impact on each other in terms of build performance.

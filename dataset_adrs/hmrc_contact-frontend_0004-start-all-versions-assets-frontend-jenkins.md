# Start all versions of assets-frontend via Service Manager in Build Jenkins

* Status: accepted
* Date: 2021-11-10

Technical Story: PLATUI-1393

## Context and Problem Statement

As part of PLATUI-1393, browser based acceptance tests were added that rely on `assets-frontend`. These acceptance tests
run as part of the build in Jenkins, which means `ASSETS_FRONTEND` needs to be added as a parameter to the `build-jobs` 
job builder `.withServiceManager` call. However, `assets-frontend` has specific logic that means all versions are started 
via Service Manager, that is multiple instances of `assets-frontend` will start, not just the latest release. 

There is logic in Service Manager to pass an `application.conf` file to start only required versions of `assets-frontend`,
however as we are not using Service Manager to start `contact-frontend` itself, this logic does not get called. Therefore,
all verisons of `assets-frontend` start during when running a build, either after merge or as part of the PR builder for 
`contact-frontend`.

## Decision Drivers

* `assets-frontend` is a deprecated service - we want to ensure the functionality using it does not break, but we are
  reluctant to invest large amounts of time in it
* Service Manager is a Python application used heavily across the Platform and not owned by PlatUI, and we would like to 
  avoid making changes to it if possible to support our workflow.
* Similarly the job builders in the `build-jobs` repo are heavily shared, and we would like to avoid making changes to 
  `build-jobs` if possible 

## Considered Options

* Keep experimenting with existing `build-jobs` code to see if there is a way to pass in a specific release of 
  `assets-frontend`
* Rewrite `build-jobs` to accept a release passed in
* Add `assets-frontend` as a dependency for the `HMRCDESKPRO` Service Manager profile, so as to hook into the logic
  for specific verions
* Rewrite Service Manager to additionally accept other ways of picking up a version of `assets-frontend`
* Accept that builds of `contact-frontend` will be slower due to starting all versions of `assets-frontend` (a quick look
  suggestions in the region of an additioanl 90-120 seconds per build)

## Decision Outcome

Chosen option: "Accept that builds of `contact-frontend` will be slower due to starting all versions of 
`assets-frontend`", because:
* It is a quick solution that does not involve further investigation to support a test case that we hope to deprecate
* The performance impact will slow down development in terms of PR building but will not affect local development
* This decision can be easily revisited if performance becomes a problem, i.e. by making no changes there will be no 
  rolling back needed if we remove the test or decide to change other services

### Positive Consequences

* Allows us to add browser-based acceptance tests for forms with `contact-frontend` relying on `assets-frontend`
* Does not involve further development time
* Proven to work in the build environment

### Negative Consequences

* Will definitely cause a negative impact on the time taken to build a release, or run a PR builder

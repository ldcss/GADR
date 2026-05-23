# 9. Test features with Cucumber

Date: 2018-12-29

## Status

Accepted

## Context

Acceptance tests aim to test the application behaviors as a whole from a consumer point of view.

Those tests must be understandable by any user, either technical or not and help documenting the provided features.

Defining new acceptance tests must be easy, through reusable step definitions.

Application sources must be self-contained, including the acceptance tests definition and implementation, so that
acceptance tests can be run during the development lifecycle in a [Behavior-driven development](https://en.wikipedia.org/wiki/Behavior-driven_development)
approach.

## Decision

[Cucumber](https://cucumber.io/) will be used to describe and execute acceptance tests in `menu-generation` application.

## Consequences

Gherkin language will be used as the acceptance tests definition language.

Cucumber java library will be used to run the tests.

Acceptance tests sources will be isolated in a dedicated gradle `sourceSet`, so that dependencies for running those tests
won't mix with dependencies used for unit tests. It will also ensure that acceptance tests don't use any underlying main
sources.

Tags will help categorize tests (e.g. smoke, edge, security) to allow running a slice of acceptance tests during
development or Continuous Integration phases.

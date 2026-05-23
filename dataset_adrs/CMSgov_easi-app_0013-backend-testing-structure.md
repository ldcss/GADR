# Use Separate Integration Package for Go Integration Tests

**User Story:**

As we write the server side of the EASi application,
we need to decide how to structure our testing suites.
With complex,
computationally expensive to access resources,
like DB calls,
or network access to APIs,
it can become both cumbersome and slow
to set up and run tests that include them.
On the flip side,
mocking these resources can cause poor test coverage
that does not mimic production use cases.
It's important to create a testing strategy
that balances coverage and runtime.

This ADR focuses on setting up a strategy
that balances resource driven integration tests
with wide coverage unit tests in our Go codebase.
It's important to understand the application layer patterns
described in the [Truss Engineering Playbook](https://github.com/trussworks/Engineering-Playbook/blob/master/web/server/go.md#application-layers),
as it is a driver for this decision.

For the purpose of this ADR,
we'll focus on breaking out "unit" and "integration" tests,
but won't try to define their contents in detail.
Integration tests will likely happen at the endpoint/handler level
and run as if it were a production case.
Unit tests will happen across the codebase,
mock outside packages,
and focus on individual function use cases.

## Considered Alternatives

* **Don't distinguish between unit and integration tests
  and run them together together**

Effectively, do nothing.
Integration tests and unit tests will reside in the same testing suites.

* **Run based integration tests in same suite as unit tests and flag
  with `testing.Short`**

In this case,
we can distinguish between integration tests by using `if !testing.Short`
and running unit tests only with `--short` from the command line.
This provides a way to separate the execution of different tests,
however their package dependencies will still be linked.

* **Move integration tests to separate package**

Integration tests would live in an `integration` package,
and those tests could be developed and run separately.
We can still utilize `--short` to break apart execution.
This would allow us to also break apart package dependencies.
Unit tests would minimize imports and use mocks,
avoiding a wide package surface,
while integration tests would pull in production dependencies,
and mirror the server setup.

## Decision Outcome

* Chosen Alternative: **Move integration tests to separate package**

Moving all dependency wiring to a separate package
allows unit tests to stay decoupled from dependencies.
This may be an `integration` package,
or an existing package based on production package structure
(ex. `routes` or `server`).
For examples, a handler, service, or model
is only required to pull in packages
that mimics an interface dependency based production structure
that a layered package approach pushes to achieve.
Integration tests then become more synonymous
with wiring up our server with dependencies.

## Pros and Cons of the Alternatives

### Don't distinguish between unit and integration tests and run them together together

* `+` Early develop is easy ("do nothing").
* `-` Lends towards bad unit testing habits, including:
      testing dependencies not integral to test target,
      writing less unit tests because they are slow,
      focusing less on API surface and single responsibility principle.
* `-` Testing suite can quickly become slow.
* `-` Not clear what coverage of a function is
      (integration and unit tests both count as coverage statistically).
* `-` Unclear where to mock and where to import.

### Run integration in same suite as handlers and flag with `testing.Short`

* `+` Long tests can be disabled during developer workflow.
* `+` Integration tests live close to their unit counterparts,
      increasing developer awareness of tests run on a function/package.
* `-` Suite setup/teardown happen on the suite level,
      but short flagging would be required within individual tests and suite setup.
      In other words, short logic would be sparse across tests.
* `-` Not clear what coverage of a function is
      (integration and unit tests both count as coverage statistically).
* `-` Unclear where to mock and where to import.

### Move integration tests to separate package

* `+` Integration tests with dependencies are clearly marked
      and easily tested as separate from unit tests.
      Dependencies are no longer imported for unit tests.
* `+` Short flagging happens on suite/package level.
      Tests can also be run per directory.
* `+` Dependency structure mirrors production.
* `+` Easier to write unit tests with wider test surface.
* `+` Can optimize performance of testing suite by type
      and can benchmark easily which testing suite is slow.
* `-` Requires developer awareness.
      This might be moot,
      as our current instructions for testing with services ignore integration tests.

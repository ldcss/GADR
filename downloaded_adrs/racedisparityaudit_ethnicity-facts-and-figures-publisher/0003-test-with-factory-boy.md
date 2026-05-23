# 3. Test with Factory Boy

Date: 23/01/2019

## Status

Accepted

## Context

When testing our code, we often need to have certain data in our database, whether it be a measure version so that we can view a measure page, or a user with a specific role so that we can test the site logged in as that role. A lot of our database models are related and therefore depend on related models to also exist and be in a specific state. Getting the correct data into our database can be fiddly and error-prone.

## Decision

Use Factory Boy to generate model instances for tests.

Pros
----
* More explicit about the data/conditions under test.
* Fewer fixtures to maintain.
* Easier/faster to write new tests that require a specific database state.

Cons
----
* Effort to understand how FactoryBoy works and how we've implemented it in our codebase.
* Potentially slower tests if we are careless with how we use the factories, as some factories generate a lot of additional instances which may not be required for the tests.

## Alternatives

1) Extend our existing suite of test fixtures with additional varieties. In order to meet all of our needs, we would probably have to write a lot of additional fixtures with similar names, increasing duplication and making it harder to understand what is available. It's possible that the same fixture could be created multiple times with different names. We would also still be making assertions about data that is described in fixtures rather than explicitly configured in the test.
2) Instantiate all required data within the test. This would lead to a huge amount of repetitive code, as well as lots of boilerplate code at the start of each test which would increase maintenance costs and decrease readability.

## Consequences

* Developers need to remember to update factories whenever they make a change to the model.

# 001 Naming Schema for Unit Tests

Date: 2018-10-29

## Status

Accepted

## Context

When deciding on a naming scheme for unit test methods, the following criteria were most important to us:

* **Readability** - The test method names should read like English sentences, with clear word boundaries
* **Flexibility** - We should be able to follow different patterns, like "Given ... When .. Then", but also like "Does X". 

## Decision

We use `snake_case` for method names in unit tests. We adapt the coding style settings to ignore the deviation from our usual `camelCase` convention. 

If it makes sense, we use sentences containing the words `given`, `when` and `then`. To give each section a clear boundary, when we use `given` or `when`, then we also use `then`.

Good:

	test_given_first_time_visitor_then_return_main_banner

Bad:

	test_given_first_time_visitor_return_main_banner
 

We keep in mind that the sentences always refer to the system-under-test (SUT) and don't unnecessarily repeat its class name.

## Consequences

We are able to [run phpunit with the `--testdox` option](https://phpunit.readthedocs.io/en/7.3/textui.html#testdox) and get meaningful output.


[Home](../../README.md)


# 5. Test Framework

Date: 2020-09-21

## Status

Accepted

## Context

We want our code to be well tested. What tools or frameworks can we
leverage?

## Decision

We will use the [pytest] framework to test our [Python] code. In
addition, we will use the [mock] library to prevent our tests
from interacting with external services.

## Consequences

**Pros:**

* Great support for modular setup/teardown processes
* Community standard (outside the standard library)
* Good documentation
* Easy to write/read

<br/>

[Previous](004-serverless-framework.md) | [Next](006-access-control.md)


[Python]: https://www.python.org/downloads/release/python-380/
[pytest]: https://docs.pytest.org/en/stable/contents.html
[mock]: https://docs.python.org/3/library/unittest.mock.html

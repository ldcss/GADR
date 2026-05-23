[Home](../../README.md)


# 6. Access Control

Date: 2020-09-21

## Status

Accepted

## Context

We need a way to protect our app. Only a small number of people
should be able to access the application. This includes the
developers and the intended end users (i.e. you).

## Decision

To protect our application, we will require all requests to include
an `Authorization` header containing a JWT. Any request that is missing
this header will be rejected. Futhermore, the JWT will include an
expiry so we can control the time period in which users can access
the application.

The authentication process will be implemented as an additional AWS
Lambda function. In [Chalice], this is referred to as a Custom Authorizer

## Consequences

**Pros:**

* Can limit access to specific users
* Can limit user access to specific time period
* Easy implementation using [Chalice Authorizers]
* Provides the ability to inject additional context into requests

**Cons:**

* Requires an additional AWS Lambda
* Cached responses may cause issues for expired/revoked access
* May require addition services (secrets, user details, etc.)


<br/>

[Previous](005-test-framework.md) | [Next](007-secrets.md)


[Chalice]: https://aws.github.io/chalice/
[Chalice Authorizers]: https://aws.github.io/chalice/api.html#authorization

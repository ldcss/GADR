# 16. Logging and tracing

Date: 2020-02-25

## Status

Accepted

## Context

We want to have an application wide logging infrastructure in place so that we can trace user requests through the 
application. It should be possible to trace each request through the application layers so that we can see what outgoing
calls were made for incoming requests.

## Decision

The use of `monolog/monolog` to provide configurable logging levels throughout the application. Unique tracing 
information is already provided by the amazon loadbalancers so this should be made available to the logging library and
attached to the logged information.

* Logging of service code to be main source of log information. If needed handlers can also be logged.
* Most logging to be done at an _info_ level.
  * User actions that need monitoring (e.g. authentication failures) at _notice_ level
  * Personally Identifiable Information (PII) to **not** be logged anywhere but _debug_

## Consequences

* Amazon trace Id information to be available throughout the application
* Logging services to be injected to service constructors to allow logging out of services.
* Where necessary logging services to be injected to Handlers. 
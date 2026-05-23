# Replace Inappropriate Usages of CTPException with Appropriate Runtime Exceptions

## Context

A Java checked exception called `CTPException` has become ubiquitous throughout our entire SDC codebase, occurring in **1,017** places, many of which are the mandatory declaration of `throws CTPException` as a consequence of using a _checked_ exception, when in most cases, a _runtime_ exception was what we wanted, because the error was unexpected and unrecoverable.

Java usefully provides IllegalArgumentException and IllegalStateException - for example - which cater for almost almost all of our needs to raise an exception, when an unexpected and unrecoverable error in our system occurs.

For the REST APIs, an HTTP status code should be specifically chosen in the logic which is closest to the definition of the API endpoint itself, to tell the API client whether it made a bad request, resource not found, or indeed an internal server error occurred (in the event that our system has an unrecoverable error, due to missing/corrupt data, mangled state and a whole host of other problems which are _internal_ and could only be investigated and fixed by ops).

`CTPException` was introduced as a convenience class to return different HTTP status codes in the REST APIs, but it has been completely mis-used and spread around the codebase.

## Decision

We will remove the CTPException class wherever it exists and replace it with a runtime exception, in most cases, with the exception of these specific REST API errors:

  - REST API is sent garbage: bad request (400)
  - REST API can't find requested resource: resource not found (404)
  - REST API can't perform 'action' because of business rules (e.g. invalid state transition): forbidden (403)

We will use **runtime** exceptions in the event of the following REST API errors:
  
  - REST API didn't find data it expected (and needed) to find, nulls, missing configuration and all the very many other kinds of system state corruption which are possible: internal server error (500)
  - REST API can't connect to database, Rabbit, Redis, or to another API it needs: service unavailable (503)
  
A very great deal of the code deals with Rabbit queue messages and cron/scheduled/poller jobs, which of course cannot report a HTTP status code, because there is no interactive 'user' - it's asynchronous. The use of checked exceptions in this code is inappropriate, because the errors are fatal and unrecoverable: we rely totally on our logging and alerting to instigate an investigation and fix the issue. These exceptions are _runtime_ exceptions. The vast majority of exceptions raised in the SDC system should be runtime exceptions.

## Consequences

It will require significant effort to replace `CTPException` in the 1,017 places where it's used. Many unit tests will need to be refactored.

The REST APIs will need some changes to the shared 'framework' to ensure that the appropriate HTTP status codes are still returned to API clients. Although, because our APIs are only used internally, a precise status code is not particularly useful. Instead, use of tools like Zipkin - with a correlation ID - allow us to be able to investigate a failure to its root cause, far more effectively than a HTTP status code.

All the other places where `CTPException` has been used are inappropriate. The appropriate exception to raise in each case will need to be considered individually, which will be time-consuming, but we need to improve our error handling when processing queue messages and when processing a scheduled/timed/cron job batch, which has confused asynchronous and synchronous paradigms. By doing this work, we avoid the situation where we end up in an unrecoverable/corrupted state, requiring manual intervention by operational support.

There will be an ongoing overhead for teaching any new developers who join the project the appropriate way to raise exceptions in Java/Spring applications.

Ultimately, improving our error handing - particularly around exceptions - should result in a system which is capable of recovering from temporary outages of parts of the microservices architecture, which also comprises PostgreSQL, RabbitMQ, SFTP and 3rd party services, which might not always be available.
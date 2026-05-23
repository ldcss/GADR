# 2. Use controller to manage all input from users

Date: 2020-05-17

## Status

Accepted

## Context

The issue motivating this decision, and any context that influences or constrains the decision.
While the initial idea was to have input be in the form of a file creation in a trigger bucket, in order to appropriately deliver results and progress reports for users, we will need a smarter solution.

We would also like to theoretically be able to provide a generic interface so that our tool could be used programmatically or via a UI as is desired by the end user.

## Decision

We will create a JSON API controller for all end user interactions with the platform. This would handle the managment of the jobs concept (however it is to be implemented) and provide users a consistent way to create, view the status of, and retrieve results for their data processing jobs

## Consequences

An additional service will need to be created to handle this. Still TBD is how much data/input validation is appropriate for this controller.


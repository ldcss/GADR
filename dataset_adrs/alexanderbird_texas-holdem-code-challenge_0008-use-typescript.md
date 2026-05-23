# 8. Use TypeScript

Date: 2019-05-30

## Status

Accepted

Guided by [3. Use familiar tools](0003-use-familiar-tools.md)

Detailed in [9. Use TypeScript 3.4.5](0009-use-typescript-3-4-5.md)

## Context

The approach I have chosen (see docs/model.md and docs/algorithm.md) leads to
many small unit-testable components and a main function that ties them together.

The options I can see for the main function are:

 1. Write it with unit tests, heavily mocking the dependencies
 2. Use a type system to check that the plumbing matches up, don't unit test the
    main function
 3. Don't test the main function, don't use types. My guess is I'll make some
    mistake along the way and have to debug it.

In all cases I'll run integration tests, but without (1) or (2) I won't know
where bugs are when the integration test fails.

My guess is that (2) will be more efficient than (1), and either of them will be
more efficient than (3).

For JavaScript static typing, I'm familiar with TypeScript.

## Decision

Use TypeScript.

## Consequences

- I have to take a few minutes to add TypeScript to the project
- I'll avoid debugging time in exchange for writing a type system

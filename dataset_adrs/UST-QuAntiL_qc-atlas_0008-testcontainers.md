# Use Testcontainers

* Status: accepted
* Deciders: [Q-tal Enpro Team]
* Date: [2020-09-04] <!-- optional -->

## Context and Problem Statement

Running Service Tests requires PostgreSQL. To ensure an instance is always up and running a container has to be manually launched or started automaticially.

## Considered Options

* Launch the container or DB before executing tests manually
* [Testcontainers](https://www.testcontainers.org/)

## Decision Outcome

Chosen option: [Testcontainers](https://www.testcontainers.org/), because it simplifies the test execution process


### Positive Consequences <!-- optional -->

* It is not mandatory to ensure postgres is running before starting the tests

## Pros and Cons of the Alternatives 

### Manual Launch

- `+` Does not require docker, How Postgres is running is irelevant, as long as its availabe on a specific port
- `+` low performace overhead, since the same instance is reused along all tests
- `+` Does not depend on third party librarires
- `-` Requires extra procedures before running the tests
- `-` Can be considered hard to use


### Testcontainers

- `+` Easy to use
- `+` Completely independent from running postgres instances (Uses random port and credentials)
- `+` No extra procedures needed, apart from launching the test
- `-` Depends on docker
- `-` Slower due to container launch overhead


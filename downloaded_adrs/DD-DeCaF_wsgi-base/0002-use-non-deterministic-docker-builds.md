# 2. Use non-deterministic Docker builds

Date: 2018-08-20

## Status

Accepted

## Context

In principle, we agree that deterministic bulids are a great idea. In practice,
first creating a lock file (using pipenv or pip-tools) via a Docker based
workflow would require us to use a separate image and thus seems inefficient.

## Decision

We build our Docker images directly from the requirements and let the resulting
container be the deterministic unit of distributing our code. We feel that the
improved build workflow outweighs the negative consequences.

## Consequences

There is a slight risk that differences are introduced between a local build and
later CI/CD builds. However, sooner or later those differences would come up
anyway. Secondly, we do not have pre-generated hashes of our dependencies.
Should someone compromise our CI environment and insert their own malicious PyPI
server, we would not detect changed packages.

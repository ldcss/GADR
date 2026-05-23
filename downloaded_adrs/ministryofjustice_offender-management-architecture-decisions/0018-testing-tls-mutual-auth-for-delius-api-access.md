# 18. Testing TLS mutual auth for Delius API access

Date: 2019-01-28

## Status

Proposed

## Context

As documented in [ADR 0014](0014-access-the-delius-api-via-ndh.md) we are
going to access the Delius API via the NOMIS data hub using TLS mutual auth,
managed on our side by a sidecar container.

We need to find a way of testing our auth setup - in particular that it only
allows access to the Delius API from our allocation manager. The NDH only
exists in production, so we need to decide how to test this setup and
deployment of the sidecar in our other environments (at the moment we only
have staging and production). We want staging to be as similar as possible to
production so that we're testing changes in a realistic environment before
pushing them to production.

## Decision

We will set up a separate namespace on the cloud platform for a Delius staging
environment.

We will deploy the NDH-side mutual auth container into that environment, along
with the Delius API with a dataset constructed to match T3 NOMIS data.
Initially our main concern is testing the mutual auth setup so instead of the
Delius API we could deploy a simple HTTP server if that's easier in the short
term.

We will deploy the sidecar in our staging environment and connect to our Delius
staging environment from it.

## Consequences

We will have a consistent deployment pipeline between environments, and as
similar architecture as possible in the ways that matter to us.

We will have a Delius API instance to use a constructed dataset with in
staging.

We have some extra setup work to do before connecting to the Delius API in
production, but it will give us greater confidence in the security of our
approach.

We will need to create a certificate authority ourselves to use in our Delius
staging environment.

We will learn more about how the TLS mutual auth setup works, which will help
us use it with confidence.

We still need to find a way of running automated tests on the mutual auth
setup to ensure that it continues to work as intended.

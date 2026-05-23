# 12. Start out with one environment which uses T3 NOMIS

Date: 2018-11-21

## Status

Accepted

## Context

We want to run the smallest number of pre-production environments which give us
useful feedback on changes to our applications before we deploy them to
production.

We think that as we integrate with more systems (NOMIS, Delius, OASys etc) we
are likely to need more pre-production environments of our own in order to test
against pre-production environments of those systems. It's unlikely that data
will match up well across systems in those environments so we may need to
create matching data in them ourselves in order to test our applications.
We don't know yet how many pre-production environments would be useful for us
to have in this context.

We suspect that challenges around data quality and how quickly records are
matched will only be clear in production data, so we're keen to start working
with production systems as soon as we can. However only NOMIS has available
APIs in production, and working with only one system is less likely to reveal
the scale of those challenges.

So far we've set up [one environment for our new applications](https://github.com/ministryofjustice/cloud-platform-environments/tree/1afcd91536201415b868ccebcaf1aeb8ecc2d339/namespaces/cloud-platform-live-0.k8s.integration.dsd.io/offender-management-staging)
on the new cloud platform, called Staging.

It's straightforward and quick to set up further environments as we need them,
but there's no way at the moment to share config between cloud platform
environments so there is a code maintenance cost to having many environments.

We still need to finish setting up authentication on our applications as a
minimum before we start using production APIs to other systems. There's little
benefit in us having a Production environment ourselves until we can do that -
we're a long way from having real users.

Setting up authentication means that we need to pick a NOMIS pre-production
environment to use from our Staging environment, because we're going to use the
NOMIS OAuth2 server (see [ADR 0011](0011-use-nomis-oauth-server2-for-allocation-api-authentication.md)).

Our team already have comprehensive access to the T3 NOMIS environment from our
work on Visit someone in prison. That environment contains anonymised data,
which is sufficient for our needs at this stage. All the NOMIS-based services
we need are running there. It's commonly used as a development environment
(rather than staging) by other services.

## Decision

We will start out with one shared Staging environment for our new applications.

We will use the T3 NOMIS environment from that environment to start with.

## Consequences

We can get on with development work on setting up authentication against the T3
NOMIS environment.

We will need to set up more environments in future, when we're ready to start
calling production NOMIS APIs and when we need to test against pre-production
environments for Delius and other systems in combination.

We may need to move our T3 use to another environment or rename our Staging
environment to Development later on, if it makes more sense to use a different
NOMIS environment from our Staging environment.

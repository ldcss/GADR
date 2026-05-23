# 7. Use Ruby for new applications for Manage Offenders in Custody

Date: 2018-10-19

## Status

Accepted

## Context

### Language use across HMPPS

HMPPS has active development in four languages, including services with
significant prison-staff-facing components in all four: Ruby, Python,
JavaScript and Java.

HMPPS has live services (which have passed service assessments) built in Ruby
and Python. Ensuring that we support our existing users should be our top
priority, so it is essential to maintain our skills in the languages used in
our live services.

One of the advantages of a microservices approach is that teams can work on
separate services in different languages, using HTTP APIs to share data and
functionality. There is no need for all services to be built in the same
language. We are already using this approach across HMPPS.

There is no clear vision or strategy at the moment for changing the number of
languages in use across HMPPS. We are not in a position to decide that for all
of HMPPS.

### Team skills

All four languages in active use across HMPPS are represented to varying
degrees in the skill sets of the current members of the team, but only Ruby is
common to all of them. The team have worked together on a live service built in
Ruby for all of their time at MOJ/HMPPS. We still own that service and
continuously improve it alongside our work on Manage Offenders in Custody,
although we are spending the majority of our time on the latter.

The primary language skills of HMPPS's civil servant developers and technical
architect (a significant proportion of whom are on this team) are in Ruby and
Python. It is unrealistic to expect people to be equally proficient in many
languages at the same time.

The team have already committed to learning about Kubernetes for the new Cloud
Platform (see [ADR 0002](0002-use-cloud-platform-for-hosting.md)) and to
learning Java so that we can collaborate on the APIs which are being built in
Sheffield (see [ADR 0006](0006-use-the-custody-api-to-access-nomis-data.md)).
This is already a significant proportion of unfamiliar technologies for the
team to learn and use.

Developing applications involves much more than using the standard library of
a language. The ecosystem of libraries tools around that language often takes
much more work and time to become familiar with than the basics of the language
itself. Although all of the team know some JavaScript, we do not all have
experience of using it for building server-side applications. We would therefore
have a lot more to learn if we were to choose to use JavaScript, as some
related but separate services do.

### Time constraints

The Offender Management in Custody programme has fixed timelines for its
national rollout in the next year. Although we are not committing to delivering
particular services at set dates months in advance, we will reduce our
opportunity for learning from a smaller set of real users before the national
rollout if we are not ready to take advantage of the Wales pilot which begins
in January.

We know that allocations is only the first of several areas of the programme
which are likely to need support from us, so timescales are tight for us.

We anticipate that the complexity of building this service lies in managing the
quality of the data available across NOMIS, Delius and OASys, rather than in
representing that data to users.

Choosing to use a less familar language for developing our applications, on top
of what we already need to learn, would put us at significant risk of not
delivering working software until several months after our first users need it.

### Code reuse

Using the same language for groups of similar services can make it easier to
provide a coherent experience for users by allowing presentation code to be
shared more easily between services. However, the same HTML structure of pages
can be produced by services written in different languages. Since we are
committed to progressive enhancement (see [ADR 0003](0003-use-progressive-enhancement.md)),
we will use client-side JavaScript solely to enhance the functionality of those
pages, and that JavaScript can be reused across services regardless of the
language used on the server.

As an example of this approach, there is a strong and active cross-government
community which develops, researches and supports design patterns, styles and
components which are used on services built in many different languages:
https://design-system.service.gov.uk/

We will base our user-facing applications on this established design system in
any case. There is already a variety of design approaches in use across the
prison-staff-facing services we have, and our best chance of standardising that
well is to align ourselves with the cross-government approach.

That approach is supported by extensive user research over several years and
across many services and departments. Using it as our starting point reduces
the need for us to undertake duplicate research ourselves to understand the
effectiveness of alternatives to those existing patterns. We expect that we
will need to extend those patterns and develop others inspired by them to meet
our users' needs, and we will contribute what we learn back to the HMPPS and
cross-government communities.

Since it has been agreed that all services which need to use a NOMIS API should
migrate to the Custody API (see [ADR 0006](0006-use-the-custody-api-to-access-nomis-data.md)),
any API client library which we build in Ruby can be reused by other Ruby
services to ease their migration.

### Operational considerations

The team has considerable experience of operating live services built in Ruby
at scale.

We do not anticipate scaling to be a significant concern for allocation - we
expect to have a couple of hundred users a day at most for it.

The new Cloud Platform makes it easy, quick and cheap for us to scale up if we
need to.

## Decision

We will use Ruby for the new applications we build in London as part of Manage
Offenders in Custody.

## Consequences

We will build on the knowledge the team already has of the Ruby ecosystem.

We will not have to significantly deepen our knowledge of a third language (as
well as Ruby and Java), familarise ourselves with a different ecosystem of
libraries and decide on and learn another set of tools in order to make
progress.

We will be able to use the GOV.UK Design System as the basis for making our
services look consistent with other government and HMPPS services.

We may not be able to reuse libraries which are built by teams in Sheffield if
they are intended for use with particular JavaScript frameworks which we do not
need to use.

We will write client code in Ruby for the Custody API (and any other APIs we
use) which we could extract into libraries to be used by other Ruby services
when they migrate to use those APIs.

We will maintain a strong level of Ruby knowledge within HMPPS, which will help
us ensure that we can continue to support a significant proportion of our live
services in the future.

If HMPPS wants to ensure that we have civil servants with strong skills in the
other languages currently used across all its services, we will need to focus
on hiring in those areas rather than expecting our existing developers to be
able to work equally productively across all those languages.

# 8. use-different-aws-account-for-interacting-with-infrastructure-variables

Date: 2020-09-24

## Status

Accepted

## Context

The issue motivating this decision, and any context that influences or constrains the decision.

Dalmatian stores variables in AWS Parameter store. Each infrastructure has an `account_id`
associated with it which is used to manage which account variables are read, added and removed from - this is as you might expect.

Dalmatian also stores another type of variable which the app has initially given
the name of "infrastructure variable". These variables are NOT managed by the
individual AWS accounts associated with each infrastructure. Rather they are all
managed within a central AWS account and given a meaningful name space to relate
it to a dependent service.

For this apps purposes it would have been easier for all variables associated with
a service to live in the same account. I believe there are restrictions to how
Dalmatian itself (rather than the services there on) is deployed which has steered
Dalmatian into being designed this way.

## Decision

Handle the complexity of 2 different types of AWS Client within the service rather
than seeking to change the way infrastructure variables are provisioned to align
with the infrastructure they belong to.

## Consequences

- The application will have complexity layered into it which makes it more
complex which may make it harder to understand and work with.
- Users of this service must align the way they managed their AWS Parameter store
with the design of Dalmatian core

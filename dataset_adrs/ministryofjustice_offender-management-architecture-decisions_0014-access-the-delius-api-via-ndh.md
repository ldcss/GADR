# 14. Access the Delius API via NDH

Date: 2018-12-12

## Status

Accepted

## Context

### Data and policy

We've known since very early on in our work on Manage Offenders in Custody that
we have a critical dependency on being able to use current or very recent data
from Delius to inform the allocation process, in line with the new OMiC policy.

The policy defines two pieces of data which determine the type of Prison
Offender Manager who can be allocated, and which staff in prisons have no other
access to:

- whether the case will be handled by the National Probation Service or a
Community Rehabilitation Company
- the tier (A/B/C/D), which is based on the scores for three risk assessments

Our user research has indicated that other information held in Delius is also
likely to be useful in informing the allocation decision, and is important for
POMs and Senior Probation Officers in carrying out their responsibilities under
OMiC.

One of the main aims of the policy is to enable prison and probation services
to work together more effectively, for which better sharing of information is
crucial.

### Existing Delius API

An API for Delius already exists and is deployed alongside Delius, but is only
accessible from inside that environment. Providing secure access to the API for
other services has long been thought to depend on the Delius migration to AWS
being completed.

However that migration has taken longer than originally hoped, and we need to
find a viable approach to get access to the data we need so that we can provide
a service which has some value for our users.

We know that some work on the API itself will also be needed to make it return
the data we need, but getting access to the API at all is the more significant
challenge.

The API itself does not have authentication built in at the moment, so all
access to it needs to be secured in other ways. It will use the NOMIS OAuth
server in future.

### Overnight extract

In the absence of API access, the Home Detention Curfew team have set up an
overnight batch process to write the names of responsible officers into NOMIS
from a Delius extract.

We could use this approach for the data we need for MOiC, but it's far from
ideal for us:

- We wouldn't have live data available, which could lead to allocation
decisions being made on the basis of outdated risk information
- It would introduce more dependencies on an outdated architectural pattern
- Duplicating data between systems means that the ownership of the data is
unclear
- We would need to support this approach until the API is accessible, and then
switch to using the API - this would take more work and redesigning interfaces
than using the API from the start

We want to avoid this approach if we possibly can, but will consider it as a
last resort.

### Other services which might provide risk assessment data

We have also heard that another team's work around risk assessments might make
the data we need available from their new service, but we have just learned
that the scope of their work doesn't extend that far in the timescales we're
working to.

### Delius API access via NDH

Another option was proposed recently: to give us access to the API via the
NOMIS Data Hub, which already has secured access to the API. We could do this
with mutual TLS auth between the NDH and our allocation manager, using the
sidecar pattern with our application. This approach is estimated to need less
than a week of work and isn't dependent on the Delius migration being
completed.

We would need help from people working on the Delius migration to take this
approach, particularly in setting up mutual auth on the NDH end, but given the
extent to which this approach unblocks our work on MOiC that is a reasonable
tradeoff. We would need help from the same people for any of the approaches
we've considered.

The NDH only exists in production, so if we take this approach we will need to
decide what to do in other environments. We know that Delius and NOMIS don't
have any shared pre-production environments anyway, so we don't expect this to
cause any extra problems for us.

## Decision

We will set up access to the Delius API via the NDH route.

When the API is accessible through a more standard route, with authentication,
we will switch to use that.

We will keep our deployment pipeline consistent by using the
mutual-auth-via-sidecar pattern in our pre-production environments as well as
in production, if possible.

## Consequences

We will be able to get access to the data we need from Delius much sooner than
we had expected, enabling us to deliver sooner and meet our users' needs much
better.

We will only have to make minimal changes to our applications to switch to use
the API with authentication through another route later on.

We need to set up a production environment as soon as possible, so that we're
ready to work on and test the NDH route on our side as soon as the work is done
on the other end.

We will need some time and help from people who can help us get this route set
up, particularly at the NDH end.

We will need to define a workable approach to managing certificates.

# 4. Pin versions of Jenkins and plugins

Date: 2018-08-06

## Status

Accepted

## Context

To guide our work, we need to decide on our approach to supporting (or not)
a build system that we may provide. This document outlines the pros and cons of
possible options and recommends an approach. 

Once decided, this decision will be used to hold further workshops to design the
processes and technology required to put that approach into practice. 

### The options

We discussed 3 options that affect our support approach, plus a fourth that
involves a third party and does not necessarily affect the way we support our
product. As such, the fourth does not have pros and cons articulated below. 

1. Release a working and stable infrastructure as code. Unpinned versions, so 
   each fresh installation includes the latest versions of everything.
2. Host it (essentially become a SaaS provider) and maintain a limited suite of
   plugins.
3. Periodically release stable versions of Jenkins (as code), with a suite of
   plugins with their versions pinned. Provide guidance on upgrading with each
   release.
4. Pay for an externally hosted (and therefore maintained) version of Jenkins.
   Don’t provide anything ourselves except recommendation and perhaps a little
   guidance

Hybrids of some of these are possible. For example, we could have Jenkins as
code (1 or 3) for those who need more configurability whilst also
recommending/paying for an externally hosted thing (4). Or we could both provide
code (1 / 3) and also host something (2). 

### Option 1: Infrastructure as code only

**Pros**

* Supposedly more secure (because latest versions include security updates)
* Encourages good behaviour (not providing a black box solution forces teams to
engage with the solution)

**Cons**

* Implicit trust up-stream means security vulnerabilities could be introduced
* Everything could break each time a new version is released (we can’t ensure
  compatibility)
* The build becomes unreproducible
* Build versions can’t be tracked
* Latest versions would only be installed for fresh installs, so potentially
  increasing divergence from secure versions

### Option 2: Host Jenkins ourselves

**Pros**

* Teams transfer all of the ‘cons’ to us
* Teams don’t need certain expertises
* We can enforce upgrades (security)

**Cons**

* Expensive (people, infrastructure, etc.)
* Cost recovery has to be dealt with
* Cost might be a barrier to adoption
* Less configurable for teams
* Residual unused instances have to be managed
* Have to manage OLAs/SLAs
* Need MTM/SMT agreement
* Service becomes a single point of failure for all service teams using it
  (up-time, etc.)

### Option 3: Release stable pinned versions periodically

**Pros**

* Users are reassured that it will work
* ^ therefore lower barrier to adoption
* Central point for monitoring security fixes
* Automated testing (integration/acceptance) of version compatibility, etc. is
  possible
* Guidance and optimised workflow = easier for teams to do things properly

**Cons**

* Someone has to stay current (security and updates)
* Someone has to maintain and update it
* Limited plugins: the fewer we support the more teams have to support (but may
  not)
* Limited plugins: if teams use a lot around GDS then maybe puts pressure on us
  to provide more in our 'limited' suite


## Decision

Based on the above pros and cons, we recommend that option 3 (perhaps with
option 4 as well, depending on user needs that are uncovered) is the best
option. 

## Consequences

We will support a limited set of plugins which will be pinned to specific
versions. We will need to agree a release cycle for supported versions, and
document an upgrade process.

# 3. Use VueJS 3

Date: 2020-09-17

## Status

Accepted

## Context

We reviewed various options for building our front end and decided Vue.js was
the best fit. However, Vue is preparing for a major version upgrade. We could
choose to use the current stable version (2) and migrate to the new version (3)
when it is released or start with the release candidates for the new version.

## Decision

We will use Vue.js 3 releases candidates.

## Consequences

Using the release candidates will allow us to more easily transition to the
new stable release when it is released while gaining immediate access to some
compelling new features.

Our development timeline is long enough that any risks of Vue.js 3 not being
released before we are in production are minimal. However, if the timeline for
Vue 3 final slips past our likely production app launch, we will need to assess
the risk associated with using a potentially unstable release based on all
information available.

We will need to update to each release candidate version that comes out to
ensure we address any changes that may be introduced before the final release.
It is possible some work will need to be adjusted if the APIs change during
release candidate phases.

Vue is a new technology for our team. If, because of Vue 3 or just Vue in
general, we find our development is slower than expected or we are unable to
complete the work necessary for success, we can pivot to a traditional Rails
application and still benefit from any HTML or CSS we develop during the Vue
development process.

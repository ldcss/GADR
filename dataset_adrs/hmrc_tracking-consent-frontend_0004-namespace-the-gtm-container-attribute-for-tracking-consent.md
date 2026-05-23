# Namespace the gtm.container attribute for tracking consent

* Status: accepted
* Date: 2020-11-05

## Context and Problem Statement

Our existing guidance for service developers implementing tracking consent
asks developers to set the `gtm.container` key in `application.conf` to 
configure the GTM container used by tracking consent.

This configuration key was already used by play-ui in its GTMSnippet component and the 
intent was by re-using this key, it would be simpler for service developers to integrate
if they are already using play-ui to provide their GTM integration.

Unfortunately, setting this key in application.conf can break services using
play-ui because gtm.container is an implicit feature toggle for 
GTMSnippet and GTMSnippet is not designed to work locally. It requires configuration keys 
like gtm.<CONTAINER>.url that are only defined on the MDTP platform environments 
(via app-config-common)

Should tracking-consent-frontend, therefore, use its own gtm.container attribute namespaced inside
the tracking-consent-frontend configuration block? For example,

```
tracking-consent-frontend {
  gtm.container = "a"
}
```

## Decision Drivers

* The need to keep things simple for service developers
* The desire not be constrained by the design decisions made for the existing
GTMSnippet
* The need to be able to test the GTM integration and tracking consent banner locally

## Considered Options

* Continue to use gtm.container but only allow testing in an environment
* Move gtm.container inside the tracking-consent-frontend configuration block

## Decision Outcome

Chosen option: "Move", because we want to support testing tracking consent locally.

### Positive Consequences

* Service developers do not receive an error when integrating with tracking consent
* Tracking consent can be tested locally
* This decision can be implemented by a simple update to the existing guidance with no 
further code changes to tracking consent
* No changes are needed for the proposed helpers for play-ui and play-frontend-hmrc
* Tracking consent is not constrained by the design choices made for GTMSnippet

### Negative Consequences

* Services uplifting from GTMSnippet will need to move the gtm.container key into the
tracking-consent-frontend configuration block.

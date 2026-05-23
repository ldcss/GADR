# Approach for Integrating and Customising the Universal Viewer

* Status: proposed
* Deciders: Daniel Grant <daniel.grant@digirati.com>, Gary Tierney
  <gary.tierney@digirati.com>, Stephen Fraser
  <stephen.fraser@digirati.com>
* Date: 2021-02-17

## Context and Problem Statement

The Universal Viewer currently has a model for customisation using
forked repositories. We need to use BFI's own fork that exists on GitHub
and modify it to track events for this project. We also need a way to
deploy the various built assets for the viewer.

## Decision Drivers

* Ease of future customisation for BFI
* Ease of integration for Digirati

## Considered Options

* Submodule the examples repository
* Build components of UV in our solution
  ([example](https://github.com/UniversalViewer/uv-hello-world))

## Decision Outcome

Chosen option: "Submodule the example repository", because it will keep
the application largely agnostic of the viewers that are integrating
with it and will reduce build complexity.

### Positive Consequences

* No frontend build considerations
* Updates can be automated with Dependabot

### Negative Consequences

* Universal viewer (UV) submodule contains the built viewer in source
  control, but this is a pattern of the UV currently.

## Pros and Cons of the Options

### Submodule the examples repository

This follows a pattern that users of the UV currently follow. The
standard examples repository found here:
https://github.com/universalViewer/examples is forked and changes made
are built and committed to this repository. Some institutions choose to
fork the whole
[Universal Viewer repository](https://github.com/UniversalViewer/universalviewer)
which itself has a submodule for the examples repository.

This approach will produce a proven and built Universal Viewer instance
with required customisations. This repository can then be further
customised in a way supported by the wider UV community and used by this
solution.

* Good, because it is the standard way in the UV to customise
* Good, because it will be quick to integrate
* Bad, because submodules require updating - but can be mitigated with
  automation
* Bad, because built code will be in source control in the forked
  Universal Viewer repository
* Bad, because the Universal Viewer needs to be manually updated and
  built

### Build components of UV in our solution

This pattern involved installing the Universal Viewer (UV) and all of
its dependencies, copying the static assets and then writing our own
HTML to bootstrap the page.

* Good, because it will use the latest available version of the
  Universal Viewer - although this has not always been stable
* Good, because no built assets are stored in source control
* Bad, because the automations will take longer to set up and builds
  will take longer going forward
* Bad, because the community support is less geared towards these types
  of customisations.

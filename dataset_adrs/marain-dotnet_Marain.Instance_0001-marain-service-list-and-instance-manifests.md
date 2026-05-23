# Marain Service List and Instance Manifests

## Status

Accepted.

## Context

The desire to define formally and unambiguously what are the component parts of a Marain instance. (An 'instance' is one deployed set of services operating in isolation from any other instance. We maintain a dev instance separate from any production use. Where customers use Marain services but are not using endjin's hosted production instance, they have their own instance.)

## Decision

The `Marain.Instance` repo (this repo) includes a master service list, `Solutions/MarainServices.jsonc`. This JSON (with comments) file contains an entry for each service that can be part of a Marain instance. This gives a name to the service (e.g. `Marain.Tenancy`) and identifies the GitHub project in which the service is defined. It also defines an API prefix, for use in scenarios where all services are made available behind a single API management layer—the API prefix indicates what the first part of the URL should be at the API gateway for accessing the relevant service.

Whereas `MarainServices.jsonc` is common to all instances, each instance also defines a manifest. This determines whether particular services are deployed to a particular instance, and if so which version.

## Consequences

By putting this information in JSON (or JSONC) files with a narrowly defined purpose it is very easy to see exactly what services can go into a Marain instance, and which particular versions are deployed to a particular instance. It also drives the automaticed deployment process implemented by `Deploy-MarainInstanceInfrastructure.ps1`.
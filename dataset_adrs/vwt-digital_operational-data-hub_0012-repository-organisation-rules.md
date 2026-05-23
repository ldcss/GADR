# 12. Repository organisation rules

Date: 2021-05-10

## Status

Accepted

## Context

We feel the need to define rules to select the correct GitHub organisation for source repositories.

## Decision

We identify rules for the GitHub organisation, the source repository name format and basic source code guidelines.

### VWT Digital

This is the main organisation for all Operational Data Hub (ODH) specific source code. When creating a new repository, 
it **has to pass** one of the following applications:
- An ODH-specific solution;
- A solution that transcends multiple solution domains (see [solution domains](https://recognize.atlassian.net/wiki/spaces/DAT/pages/1304166628/Cloud+naming+convention#Cloudnamingconvention-Domains)).

In addition, these repositories **may not** contain:
- Any configuration;
- Any solution business logic.

When creating a name for the repository, it **has to start** with either `odh-<repo_name>` or `dat-<repo_name>`:
- `odh-`: When the repository contains source code specifically made for the Operational Data Hub;
- `dat-`: When the repository contains source code created for generic usage within the Digital Ambition Team domain.

See our [repo naming convention](0002-repo-naming-conventions.md#4-normal-vwt-dat-repositories) for a more elaborate explanation.

### VWT Digital Solutions

This is the main organisation for all Solution-specific source code. When creating a new repository, it **has to pass** the following application:
- A specific application for a domain solution, only used by one domain (see [solution domains](https://recognize.atlassian.net/wiki/spaces/DAT/pages/1304166628/Cloud+naming+convention#Cloudnamingconvention-Domains)).

In addition, these repositories **may not** contain:
- Any configuration.

When creating a name for the repository, it has to start with the abbreviation of the solutions it is a part of.

See our [repo naming convention](0002-repo-naming-conventions.md#4-normal-vwt-dat-repositories) for a more elaborate explanation.

### VWT Digital Configuration

This is the main organisation for all configuration code. When creating a new repository, it **has to pass** the following application:
- Google Cloud Platform (GCP) project-specific configuration code that is for private usage only.

When creating a name for the repository, it has to contain the GCP project they are connected to minus the customer, 
environment and location. Furthermore, it has to end with `-config`.

See our [repo naming convention](0002-repo-naming-conventions.md#4-normal-vwt-dat-repositories) for a more elaborate explanation.

## Consequences

# Selection of Identity Management Platform

* Status: Accepted
* Deciders: [Daniel Grant](https://github.com/danielgrant),
  [Robert Kenny](https://github.com/kenoir),
  [Paul Mollahan](https://github.com/pmollahan), [Gary
  Tierney](https://github.com/garyttierney),
  [Jonathan Tweed](https://github.com/jtweed)
* Date: 2020-10-02

Technical Story: to identify a managed Identity and Access Management
platform to form the core of the delivery of the Wellcome Collection
Identity project.

## Context and Problem Statement

Wellcome Collection wishes to implement an Identity and Access
Management platform, to provide authentication and authorisation
services. Such a service is required to integrate with Wellcome
Library's existing pool of registered library members, and would expose
itself through recognised, standards based protocols.

## Decision Drivers

* Ease of implementation and ongoing maintenance.
* Low / nil upfront and ongoing subscription costs.
* Ability to integrate with, and maintain, an existing user pool.

## Considered Options

* AWS Cognito
* Auth0

## Decision Outcome

Chosen option: Auth0, because it offers superior integration with
existing user pools.

## Pros and Cons of the Options

### AWS Cognito

- Good, because it is effectively free to use for lower usage tiers.
- Bad, because integration with third-party user pools is complex and
  limited.
- Bad, because it enforces the existence of an unwanted immutable
  "username" attribute.
- Bad, because core configuration options cannot be changed without
  destroying and recreating the AWS Cognito resource.
- Bad, because the degree of customisation for user interfaces and
  automatically generated emails is not sufficient for the identified
  use cases.

### Auth0

* Good, because it provides simple integration with a third-party user
  pool via custom scripts that can run any NodeJS code on login / user
  lookup.
* Good, because it does not require the use of usernames (i.e. email
  addresses only).
* Good, because it ships with a large number of SSO / social /
  enterprise integrations out-of-the-box.
* Good, because it offers the ability to extensively customise hosted
  pages (e.g. login / forgot password).
* Bad, because depending on usage, ongoing subscription costs can be
  significant.

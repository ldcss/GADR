# Make tracking consent available on non-tax domains

* Status: accepted
* Date: 2020-12-15

Technical Story: PLATUI-892

## Context and Problem Statement

In the context of the need to support MDTP domains other than www.tax.service.gov.uk (non-tax domains), facing the need
to keep things simple for service developers and for tracking preferences to be stored on the
correct domain, should we make tracking consent available on non-tax domains and advise using a relative URL to link to 
it except when running locally, adjusting the helpers in play-ui and play-frontend-hmrc accordingly?

At the moment, if tracking consent is integrated with a service not on www.tax.service.gov.uk via an
absolute URL, users visiting the preferences page will have their preferences set on the incorrect domain.

This decision does not introduce the need for any technical changes to tracking consent itself other than adding routing
for the additional domains as required, but it does require changes to the integration guidance and helpers that are used to link to 
tracking consent because they currently use an absolute URL derived from the `platform.frontend.host` configuration key.

## Decision Drivers

* The need to support the MDTP-hosted API platform on developer.service.hmrc.gov.uk and corresponding 
lower environments
* The need to ensure tracking preferences are set on the correct domain
* The potential need to support other similar non-tax domains in future
* The need to reduce boilerplate code across MDTP services
* The need to support local development
* The limitation around non-tax users seeing the same content on the banner and settings page.

## Considered Options

* Do nothing, not support non-tax domains.
* Update integration guidance and helpers to use a relative URL.

## Decision Outcome

Chosen option: "Update integration guidance and helpers", because making this change is technically straightforward, does not 
undermine the solution, and the API platform are aware of the limitations around content.

### Positive Consequences

* Third party developers using the API platform will be able to adjust their tracking preferences using tracking consent.
* The API platform does not need to source or develop their own consenting solution or develop and review bespoke
cookie categories and content.
* The API platform can use a consenting solution consistent with the rest of the platform including API 
platform frontend microservices that do run under the tax domain
* The API platform can use the same data format and technical mechanism for storing tracking preferences.
* We are supporting the frontend needs of the API platform consistent with the principle that all MDTP hosted services
 can benefit from the same frontend components and services.

### Negative Consequences

* The API platform will not be able to customise the content on the banner or settings page (this limitation has been communicated
to the team).
* Content designers will need to bear in mind that the tracking consent content is being used on the developer hub aimed at third
party developers.
* The scope increase and risk of future pressure to make additional changes to tracking consent that may undermine the solution's conceptual
integrity.

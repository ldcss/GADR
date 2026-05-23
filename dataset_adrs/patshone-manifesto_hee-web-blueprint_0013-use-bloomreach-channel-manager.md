---
layout: layouts/page.njk
title: ADR-0013 Use Bloomreach channel manager
pageTitle: ADR-0013 Bloomreach channel manager
pageDescription: 
path: /blueprint
permalink: /blueprint/adrs/ADR-0013-use-bloomreach-channel-manager.html
eleventyNavigation:
  parent: Architecture decisions
  key: ADR-0013 Use Bloomreach channel manager
  order: 13
---

Date: 2020-06-08

## Status

Pending

## Context

We sought to determine whether to deliver our document management capabilities using the content management platform natively or through the integration of an external document management platform.

We sought to determine whether Bloomreach's 'Channel' concept would be suitable for managing the various sites required to be brought onto the platform both at MVP and in the future, such as Deenary and Speciality sights. 

As part of this, considerations were made around: 
* Ease of use for creating new sites
* Ability to share components 
* Ability to segregate content for specific channels (sites)
* Ability to share content up and down the stack where needed and appropriate
* Permissions model required to support this model

## Decision

Bloomreach's concept of channels is well suited to meet the needs of running the sites required under the NWP platform umbrella. Channels offer the ability to build new sites that share components and modules, which enables for greater consistency. By utilising roles and permissions from within BR, content can be segregated to be available only where it is most relevant, whilst allowing for content to be made available up or down the organisational stack (e.g. national content being aggregated at a regional level). 

BR's 'blueprinting' functionality allows for sites to be created using a series of parameters, further standardising the creation of sites where needed in an easy fashion. 

## Consequences

The channel and blueprinting functionality are core offerings of the product and are well documented

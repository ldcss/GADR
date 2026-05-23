---
layout: layouts/page.njk
title: ADR-0010 Use external document management system
pageTitle: ADR-0010 Use external document management system
pageDescription: 
path: /blueprint
permalink: /blueprint/adrs/ADR-0010-use-external-document-management-system.html
eleventyNavigation:
  parent: Architecture decisions
  key: ADR-0010 Use external document management system
  order: 10
---

Date: 2020-04-11

## Status

Accepted

## Context

We sought to determine whether to deliver our document management capabilities using the content management platform natively or through the integration of an external document management platform.

### Options

#### NHS Digital BloomReach

We looked at the implementation of document management functionality in BloomReach delivered as part of the work for NHS Digital - https://github.com/NHS-digital-website/hippo. This project provides a good view of what native BloomReach document management and publishing looks like, it delivers a flexible content model for publishing to HTML documents. 

#### Office 365

In addition we should look at the current usage of Office 365 to determine whether the platform would be suitable for integration with BloomReach.

#### FutureNHS
Finally looked at the FutureNHS collaboration platform to see whether it would be suitable for integration with BloomReach. Whilst the platform in its current state would be a good candidate for integration, we discovered that at the time of writing, this platform is due to be rewritten. 

## Decision

We believe that Microsoft Office 365 and Sharepoint provide a good basis for the platforms document management capabilities and we have proved that it can be successfully integrated.

Having looked at the requirements for LKS staff, particularly around the ability to support a range of document types such as spreadsheets and presentations, our belief is that we would be better placed to integrate an external document management system. The NHS Digital publishing platform provides an excellent HTML publishing model and workflow, however extending it to support a broader range of document types would be complex.

FutureNHS may provide a good candidate for integration in the future, however at the time of writing it is difficult to recommend as the product is in the process of being rewritten.


## Consequences

An integration with an external system brings additional complexity as it requires the wiring in of an external system, however it moves the responsibility for providing a broad range of document management capabilities to a dedicated platform

---
layout: layouts/page.njk
title: ADR-0012 Use external search service
pageTitle: ADR-0012 Use external search service
pageDescription: 
path: /blueprint
permalink: /blueprint/adrs/ADR-0012-use-external-search-service.html
eleventyNavigation:
  parent: Architecture decisions
  key: ADR-0012 Use external search service
  order: 12
---

# 12. Use external search service

Date: 2020-06-08

## Status

Pending

## Context

We sought to determine whether the native out of the box solution provided by the platform nativly would be fit for purpose, or if an external service would be required. 

For the purpose of the decision, the following were considered as requirements:

* Flexible facet management
* Synonym configuration 
* Query suggestions
* Configurable misspelling tolerance
* Natual language query support
* Ability to integrate with external sources

### Options

#### Native Bloomreach Lucene Search

The OOTB search provided by the platform nativly is provided by Apache Lucene. This native search option provides standard search options, including free text search and faceted filters. Common query types are supported, such as wildcard searches. 

Whilst the native search functionality is fine for simple content websites, it lacks some of the enhanced functionality and configurability that the final solution will be asked to provide, including synonym configuration. 

#### Bloomreach Search & Merchandising (brSM) 

Bloomreach offer an enhanced managed search service, called 'Search & Merchandising'

https://www.bloomreach.com/en/products/search-merchandising

This tool provides several additional pieces of functionality including semantic understanding and personalisation. The product however is geared in the first instance to product and merchansing and many of the features are directed towards that usecase.  

NHS digital are undertaking some work to prove out the use of brSM for this scenario. This is one of the first POCs using this search tool outside of a comemerce functionality. 

#### Algolia

Algolia is a decided search-as-a-service product that provides much of the functionality needed out of the box, including synonym support and filters and facets. It is also highly customisable through the UI, allowing for non-developers to configure, adjust and maintain the search offering. 

Algolia also offers prebuilt configurable front end components, which make implementing the search experience quick and easily.

#### Azure Cognative Search

Microsoft offer a cloud search service called Azure Cognative Search. This is a scalable search-as-a-service product, with a focus on machine learning powered capabilities such as optical character regognition 

#### Amazon Kendra/ Elasticsearch 

Amazon has long provided a well regarded open source search solution called Elasticsearch, which can be run on premises or on an EC2 or managed search instance. Amazon also offered Kendra, which is a machine learning based search service. 

## Decision

We believe that an external search service will be required to provide all of the capabailities that will ultimatly be needed to meet the complex user experience needs. Further to that, using an external search service will better suit the service based architectural model, where the search service will likely need to ultimatly take data from a variety of services such as the LKS document and colberation platform, and in future potentially other services such as Oriel and TIS. 

Using a managed service such as Algolia provides a good balance between powerful and user friendly functionality and implementation complexity - Algolia was chosen as the basis for the POC in part owing to its comprehensive service offering combined with its prebuilt react component library offering fast and efficient implementation. 

Bloomreach Search and Merchandising is an interesting option that provides advantages being tightly integrated into the core CMS project, however using it outside of commerce is somewhat unproven in the market. 

Search as a service options such as Elastic or Azure Cognative search would also be viable candidates (assuming the organisational goal of aligning more functionality to MS's offerings, Azure would likely be recommended ahead of Elasticsearch), and the cost models of these offer likely cost savings, the trade off is more complexity to implement and maintain.  

## Consequences

An integration with an external search provider brings additional complexity to the architectural stack, and requires additional considerations during development, as well as an additional ongoing cost for procuring the service (if a managed service is selected). 

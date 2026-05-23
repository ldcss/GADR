---
layout: layouts/page.njk
title: ADR-0009 Use react to manage and develop the components for the HEE frontend framework
pageTitle: ADR-0009 Use react to manage and develop the components for the HEE frontend framework
pageDescription: 
path: /blueprint
permalink: /blueprint/adrs/ADR-0009-use-react-to-manage-and-develop-the-components-for-the-hee-frontend-framework.html
eleventyNavigation:
  parent: Architecture decisions
  key: ADR-0009 Use react to manage and develop the components for the HEE frontend framework
  order: 9
---

# 9. Use react to manage and develop the components for the HEE frontend framework

Date: 2020-04-04

## Status

Pending

## Context

We sought to identify a single templating language that would provide a source of truth across our frontend & content management platforms. This aim seeks to reduce the effort in developing on the content management platform by mitigating the burden of markup integration. We also aimed to find a templating language that allowed us to utilise the components already created as part of the NHSUK frontend framework.

### Options

We identified three main candidates to use as our templating language:

#### Freemarker: 

Freemarker - https://freemarker.apache.org/ is the native templating language used by BloomReach and although there are projects that provide the ability to parse Freemarker templates with Javascript - this would be a prerequisite to using a tool like StoryBook to manage the frontend components - choosing Freemarker and utlising the prexisting work of the NHSUK Frontend project would require implementing and maintaining Freemarker versions of those components.


#### Nunjucks:

Nunjucks - https://mozilla.github.io/nunjucks/ is the native templating language used by the NHSUK Frontend project. It's syntax is similar to the Jinja templating language which is widely used in Python application development. Choosing Nunjucks would require implementing a custom integration with BloomReach using that platforms SPA/headless functionality. Integrating with StoryBook would require the creation of a custom StoryBook renderer.  


#### React:

React - https://reactjs.org/ is a fuller javascript framework for building UIs. BloomReach provides an out of the box, if perhaps somewhat nascent integration with React through its SPA/headless functionality. StoryBook provides full support for React and NHS Digital have developed and maintain an implementation of the NHSUK Frontend in React

- https://github.com/NHSDigital/nhsuk-react-components


## Decision

We will use React to develop the HEE Frontend platform.

## Consequences

We should look to describe a fallback rendering path for user agents that are unable to render an in browser React application. BloomReach provides support for server side rendering using Next.js - https://nextjs.org/ which mitigates this risk. 
